# Nyx

Nyx is a local-first hackathon demo for keeping orientation when GPS, comms,
cloud access, and confidence disappear.

It is not a tactical command system. It does not identify people, threats,
weapons, hazards, or safe entry conditions. It demonstrates one interface
pattern:

```text
weak evidence -> conservative state -> short action card -> human decision
```

## Why It Exists

In indoor, underground, or otherwise signal-denied spaces, position is not
enough. The more useful question is often:

```text
Can the operator still trust the route, the last checkpoint, and the mission
intent?
```

Nyx answers with a small set of drill cards:

| State | Meaning | Bias |
|---|---|---|
| `RE-ORIENT` | The last reliable reference is stale or missing. | recover the checkpoint |
| `REALIGN` | The route and observed landmarks disagree. | compare two independent cues |
| `HOLD` | Evidence is too weak to upgrade confidence. | avoid over-claiming |
| `HANDOFF` | The scene needs another asset or teammate. | mark, log, and transfer |

## Why This Problem Matters

Subterranean and signal-denied environments are not edge cases. They are a
recurring pattern across old and current conflicts: the map is incomplete, the
operator is under pressure, and the most dangerous mistake is turning weak
evidence into a confident action.

| Pattern | What It Shows | Nyx Translation |
|---|---|---|
| Vietnam War tunnel systems | Tunnel complexes made above-ground awareness unreliable and forced small teams into dark, narrow, low-context spaces. | The interface should preserve orientation before it tries to be clever. |
| Korean Peninsula infiltration tunnels | North Korean tunnel activity made SubT a concrete Korean security problem, not an abstract future scenario. | The drill treats underground route confidence as a first-class state. |
| Ukraine trench and electronic-warfare battlefield | Modern trench lines, drones, jamming, and degraded links show how quickly GPS, comms, and remote confidence can fail. | Local cards should still help the operator hold, re-align, or hand off. |

The through-line is simple:

```text
When the environment denies signal, the system must not invent certainty.
```

Nyx focuses on the narrow moment before a bad commitment:

```text
last checkpoint stale
observed landmarks ambiguous
contact or route evidence weak
operator asks whether to continue
```

The correct demo behavior is restraint:

```text
RE-ORIENT. REALIGN. HOLD. HANDOFF.
```

## Repository Shape

```text
.
├── app.py
├── demo/
│   ├── index.html
│   └── sample_scenarios/
├── docs/
│   ├── claim_boundary.md
│   ├── demo_story.md
│   ├── judging_notes.md
│   └── problem.md
└── src/
    └── nyx_demo/
```

The demo is intentionally small. The public repo contains a presentation-grade
stub, not a production sensor stack or operational rule base.

## Run

```bash
python3 app.py
```

Open:

```text
http://localhost:8080
```

## What To Look For

1. The header says `Nyx`.
2. The left panel shows a signal-denied drill state.
3. The action card never over-confirms a route, person, hazard, or entry.
4. The output stays short enough to read under pressure.

## Boundary

Nyx is a hackathon demonstration of a conservative interface pattern. It is not
fielded equipment, military advice, targeting software, autonomous control, or
a safety-certified decision system.

## Public References

These links are included only to explain the problem class. Nyx does not
implement tactics from them.

- [Underground Warfare 101 - Modern War Institute, West Point](https://mwi.westpoint.edu/underground-warfare-101/)
- [Subterranean Operations: Israeli Defense Force Lessons from Gaza - U.S. Army](https://www.army.mil/article/288356/subterranean_operations_israeli_defense_force_lessons_from_gaza)
- [Củ Chi tunnels - Wikipedia](https://en.wikipedia.org/wiki/C%E1%BB%A7_Chi_tunnels)
- [Third Tunnel of Aggression - Wikipedia](https://en.wikipedia.org/wiki/Third_Tunnel_of_Aggression)
- [In Ukraine's trenches, the warfare is electronic - Le Monde](https://www.lemonde.fr/en/international/article/2024/05/24/in-ukraine-s-trenches-the-warfare-is-electronic_6672587_4.html)
