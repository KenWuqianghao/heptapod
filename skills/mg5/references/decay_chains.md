# Decay-chain syntax in MadGraph: when each form works

## Decision tree

```
Need a decay chain in MG5?
│
├── 1 level (e.g. h > b bbar)                        → just `generate p p > h, h > b bbar`
├── 2 levels, distinct particles (top + antitop)     → parens per top:
│                                                       `generate p p > t t~,
│                                                          (t > b w+, w+ > l+ vl),
│                                                          (t~ > b~ w-, w- > l- vl~)`
├── 2 levels, identical particles (h > zz, z > 4l)   → comma chain often OK,
│                                                       BUT verify LHE has full final state.
├── 3+ levels                                        → PREFER explicit n-body ME with NP=N
│                                                       (the comma chain often only unfolds 2 levels).
└── Need to factor production from decay,             → MadSpin (post-processing).
    or want easy reweighting,
    or n-body ME blows up combinatorially.
```

## What goes wrong with deep comma chains

For a 3-level cascade with identical intermediates like
```
ta- > mu- phid, phid > Ap Ap, Ap > mu+ mu-
```
MG5 reports "1 processes with 2 diagrams" but the LHE writes only the first two levels:
the two A's appear as `status=1` (final), and the muons that should come from them are missing.
The matrix element is computed correctly internally, but the LHE record is truncated.

This is a known shape of the issue — search the `mg5amcnlo` Launchpad for "decay chain truncated" or
"compute_widths cascade".

## Reliable workaround: explicit n-body ME with order constraint

Count the BSM vertices on the cascade you want. For our example:
- 1 LFV vertex (`tau-mu-phid`)
- 1 `phid-Ap-Ap` vertex
- 2 `Ap-mu-mu` vertices (kinetic mixing carries `NP=1` per vertex via `eps`)

Total: `NP = 4`.

Then write the full final state and constrain:
```
generate ta- > mu- mu- mu- mu+ mu+ NP=4
```

MG5 generates only diagrams with exactly 4 NP-tagged vertices — which uniquely picks out the cascade.
The LHE then contains the full chain (intermediates as `status=2`, all 5 muons as `status=1`).

## When parenthesized chains work

For a 2-level chain with two **distinct** decaying particles, parens isolate them:
```
generate p p > t t~,
  (t > w+ b, w+ > l+ vl),
  (t~ > w- b~, w- > l- vl~)
```

For two **identical** intermediates (e.g. h > z z, then each z > l+l-):
```
generate p p > h > z z, z > l+ l-
```
or
```
generate p p > h, (h > z z, z > l+ l-)
```
both should work in 4.6+. The relevant MG5 docs: <https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/FAQ-General-6>.

## When MadSpin is the right tool

MadSpin is a separate program that:
- Takes an LHE produced WITHOUT decay chain,
- Decays selected particles in-place,
- Preserves polarization information through the decay (within an approximation).

Use MadSpin when:
- The production is expensive but the decay is cheap, and you want to vary decay channels without re-generating production.
- Some decays are not in the model but you have an analytic shape.
- The matrix element with the explicit final state is too large (combinatorial blowup).

Drawback: MadSpin loses some spin correlations across the production-decay boundary.

Trigger from MG5 card:
```
import model X
generate p p > t t~
output run01
launch
shower=Pythia8
madspin=ON
done
```
The MadSpin card lets you specify `decay t > b w+, w+ > l+ vl` etc.

## Useful order constraints

| Syntax | Meaning |
|---|---|
| `NP=N`           | EXACTLY N NP-tagged vertices (use this) |
| `NP^2==N`        | Squared-amp order: cross-section ∝ coupling^2N |
| `NP<=N`          | At most N NP-tagged vertices |
| `QED=2`          | Exactly 2 QED-tagged vertices |
| `/ z h a`        | Forbid Z, H, photon as intermediate |
| `$$ z h`         | Allow but no s-channel propagation through these |
| `$ z h`          | Forbid s-channel through these |
| `$$$ z h`        | Forbid only the on-shell part |

Precedence: explicit `=` constraints > `<=` constraints. Combine with comma to chain.

## Useful diagnostic: inspect the diagram set

After `output`, MG5 writes the diagram set to PNG/EPS. To audit which topologies are kept:
```
SubProcesses/P*/diagrams.html        # browse
SubProcesses/P*/matrix.f             # actual amplitude
```
If the diagrams don't match your topology expectation, your order constraint is wrong.
