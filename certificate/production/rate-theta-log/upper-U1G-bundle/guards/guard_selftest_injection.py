#!/usr/bin/env python3
"""U1G injection self-test: proves the hygiene guard is fail-capable.

Copies the live bundle surface to a temp tree, applies each mutation
from the round-3 auditors' own injection sets, runs the copied hygiene
guard, and asserts NONZERO exit for every mutation (and ZERO exit for
the unmutated copy). Shipped IN the bundle per round-3 integrity
blocker 1 ("implement the adopted rule, and ship the injection test").

Mutations:
  I0  no mutation                                  -> must PASS
  I1  killed literal + identity assertion injected into EACH authored
      live file (one run per file)                 -> must FAIL each
  I2  delete authority/PROMOTED_LOWER_RATE_RECEIPT.md (the file the
      round-3 auditor deleted undetected)          -> must FAIL
  I3  laundering block (retraction markers around a live THEOREM
      assertion) injected into the ledger          -> must FAIL
  I4  any retraction block injected into the PROOF -> must FAIL
  I5  kill-route token injected into the graph     -> must FAIL
  I6  dangling dependencies/ pointer in the proof  -> must FAIL
  I7  one hex digit of a proof-quoted anchor hash flipped -> must FAIL
  I8  new unlisted authority/*.md file added       -> must FAIL

Writes nothing outside the system temp directory; prints stdout only.
"""

from __future__ import annotations
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
SURFACE = ["proof", "authority", "dependencies", "guards",
           "artifacts", "audit_archive", "audit_diff",
           "STATUS_U1E.json", "MANIFEST_U1E_SHA256.json",
           "README.md", "U1_TO_U1E_CHANGES.md"]


def make_copy(tmp: Path) -> Path:
    root = tmp / "U1G_selftest"
    root.mkdir()
    for item in SURFACE:
        src = HERE / item
        if src.is_dir():
            shutil.copytree(src, root / item)
        else:
            shutil.copy2(src, root / item)
    return root


def run_guard(root: Path) -> int:
    r = subprocess.run(
        [sys.executable,
         str(root / "guards" / "guard_live_upper_authority_hygiene.py")],
        capture_output=True, text=True)
    return r.returncode


def run_strictness(root: Path) -> int:
    r = subprocess.run(
        [sys.executable,
         str(root / "guards" / "guard_a8_strictness.py")],
        capture_output=True, text=True)
    return r.returncode


def expect(name: str, rc: int, want_fail: bool):
    ok = (rc != 0) if want_fail else (rc == 0)
    verdict = "fired" if rc != 0 else "passed"
    if not ok:
        print(f"SELFTEST FAIL: {name} — guard {verdict}, expected "
              f"{'FAIL' if want_fail else 'PASS'}")
        sys.exit(1)
    print(f"PASS selftest {name}: guard {verdict} as expected")


def mutate(root: Path, path: str, inject: str):
    f = root / path
    f.write_text(f.read_text(encoding="utf-8") + "\n" + inject + "\n",
                 encoding="utf-8")


