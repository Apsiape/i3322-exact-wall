#!/usr/bin/env python3
"""Enforce v28.1 live authority, symbol typing, and killed-item absence."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
new=root/'new_docs'
required=[
 '00_AUTHORITY_BANNER_V28.md',
 '01_RAW_CELL_PARITY_EDGE_BUDGET_V28.md',
 '02_CELL_RESPONSE_AND_BRIDGE_RECURRENCE_V28.md',
 '03_REPEATED_CELL_CYCLE_EXACTIFICATION_V28.md',
 '04_STATE_CARRYING_COMMON_RETURN_AND_NEUTRAL_GAIN_V28.md',
 '05_EXPONENTIAL_LOWER_ASSEMBLY_V28.md',
 '06_P4_RECEIPTS_AND_SYMBOL_HYGIENE_V28.md',
 '07_CORRECTION_AND_SUPERSESSION_LEDGER_V28.md',
 '08_P5_ARTIFACT_CLOSEOUT_V28.md',
 '09_TERMINAL_EVENT_TABLE_V28.md',
 '10_LOWER_BOUND_PROMOTION_AUDIT_COMMISSION_V28.md',
]
for n in required: assert (new/n).is_file(),n
proof='\n'.join((new/n).read_text(encoding='utf-8') for n in required[1:7])
symbols=(new/'06_P4_RECEIPTS_AND_SYMBOL_HYGIENE_V28.md').read_text(encoding='utf-8')
doc4=(new/'04_STATE_CARRYING_COMMON_RETURN_AND_NEUTRAL_GAIN_V28.md').read_text(encoding='utf-8')
ledger=(new/'07_CORRECTION_AND_SUPERSESSION_LEDGER_V28.md').read_text(encoding='utf-8')
index=(root/'DEPENDENCY_RECEIPT_INDEX.md').read_text(encoding='utf-8')
r1=(root/'dependencies/PROJECTED_RETURN_MISMATCH_R1_V23.md').read_text(encoding='utf-8')
upper=(root/'upper_artifacts/UPPER_SCOPE_NOTE.md').read_text(encoding='utf-8')
rho=(root/'upper_artifacts/RHO_Q_IDENTIFICATION.md').read_text(encoding='utf-8')

# Required live typing.
for token in ['b_{\\rm amp}', '\\iota(t)=-t', 'K_A=Wb_{\\rm amp}(X)^{-1}', 'K_B=W_Bb_{\\rm amp}(U)^{-1}',
              'r_A^{\\rm step}', 'r_B^{\\rm step}', 'r_A^{\\rm ret}', 'r_B^{\\rm ret}',
              'r_{A,{\\rm mult}}', 'r_{B,{\\rm mult}}']:
    assert token in symbols,token
assert 'K_A:=W\\,b_{\\rm amp}(X)^{-1}' in doc4
assert 'normalized gains' in doc4.lower() and 'raw gains' in doc4.lower()
assert 'Q=S' in doc4.replace(' ','')
assert 'R2 (formerly G2) remains OPEN and is not on the v28 critical path' in doc4

# Bare r_A/r_B are forbidden in live Docs 01--06: every literal r_A occurrence
# must be immediately typed with ^; r_{A,...} is a different string.
for base in ('r_A','r_B'):
    pos=0
    while True:
        i=proof.find(base,pos)
        if i<0: break
        nxt=proof[i+len(base):i+len(base)+1]
        assert nxt=='^', (base,proof[i:i+40])
        pos=i+len(base)

# Killed or superseded content must not re-enter the live proof chain.
for bad in ['1/2000','13.2991468418','P(-t_k)','P(-u_k)','P(-u_j)','P(-t_j)',
            'sum component rank costs <= d','C034/current-S atlas']:
    assert bad not in proof,bad

# Ledger restorations and predecessor diff.
assert 'Diff against v27' in ledger
assert 'partial/a.e.-\\(\\tau\\)' in ledger or 'partial/a.e.-\\(\\tau\\)' in ledger.replace(' ','')
assert '1/2000' in ledger

# R1/index reconciliation and symbol hygiene.
assert 'r_A^{\\rm ret}' in r1 and 'r_B^{\\rm ret}' in r1
assert 'r_{A,{\\rm mult}}' in r1 and 'r_{B,{\\rm mult}}' in r1
assert 'R1-only optional provenance' in r1
assert 'R1-only optional dependencies' in index and 'TOP_D_SIMULTANEOUS_MONOTONE_CLUSTERING_V23.md' in index

# Upper scope and endpoint-symbol collision.
assert 'Commission v28-L' in upper and '\\Theta(\\log' in upper
assert '\\alpha_{\\rm end}' in rho and 'a_{+,\\rm end}' in rho
assert 'q_{\\rm ret,+}' in rho

print('PASS v28.1 live-authority hygiene')
print('  symbol families typed; killed items absent from live proof; R1/TOP_D/upper scope reconciled')
