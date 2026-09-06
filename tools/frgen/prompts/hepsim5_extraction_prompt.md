HEPSIM5 extraction prompt (text-only hardening)

Scope:
- Apply this checklist to Ian model 1, Ian model 2, Ian model 3, Ian model 4, and the EffLRSM Eq.8 sqrt case.
- Work from the paper equations and definitions, then write the extracted terms in FeynRules-ready form.

Checklist (one line per item):
1. Overall normalisation: state whether each Sqrt or root factor is in the numerator or denominator, and quote the paper equation number.
2. Field completeness: every new vector or scalar field must include a kinetic term and a mass term.
3. Dimension counting: every operator with mass dimension above 4 must carry the matching 1/Lambda^n prefactor.
4. Majorana or light-neutrino mass terms: use charge conjugation for each such mass term.
5. SU(2) and U(1) conventions: state epsilon versus dagger structure for SU(2) doublet contractions, and keep U(1) charge signs consistent with the covariant-derivative convention.

Required output note:
- For each checklist item, provide a short pass or fail statement and cite the exact equation or definition used.
