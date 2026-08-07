#!/usr/bin/env python3
"""Replay the original exact rational endpoint certificate and check registered floors."""
from pathlib import Path
from fractions import Fraction
import subprocess, json, sys
root=Path(__file__).resolve().parent
p=subprocess.run([sys.executable, str(root/'exact_rational_endpoint_line_certificate.py')],check=True,capture_output=True,text=True)
data=json.loads(p.stdout)
mp=Fraction(data['margin_plus_exact']); mm=Fraction(data['margin_minus_exact'])
assert data['all_exact_pivots_positive'] is True
assert mp > Fraction(4039,100000)
assert mm > Fraction(9893,50000)
assert data['grid_points']==2001 and data['history_depth']==100
print('PASS endpoint exact-rational replay')
print('  margin_plus_decimal=', data['margin_plus_decimal'])
print('  margin_minus_decimal=', data['margin_minus_decimal'])
