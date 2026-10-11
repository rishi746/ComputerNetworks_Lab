
# Q3: Find the Communication Range Using ProtocolChannelModel

## 1. Run the Simulation

Save the script as `q3.groovy`.

Run:

```bash
unet q3.groovy
```

Open the web shells:

- Node 1: http://localhost:8081
- Node 2: http://localhost:8082
- Node 3: http://localhost:8083

## 2. Initial Node Positions

| Node | Address | Location |
|---|---|---|
| N1 | 1 | [0, 0, -15] |
| N2 | 2 | [1200, 0, -15] |
| N3 | 3 | [2400, 0, -15] |

Channel settings:

- Communication Range: 1500 m
- Detection Range: 2000 m
- Interference Range: 2500 m

## 3. Test Connectivity

### Test 1: Node 1 to Node 2

Open node 1's shell:

```groovy
ping 2
```

Expected: Success (1200 m).

### Test 2: Node 2 to Node 3

Open node 2's shell:

```groovy
ping 3
```

Expected: Success (1200 m).

### Test 3: Node 1 to Node 3

Open node 1's shell:

```groovy
ping 3
```

Expected direct-link result: Unreachable (2400 m).

Take screenshots of all three ping outputs.

## 4. Move Node 3

Stop the simulation.

Change node 3's location from:

```groovy
location: [2400.m, 0.m, -15.m]
```

to:

```groovy
location: [1800.m, 0.m, -15.m]
```

Restart the simulation.

From node 1's shell, run:

```groovy
ping 3
```

Expected direct-link result: Unreachable (1800 m).

Take a screenshot.

## 5. Connectivity Table

| Node 3 Position | Pair | Distance (m) | Directly Reachable |
|---|---|---|---|
| 2400 m | 1–2 | 1200 | Yes |
| 2400 m | 2–3 | 1200 | Yes |
| 2400 m | 1–3 | 2400 | No |
| 1800 m | 1–2 | 1200 | Yes |
| 1800 m | 2–3 | 600 | Yes |
| 1800 m | 1–3 | 1800 | No |

Note: Ping results may differ from direct-link reachability if multi-hop routing is enabled.

## 6. Explanation

The ProtocolChannelModel allows direct communication between nodes within the configured communication range of 1500 m.

Initially, nodes 1–2 and 2–3 are within range, while nodes 1–3 are 2400 m apart and cannot communicate directly.

After moving node 3 to 1800 m, nodes 1 and 3 remain outside the direct communication range.

## 7. Submission Checklist

- [ ] Groovy simulation script.
- [ ] Ping screenshot for nodes 1–2.
- [ ] Ping screenshot for nodes 2–3.
- [ ] Ping screenshot for nodes 1–3 at 2400 m.
- [ ] Ping screenshot for nodes 1–3 at 1800 m.
- [ ] Connectivity table with observed results.
