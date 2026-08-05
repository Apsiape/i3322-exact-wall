#!/usr/bin/env python3
"""Fail-closed W1-W10 integrity check for package v5."""
from pathlib import Path
import json, re
BASE=Path(__file__).resolve().parents[1]

def read(name): return (BASE/name).read_text(encoding='utf-8')
readme=read('README.md')
signed=read('THEOREM_N_SIGNED_PUBLIC_STATEMENT.md')
assembly=read('FOUR_RECEIPTS_AT_S_ASSEMBLY.md')
completion=read('CONVEX_ENVELOPE_PLATEAU_EXCLUSION_AND_THEOREM_N_COMPLETION.md')
zero=read('CRITICAL_ZERO_SET_REDUCTION_FOR_THEOREM_N.md')
ledger=read('W1_W10_EXECUTION_LEDGER.md')
artread=read('artifacts/README.md')

# W1
assert 'D:=(-1,1)' in completion or 'D=(-1,1)' in completion
assert 'C(x)\\ge g(0)>0' in completion
assert 'endpoint-excluded compact source interval' not in completion.lower().replace('replaces the v4 phrase\n“endpoint-excluded compact source interval”','')
# W2/W3/W4/W5
assert 'affine function `y -> uy+m`' in completion
assert 'max(H,\\ell+\\epsilon)' in completion
assert 'Longrightarrow' in completion and 'The converse is not asserted' in completion
assert "C'_-(x_0)=H'_-(x_0)=H'_+(x_0)=C'_+(x_0)" in completion
# W6
assert 'explicit spectral cutoff' in assembly.lower()
assert 'Pi R_{\\nu,n}\\Pi' in assembly
# W7
for token in ['classical bound `0`','qubit and qutrit','C_q(3,3;2,2)','not closed']:
    assert token in signed
assert 'historical Pál–Vértesi decimal' in signed
assert 'C_qs \\\\ C_q' in signed and 'not promoted' in signed
# W8
for obsolete in ['FOUR_RECEIPTS_AT_S_ASSEMBLY_V2.md','receipt_ii_certificate_schema.json','validate_receipt_ii_certificate.py']:
    assert not (BASE/obsolete).exists()
    assert not (BASE/'artifacts'/obsolete).exists()
# W9
assert 'guards, not theorem verifiers' in artread
assert 'do **not** verify' in artread
# W10
assert 'dimension-255' in assembly and 'Q_127' not in assembly
# Status consistency
assert '**PROMOTED.**' in readme
status=json.loads(read('artifacts/theorem_N_promoted_status.json'))
assert status['status']=='PROMOTED'
assert status['theorem']['Cq_nonclosed'] is True
# Every finding executed
for i in range(1,11): assert f'**W{i}**' in ledger and '**EXECUTED**' in ledger
# Operative docs may not claim pending promotion or Receipt ii open.
operative=[readme,signed,assembly,completion,zero,ledger]
for text in operative:
    assert 'NOT YET PROMOTED' not in text
    assert 'PENDING_BLIND' not in text
print('PASS: W1-W10 package controls and status consistency')
