import I3322Kernel

-- Axiom hygiene: every theorem must report only the standard axioms
-- (propext, Classical.choice, Quot.sound). Run:
--   lake env lean AxiomCheck.lean

#print axioms I3322Kernel.discriminant_identity
#print axioms I3322Kernel.amplitude_expansion
#print axioms I3322Kernel.sqrt_prod_le
#print axioms I3322Kernel.amplitude_le
#print axioms I3322Kernel.scalar_quarter_ceiling
#print axioms I3322Kernel.quarter_ceiling
#print axioms I3322Kernel.quarter_lt_window_lower
#print axioms I3322Kernel.mPlus_eq
#print axioms I3322Kernel.mMinus_eq
#print axioms I3322Kernel.mPlus_pos
#print axioms I3322Kernel.mMinus_pos
#print axioms I3322Kernel.mPlus_gt
#print axioms I3322Kernel.mMinus_gt
#print axioms I3322Kernel.window_sub_mPlus_lt_third
#print axioms I3322Kernel.window_sub_mMinus_lt_third
#print axioms I3322Kernel.mPlusAt_antitone
#print axioms I3322Kernel.mMinusAt_antitone
#print axioms I3322Kernel.strictMono_self_eq_id
#print axioms I3322Kernel.decreasing_bijections_coincide
