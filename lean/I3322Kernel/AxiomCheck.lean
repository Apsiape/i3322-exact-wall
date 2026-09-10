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
#print axioms I3322Kernel.staircase_sum_injOn
#print axioms I3322Kernel.staircase_card_le
#print axioms I3322Kernel.prod_le_two_pow_sum
#print axioms I3322Kernel.min_point_pseudocycle
#print axioms I3322Kernel.s_mul_one_sub_s_le_quarter
#print axioms I3322Kernel.band_identity
#print axioms I3322Kernel.band_quarter_ceiling
#print axioms I3322Kernel.amplitude_b_le_half

-- Replacement lower proof: selected finite accounting cores, not the
-- analytic/SCC-existence/quantum reduction chain.
#print axioms I3322Kernel.WeightedFlow.all_edges
#print axioms I3322Kernel.WeightedFlow.balance_identity
#print axioms I3322Kernel.WeightedFlow.signed_work_bound
#print axioms I3322Kernel.WeightedFlow.mass_le_residual
#print axioms I3322Kernel.WeightedFlow.low_internal
#print axioms I3322Kernel.WeightedFlow.high_internal
#print axioms I3322Kernel.WeightedFlow.entering_low
#print axioms I3322Kernel.WeightedFlow.assembly_alternative
#print axioms I3322Kernel.WeightedFlow.weighted_endpoint_payment
#print axioms I3322Kernel.WeightedFlow.upper_rounding_slack
