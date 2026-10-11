
# Q1: Build a 2-Node Network and Inspect Its Agents

## 1. Run the Simulation

Save the Groovy script as `q1.groovy` in your UnetStack simulation directory.

Run the simulation using:

```bash
unet q1.groovy
```

Open the web shells:

- Node A: http://localhost:8081
- Node B: http://localhost:8082

## 2. List the Running Agents

Run this command in both node shells:

```groovy
ps
```

This lists the agents running on each node.

**Screenshots required:**
- Agent list on node A.
- Agent list on node B.

## 3. Display Node Information

Run the following command in each node shell:

```groovy
node
```

Expected configuration:

| Node | Address | Location |
|---|---|---|
| A | 10 | [0, 0, -15] |
| B | 20 | [1200, 0, -15] |

Record the actual output displayed by your simulation.

## 4. Inspect PHY Parameters

Run:

```groovy
phy
```

Identify at least four PHY parameters and record their values.

Examples of parameters, depending on your UnetStack version:

- `MTU` — Maximum transmission unit.
- `queueLength` — Queue length.
- `basebandRate` — Baseband data rate.
- `carrierFrequency` — Carrier frequency.

To inspect an individual parameter, try:

```groovy
phy.MTU
```

If a parameter is unavailable, select another parameter from the list displayed by your PHY agent.

**Screenshot required:** PHY parameters and their values.

## 5. Agent-Role Table

Use the agent names displayed by `ps` to complete this table.

| Agent | Role |
|---|---|
| `phy` | Physical layer (PHY) |
| `mac` | Medium access control (MAC) |
| `uwlink` | Link layer (LINK) |
| `router` | Network routing (ROUTER) |
| `node` | Node information |
| `websh` | Web-based shell |

Agent names may differ depending on your UnetStack version.

## 6. Submission Checklist

- [ ] Groovy simulation script (`q1.groovy`).
- [ ] Screenshot of agents on node A.
- [ ] Screenshot of agents on node B.
- [ ] Screenshot of node name, address and location.
- [ ] At least four PHY parameter names and actual values.
- [ ] Completed agent-role table.

## Notes

- Record actual values from your simulation.
- Do not use example values as measured results.
- If the launcher command or parameter names differ, follow the instructions for your installed UnetStack version.
