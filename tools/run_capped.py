"""Run one command inside a Windows job capped at 2 GiB total.

Usage: python tools/run_capped.py -- python path/to/probe.py
Copied from the AK safety runner for this paper's development workflow.
The child and its descendants share the job's committed-memory limit. The
remote model and tool-server processes are not covered by this local job.
Requires the already-installed psutil package to resume a suspended child.
Default wall timeout is 60 seconds; expiration terminates the whole job.
For diagnostics use --limit-mib 512 --timeout-seconds 60. Limits apply only
to commands launched through this wrapper, not unrelated host processes.
"""

from __future__ import annotations

import argparse
import ctypes
from ctypes import wintypes
import os
import math
import subprocess
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit-mib", type=int, default=2048)
    parser.add_argument("--timeout-seconds", type=float, default=60)
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command
    if command and command[0] == "--":
        command = command[1:]
    if not command:
        parser.error("supply a command after --")
    if not 32 <= args.limit_mib <= 2048:
        parser.error("limit must be between 32 and 2048 MiB")
    if not math.isfinite(args.timeout_seconds) or args.timeout_seconds <= 0:
        parser.error("timeout must be a positive finite number of seconds")
    if sys.platform != "win32":
        parser.error("this job-object runner requires Windows; no uncapped fallback")
    import psutil

    class BasicLimits(ctypes.Structure):
        _fields_ = [
            ("PerProcessUserTimeLimit", ctypes.c_longlong),
            ("PerJobUserTimeLimit", ctypes.c_longlong),
            ("LimitFlags", wintypes.DWORD),
            ("MinimumWorkingSetSize", ctypes.c_size_t),
            ("MaximumWorkingSetSize", ctypes.c_size_t),
            ("ActiveProcessLimit", wintypes.DWORD),
            ("Affinity", ctypes.c_size_t),
            ("PriorityClass", wintypes.DWORD),
            ("SchedulingClass", wintypes.DWORD),
        ]

    class IoCounters(ctypes.Structure):
        _fields_ = [(name, ctypes.c_ulonglong) for name in (
            "ReadOperationCount", "WriteOperationCount", "OtherOperationCount",
            "ReadTransferCount", "WriteTransferCount", "OtherTransferCount",
        )]

    class ExtendedLimits(ctypes.Structure):
        _fields_ = [
            ("BasicLimitInformation", BasicLimits),
            ("IoInfo", IoCounters),
            ("ProcessMemoryLimit", ctypes.c_size_t),
            ("JobMemoryLimit", ctypes.c_size_t),
            ("PeakProcessMemoryUsed", ctypes.c_size_t),
            ("PeakJobMemoryUsed", ctypes.c_size_t),
        ]

    kernel = ctypes.WinDLL("kernel32", use_last_error=True)
    kernel.CreateJobObjectW.argtypes = [ctypes.c_void_p, wintypes.LPCWSTR]
    kernel.CreateJobObjectW.restype = wintypes.HANDLE
    kernel.SetInformationJobObject.argtypes = [
        wintypes.HANDLE, ctypes.c_int, ctypes.c_void_p, wintypes.DWORD,
    ]
    kernel.SetInformationJobObject.restype = wintypes.BOOL
    kernel.AssignProcessToJobObject.argtypes = [wintypes.HANDLE, wintypes.HANDLE]
    kernel.AssignProcessToJobObject.restype = wintypes.BOOL
    kernel.CloseHandle.argtypes = [wintypes.HANDLE]
    kernel.CloseHandle.restype = wintypes.BOOL
    kernel.TerminateJobObject.argtypes = [wintypes.HANDLE, wintypes.UINT]
    kernel.TerminateJobObject.restype = wintypes.BOOL

    job = kernel.CreateJobObjectW(None, None)
    if not job:
        raise ctypes.WinError(ctypes.get_last_error())
    process = None
    try:
        limits = ExtendedLimits()
        limits.BasicLimitInformation.LimitFlags = 0x200 | 0x2000
        limits.JobMemoryLimit = args.limit_mib * 1024 * 1024
        if not kernel.SetInformationJobObject(job, 9, ctypes.byref(limits), ctypes.sizeof(limits)):
            raise ctypes.WinError(ctypes.get_last_error())
        env = os.environ.copy()
        for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                     "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "BLIS_NUM_THREADS"):
            env[name] = "1"
        process = subprocess.Popen(command, env=env, creationflags=0x00000004)  # CREATE_SUSPENDED
        if not kernel.AssignProcessToJobObject(job, wintypes.HANDLE(int(process._handle))):
            raise ctypes.WinError(ctypes.get_last_error())
        print(f"AK cap active: {args.limit_mib} MiB; timeout={args.timeout_seconds:g}s; numerical threads=1", file=sys.stderr, flush=True)
        psutil.Process(process.pid).resume()
        try:
            return process.wait(timeout=args.timeout_seconds)
        except subprocess.TimeoutExpired:
            print("AK timeout: terminating the contained process tree.", file=sys.stderr, flush=True)
            if not kernel.TerminateJobObject(job, 124):
                raise ctypes.WinError(ctypes.get_last_error())
            process.wait(timeout=10)
            return 124
    finally:
        # KILL_ON_JOB_CLOSE also removes descendants after an ordinary exit or
        # interruption. No process names or unrelated PIDs are targeted.
        kernel.CloseHandle(job)
        if process is not None and process.poll() is None:
            process.kill()
            process.wait(timeout=10)


if __name__ == "__main__":
    raise SystemExit(main())