def rehash_manifest(root: Path):
    """Recompute the temp tree's manifest after a mutation, so each
    injection tests its SPECIFIC content tripwire rather than the
    blanket H8 hash mismatch (which is separately tested by I9b)."""
    import hashlib, json
    entries = {}
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.name == "MANIFEST_U1E_SHA256.json":
            continue
        if p.suffix == ".pyc" and "__pycache__" in p.parts:
            continue
        entries[p.relative_to(root).as_posix()] = hashlib.sha256(
            p.read_bytes()).hexdigest()
    man_path = root / "MANIFEST_U1E_SHA256.json"
    man = json.loads(man_path.read_text(encoding="utf-8"))
    man["sha256"] = entries
    man["file_count"] = len(entries)
    man_path.write_text(json.dumps(man, indent=1), encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)

        base = make_copy(tmp)
        expect("I0 unmutated copy", run_guard(base), want_fail=False)
        shutil.rmtree(base)

        authored = ["proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
                    "authority/00_AUTHORITY_BANNER_U1E.md",
                    "authority/PROMOTED_LOWER_RATE_RECEIPT.md",
                    "authority/U1E_CORRECTION_LEDGER.md",
                    "authority/U1E_DEPENDENCY_GRAPH.md",
                    "STATUS_U1E.json"]
        for i, rel in enumerate(authored):
            root = make_copy(tmp)
            mutate(root, rel,
                   "The coefficient 13.299 is asserted; "
                   "g(1)g(-1)=0 holds.")
            rehash_manifest(root)
            expect(f"I1.{i} killed literal in {Path(rel).name}",
                   run_guard(root), want_fail=True)
            shutil.rmtree(root)

        root = make_copy(tmp)
        (root / "authority" / "PROMOTED_LOWER_RATE_RECEIPT.md").unlink()
        rehash_manifest(root)
        expect("I2 banner-listed file deleted", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        mutate(root, "authority/U1E_CORRECTION_LEDGER.md",
               "RETRACTION-BLOCK-BEGIN THEOREM: the coefficient is "
               "exactly 13.299 and this is a live assertion. "
               "RETRACTION-BLOCK-END")
        rehash_manifest(root)
        expect("I3 laundering block in ledger", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "RETRACTION-BLOCK-BEGIN historical note, retracted. "
               "RETRACTION-BLOCK-END")
        rehash_manifest(root)
        expect("I4 any block in the proof", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        mutate(root, "authority/U1E_DEPENDENCY_GRAPH.md",
               "The value F(q) at the endpoint is consumed here.")
        rehash_manifest(root)
        expect("I5 kill-route token in graph", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "See dependencies/NONEXISTENT_RECEIPT.md for details.")
        rehash_manifest(root)
        expect("I6 dangling pointer in proof", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        pf = root / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
        text = pf.read_text(encoding="utf-8")
        target = "090aecebe7d5c150"
        assert target in text, "selftest setup: anchor hash not found"
        pf.write_text(text.replace(target, "090aecebe7d5c151", 1),
                      encoding="utf-8")
        rehash_manifest(root)
        expect("I7 anchor hash digit flipped", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        root = make_copy(tmp)
        (root / "authority" / "UNLISTED_NEW_AUTHORITY.md").write_text(
            "A new authority file the banner does not list.\n",
            encoding="utf-8")
        expect("I8 unlisted authority file added", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        # ---- Round-4 additions (integrity findings 1-4) ----

        # I9: the round-4 auditor's J1 — tamper a dependency copy AND
        # re-pin every internal digest (proof quote + manifest entry).
        # Only the EXTERNAL byte-identity check H7 can catch this.
        root = make_copy(tmp)
        dep = root / "dependencies" / "ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md"
        import hashlib as _hl
        old_digest = _hl.sha256(dep.read_bytes()).hexdigest()
        mutate(root, "dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md",
               "## 14. Addendum — The outward multiplier equals "
               "0.8616013 and this bound is asserted as live.")
        new_digest = _hl.sha256(dep.read_bytes()).hexdigest()
        pf = root / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
        pf.write_text(pf.read_text(encoding="utf-8").replace(
            old_digest, new_digest), encoding="utf-8")
        rehash_manifest(root)
        expect("I9 copy tampered with full internal re-pin (J1)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I9b: same tamper WITHOUT any re-pin — H8 manifest catches it.
        root = make_copy(tmp)
        mutate(root, "dependencies/ENDPOINT_CESARO_CARRIER_RATE_THEOREM.md",
               "## 14. Addendum.")
        expect("I9b copy tampered, no re-pin (manifest tripwire)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I10: the round-4 auditor's J2 — laundering block with
        # 'Historical' + 'Lemma' phrasing that evades the old regex;
        # the RB registry count now catches it.
        root = make_copy(tmp)
        mutate(root, "authority/U1E_CORRECTION_LEDGER.md",
               "RETRACTION-BLOCK-BEGIN Historical note. Lemma 4 "
               "(established, and relied upon below): the endpoint "
               "coefficient is exactly 13.299 and the endpoint product "
               "g(1)g(-1)=0 holds; the U1G bound is derived from this "
               "value. RETRACTION-BLOCK-END")
        rehash_manifest(root)
        expect("I10 registry-evading laundering block (J2)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I11: the round-4 auditor's J10 — a block inside a dependency
        # copy (zero blocks allowed in copies).
        root = make_copy(tmp)
        mutate(root, "dependencies/08_ENDPOINT_RECEIPT_PROVENANCE.md",
               "RETRACTION-BLOCK-BEGIN historical: 13.299 asserted; "
               "g(1)g(-1)=0 holds. RETRACTION-BLOCK-END")
        # note: this also breaks H7 byte-identity; both tripwires valid.
        rehash_manifest(root)
        expect("I11 block in dependency copy (J10)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I12: the round-4 auditor's J3 — non-.md file in authority/
        # carrying killed tokens (escapes the .md glob; H8 partition
        # catches it).
        root = make_copy(tmp)
        (root / "authority" / "EXTRA_AUTHORITY.txt").write_text(
            "13.299 and g(1)g(-1)=0 and F(q) and q_ret\n",
            encoding="utf-8")
        rehash_manifest(root)
        expect("I12 non-md scope escape in authority/ (J3)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I13: the round-4 auditor's J4 — a new live-looking directory
        # outside every scanned location (H8 partition catches it).
        root = make_copy(tmp)
        (root / "supplement").mkdir()
        (root / "supplement" / "EXTRA_LIVE_LEMMA.md").write_text(
            "The coefficient 13.299 is asserted as live.\n",
            encoding="utf-8")
        rehash_manifest(root)
        expect("I13 unscanned-directory scope escape (J4)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # ---- Round-4 PROOF-surface additions (findings F-02, F-06) --

        # I14: the round-4 proof auditor's S-I4 — weaken the proof's
        # displayed K to the short surrogate whose reciprocal
        # overshoots the bound; the strictness guard's G5 CHAIN check
        # must fire (it verifies the chain the proof displays).
        root = make_copy(tmp)
        pf = root / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
        text = pf.read_text(encoding="utf-8")
        assert "K_0 := 0.08367827985" in text, "selftest setup: K_0 not found"
        pf.write_text(text.replace("K_0 := 0.08367827985",
                                   "K_0 := 0.0836782", 1),
                      encoding="utf-8")
        expect("I14 proof K_0 weakened to unsafe surrogate (S-I4)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I14b: baseline — unmutated strictness guard must PASS in the
        # temp tree.
        root = make_copy(tmp)
        expect("I14b strictness guard baseline", run_strictness(root),
               want_fail=False)
        shutil.rmtree(root)

        # I15: the round-4 proof auditor's H-I2/H-I5 class — an
        # unfencing phrase added to the proof; H9 must fire.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "This bound is unconditional.")
        rehash_manifest(root)
        expect("I15 unfencing phrase in proof (H-I2/H-I5)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # ---- Round-5 additions (integrity findings 1-9, proof AI set) --

        # I16 (round-5 N1c): lockstep tamper of a dependency copy AND
        # its external sealed source, with proof digest and manifest
        # re-pinned. Only the pinned digest registry (H7) catches it.
        # We mirror the external sources into temp and repoint the
        # copied guard, so the REAL sealed bundles are never touched.
        root = make_copy(tmp)
        ext = tmp / "ext_mirror"
        (ext / "dependencies").mkdir(parents=True)
        (ext / "upper_artifacts").mkdir()
        (ext / "new_docs").mkdir()
        gpath = root / "guards" / "guard_live_upper_authority_hygiene.py"
        gtext = gpath.read_text(encoding="utf-8")
        v281 = ("C:\\Infanox\\finite-contact"
                "\\I3322_V28_1_LOWER_BOUND_FINAL_FIXES_BUNDLE_2026-08-06")
        cons = ("C:\\Infanox\\finite-contact"
                "\\i3322_consolidated_promotion_bundle")
        for sub_dir in ("dependencies", "upper_artifacts"):
            src_dir = Path(v281) / sub_dir
            for f in src_dir.glob("*.md"):
                shutil.copy2(f, ext / sub_dir / f.name)
        shutil.copy2(Path(cons) / "new_docs" /
                     "08_ENDPOINT_RECEIPT_PROVENANCE.md",
                     ext / "new_docs")
        gtext2 = gtext.replace(
            'r"C:\\Infanox\\finite-contact"\n             '
            'r"\\I3322_V28_1_LOWER_BOUND_FINAL_FIXES_BUNDLE_2026-08-06"',
            repr(str(ext))).replace(
            'r"C:\\Infanox\\finite-contact"\n             '
            'r"\\i3322_consolidated_promotion_bundle"', repr(str(ext)))
        assert gtext2 != gtext, "selftest setup: path repoint failed"
        gpath.write_text(gtext2, encoding="utf-8")
        rehash_manifest(root)
        expect("I16a external-mirror control (repoint only)",
               run_guard(root), want_fail=False)
        # now the lockstep tamper + full internal re-pin
        import hashlib as _h2
        dep2 = root / "dependencies" / "08_ENDPOINT_RECEIPT_PROVENANCE.md"
        old_d = _h2.sha256(dep2.read_bytes()).hexdigest()
        payload = "\n## Addendum: the coefficient is asserted live.\n"
        for tgt in (dep2, ext / "new_docs" /
                    "08_ENDPOINT_RECEIPT_PROVENANCE.md"):
            tgt.write_text(tgt.read_text(encoding="utf-8") + payload,
                           encoding="utf-8")
        new_d = _h2.sha256(dep2.read_bytes()).hexdigest()
        pf2 = root / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
        pf2.write_text(pf2.read_text(encoding="utf-8").replace(
            old_d, new_d), encoding="utf-8")
        rehash_manifest(root)
        expect("I16 lockstep copy+source tamper, full re-pin (N1c)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)
        shutil.rmtree(ext)

        # I17 (round-5 N3): edit the INTERIOR of an existing registered
        # ledger block (count unchanged) — content digest must fire.
        root = make_copy(tmp)
        lf = root / "authority" / "U1E_CORRECTION_LEDGER.md"
        ltext = lf.read_text(encoding="utf-8")
        import re as _re
        mblk = _re.search(r"RETRACTION-BLOCK-BEGIN(.*?)RETRACTION-BLOCK-END",
                          ltext, _re.S)
        assert mblk, "selftest setup: no ledger block found"
        laundered = (" Historical note. Lemma 4 (established above and "
                     "relied upon by the live section 3): the endpoint "
                     "coefficient is exactly 13.299 and the endpoint "
                     "product g(1)g(-1)=0 holds. ")
        lf.write_text(ltext.replace(mblk.group(1), laundered, 1),
                      encoding="utf-8")
        rehash_manifest(root)
        expect("I17 interior edit of registered block (N3)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I18 (round-5 N7 = round-4 J5): remove the graph from the
        # banner's AUTHORED list AND relocate the file to artifacts/ —
        # the pinned filename allowlist must fire.
        root = make_copy(tmp)
        bf = root / "authority" / "00_AUTHORITY_BANNER_U1E.md"
        btext = bf.read_text(encoding="utf-8")
        assert "- authority/U1E_DEPENDENCY_GRAPH.md\n" in btext
        bf.write_text(btext.replace(
            "- authority/U1E_DEPENDENCY_GRAPH.md\n", "", 1),
            encoding="utf-8")
        shutil.move(str(root / "authority" / "U1E_DEPENDENCY_GRAPH.md"),
                    str(root / "artifacts" / "U1E_DEPENDENCY_GRAPH.md"))
        rehash_manifest(root)
        expect("I18 banner-delete + relocate to artifacts/ (N7/J5)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I19 (round-5 N2): new poisoned file under artifacts/ — the
        # allowlist must fire even though the prefix is 'historical'.
        root = make_copy(tmp)
        (root / "artifacts" / "EXTRA_LIVE_LEMMA.md").write_text(
            "The coefficient 13.299 is asserted as live; F(q) holds.\n",
            encoding="utf-8")
        rehash_manifest(root)
        expect("I19 new file under artifacts/ (N2)", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        # I20 (round-5 N8): a non-.pyc file smuggled into __pycache__ —
        # the narrowed exclusion must see it.
        root = make_copy(tmp)
        pyc = root / "guards" / "__pycache__"
        pyc.mkdir(exist_ok=True)
        (pyc / "EXTRA_LIVE_LEMMA.md").write_text(
            "The coefficient 13.299 is asserted as live.\n",
            encoding="utf-8")
        rehash_manifest(root)
        expect("I20 non-pyc file inside __pycache__ (N8)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I21 (round-5 N4): a RESTATED unsafe surrogate appended after
        # the safe one — G5's every-occurrence scan must fire.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Restatement: with kappa_pm >= K_0 := 0.0836782 we "
               "obtain 1/kappa_eff <= 23.9010650.")
        expect("I21 restated unsafe surrogate (N4)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I22 (round-5 N5): unfencing phrases in a NON-proof authored
        # file — bundle-wide H9 must fire.
        root = make_copy(tmp)
        mutate(root, "authority/PROMOTED_LOWER_RATE_RECEIPT.md",
               "The Theta(log) rate established here is unconditional "
               "and does not depend on this gate.")
        rehash_manifest(root)
        expect("I22 unfencing phrase in lower receipt (N5)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

        # I23 (round-5 proof AI-4): a FALSE tighter display added
        # beside the true one — the structural range check must fire.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Moreover 1/kappa_eff <= 23.9010000 and "
               "y^2 <= 0.9197270.")
        expect("I23 false tighter display (AI-4)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I24 (round-5 proof AI-6b): repoint the proof's Lean commit id
        # — H5 parses the commit from the proof, so the bogus commit
        # must fail cat-file.
        root = make_copy(tmp)
        pf3 = root / "proof" / "CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md"
        t3 = pf3.read_text(encoding="utf-8")
        assert "public commit 6e6adb5" in t3
        pf3.write_text(t3.replace("public commit 6e6adb5",
                                  "public commit 9999999", 1),
                       encoding="utf-8")
        rehash_manifest(root)
        expect("I24 Lean commit repointed (AI-6b)", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        # ---- Round-6 additions (integrity V/E sets, blockers 1-6) ----

        # I25 (round-6 V1): the round-5 N4 text VERBATIM with the
        # pre-rename identifier "K :=" — the widened regex must catch
        # it (round-6 finding 1: an identifier rename must never
        # narrow a tripwire).
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Restatement (3.12): with kappa_pm >= K := 0.0836782 "
               "we obtain 1/kappa_eff <= 2/K <= 23.9010650.")
        expect("I25 pre-rename identifier restatement (V1)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I26 (round-6 V2): false display under STRICT '<'.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Note that 1/kappa_eff < 23.9010000 here.")
        expect("I26 false display via strict < (V2)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I27 (round-6 V3): false display under Unicode comparison.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Note that 1/kappa_eff ≤ 23.9010000 here.")
        expect("I27 false display via Unicode le-symbol (V3)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I28 (round-6 V4): false mu_min lower display — the newly
        # wired range branch must fire.
        root = make_copy(tmp)
        mutate(root, "proof/CONSTRUCTIVE_LOG_UPPER_BOUND_U1G.md",
               "Consequently mu >= 2.0017508 throughout.")
        expect("I28 false mu_min lower display (V4)",
               run_strictness(root), want_fail=True)
        shutil.rmtree(root)

        # I29 (round-6 E1): killed literal appended to README.md — the
        # extended token scan H9x must fire.
        root = make_copy(tmp)
        mutate(root, "README.md",
               "The coefficient 13.299 is asserted; this bound is "
               "unconditional.")
        rehash_manifest(root)
        expect("I29 poisoned README (E1/N2c)", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        # I30 (round-6 E3): rewrite an archived early-round verdict
        # (evidence tampering) with the manifest re-pinned — the H10
        # custody cmp against the blind-batch original must fire.
        root = make_copy(tmp)
        av = (root / "audit_archive" /
              "VERDICT-U1E-AUDITOR-2-INTEGRITY.md")
        av.write_text(av.read_text(encoding="utf-8").replace(
            "DENIED", "PROMOTE"), encoding="utf-8")
        rehash_manifest(root)
        expect("I30 archived verdict rewritten (E3)", run_guard(root),
               want_fail=True)
        shutil.rmtree(root)

        # I31 (round-6 E4): a .pyc OUTSIDE __pycache__ carrying live
        # content — the scoped exclusion must now see it.
        root = make_copy(tmp)
        (root / "authority" / "LIVE_CLAIM.pyc").write_text(
            "The coefficient 13.299 is asserted as live.\n",
            encoding="utf-8")
        rehash_manifest(root)
        expect("I31 stray .pyc outside __pycache__ (E4)",
               run_guard(root), want_fail=True)
        shutil.rmtree(root)

    print("U1G INJECTION SELF-TEST: ALL PASS (guard is fail-capable on "
          "the round-3, round-4, round-5 AND round-6 injection sets)")


if __name__ == "__main__":
    main()
