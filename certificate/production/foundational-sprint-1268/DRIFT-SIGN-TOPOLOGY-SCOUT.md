# The Bellman drift appears to have four intrinsic sign chambers

Status: **two-resolution numerical scout; interval certification remains
open**

The standalone scout reconstructs the Bellman profile from the displayed
min-plus equation, with no imported profile file, at 1601 and 3201 nodes.  It
then continuously refines the predecessor policy and evaluates

```text
chi(u)=2 log beta(u)-2 log alpha(u).                 (1)
```

Both retained resolutions find exactly three sign changes on the certified active
box.  The fine-grid roots are approximately

```text
-0.8662,  -0.3770,  0.8000.                         (2)
```

At those roots the reconstructed horizontal defect `|a(u)+u|` is respectively
about

```text
0.385,  1.146,  0.076.                              (3)
```

Thus the numerical target registered in `PRE-REGISTRATION.md` survives at two
independently rebuilt discretizations.  The smallest observed separation is
comfortably above the registered `1/20` threshold.

If this topology is interval-certified, it changes the proof architecture.
The fine shifted grid of Sprints 1264--1267 can be replaced by four intrinsic
drift chambers.  Near the three boundaries, horizontal coalescence is
forbidden by (3); inside a chamber, the vertical orientation is fixed.  The
number of required response prefixes would then be an absolute constant,
not a function of Schmidt rank.

An initial 801/1601 comparison missed an unregistered `5e-4` agreement guard
by `1.2e-4`; the threshold was held fixed and both resolutions were doubled.
The retained 1601/3201 comparison passes.  This document does **not** assert
the zero count as a theorem.  PCHIP policy
reconstruction can miss a narrow root or misplace a Bellman corner.  The next
gate is the registered full-domain interval exclusion plus simple-root proof.
