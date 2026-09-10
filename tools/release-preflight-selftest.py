"""Bounded nonmathematical controls for the UNRELEASED custody helper."""
from pathlib import Path
from unittest.mock import patch

namespace = {"__file__": str(Path(__file__).with_name("release-preflight.py")),
             "__name__": "release_preflight_test_target"}
exec(compile(Path(namespace["__file__"]).read_text(encoding="utf-8"),
             namespace["__file__"], "exec"), namespace)


def rejected(action):
    try:
        action()
    except (ValueError, FileNotFoundError):
        return
    raise AssertionError("unsafe or invalid input was accepted")


def main():
    safe = namespace["safe_path"]
    for bad in ["../README.md", "/README.md", "C:/README.md", "paper\\resolution.tex", ""]:
        rejected(lambda: safe(bad))
    exclude = namespace["excluded"]
    for generated in ["tmp/test.tex", "output/pdf/resolution.pdf", "paper/resolution.aux",
                      "lean/I3322Kernel/.lake/test", "review/end-to-end-2026-09-10/CLEANUP-REPORT.md",
                      "review/revision-2026-09-10/baseline/resolution.tex"]:
        assert exclude(generated), generated
    for kept in ["paper/resolution.tex", "paper/resolution.pdf", "certificate/release/release-manifest.json",
                 "tools/release-preflight.py"]:
        assert not exclude(kept), kept
    assert namespace["source_plan"]()["archive_members"] == ["LOWER-BOUND-REVISION.tex", "resolution.tex"]
    paths = ["paper/LOWER-BOUND-REVISION.tex", "paper/resolution.tex"]
    with patch.dict(namespace, {"inventory": lambda: paths}):
        data = namespace["snapshot"]()
        assert namespace["verify_manifest"](data) == 2
        data["files"][0]["sha256"] = "0" * 64
        rejected(lambda: namespace["verify_manifest"](data))
        data = namespace["snapshot"]()
        data["files"].append(data["files"][0])
        rejected(lambda: namespace["verify_manifest"](data))
        data = namespace["snapshot"]()
        data["files"].pop()
        rejected(lambda: namespace["verify_manifest"](data))
        data = namespace["snapshot"]()
        data["status"] = "RELEASED"
        rejected(lambda: namespace["verify_manifest"](data))
    print("PASS: unsafe paths, generated exclusions, retained history, two-source closure, valid custody, altered hash, duplicate/missing member, release-label rejection")
    print("No mathematical tests, proof replay, Lean/PDF build, or publication gate executed.")


if __name__ == "__main__":
    main()
