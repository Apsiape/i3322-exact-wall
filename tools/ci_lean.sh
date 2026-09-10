#!/usr/bin/env bash
# Hosted Linux only; caller must supply a bounded systemd memory cgroup.
set -euo pipefail
: "${I3322_AXIOM_LOG:?axiom-log destination required}"
test -r /sys/fs/cgroup/cgroup.controllers
cgroup_path="$(awk -F: '$1 == "0" { print $3 }' /proc/self/cgroup)"
test -n "$cgroup_path"
test "$(cat "/sys/fs/cgroup${cgroup_path}/memory.max")" = 1610612736
test "$(cat "/sys/fs/cgroup${cgroup_path}/memory.swap.max")" = 0
printf '%s\n' 'Verified process-group cap: 1536 MiB charged memory, zero swap; 35-minute service deadline.'
timeout 600s lake exe cache get Mathlib.Tactic Mathlib.Analysis.SpecialFunctions.Sqrt
for module in QuarterCeiling EndpointMargins FiniteClosure RateCores WeightedFlow; do
  timeout 600s lake --no-cache build "I3322Kernel.$module"
done
timeout 600s lake --no-cache build
timeout 600s lake env lean AxiomCheck.lean > "$I3322_AXIOM_LOG"
