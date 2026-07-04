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

