
# Q6: Modify an Existing Script and Read the Simulation Log

## 1. Objective

Modify the handbook's `2-node-network.groovy` to create three nodes, run a 10-minute discrete-event simulation, and analyze the generated log file.

## 2. Changes Made

- Added node 3 with address 3.
- Changed node locations so adjacent nodes are 800 m apart.
- Configured `DiscreteEventSimulator`.
- Configured the channel model and communication ranges.
- Required traffic: node 1 pings node 3 every 30 seconds for 10 minutes.

## 3. Run the Simulation

Save your modified script as `q6.groovy`.

From the UnetStack installation directory, run:

```bash
bin/unet q6.groovy
```

On Windows, use:

```powershell
bin\unet q6.groovy
```

Wait for the simulation to finish.

**Important:** The topology script must also include a working periodic-ping schedule and a 10-minute simulation termination condition. Merely setting `platform = DiscreteEventSimulator` does not implement those requirements.

## 4. Open the Simulation Log

After the simulation finishes, open:

```text
logs/log-0.txt
```

You can open this file in VS Code or another text editor.

Search for relevant events, such as:

- `TxFrameNtf` — transmission notification.
- `RxFrameNtf` — reception notification.
- `PingReq` — ping request, if logged.
- `PingRsp` — ping response, if logged.
- `Created static node` — node creation.
- `BEGIN SIMULATION` — simulation start.

The exact entries depend on the agents and logging levels enabled.

## 5. Find a Transmitted Frame and Its Reception

Search the log for transmission and reception events.

Example format from a UnetStack log:

```text
5673|INFO|org.arl.unet.sim.SimulationAgent/3@570:call|TxFrameNtf:INFORM[type:DATA txTime:...]
```

This is an illustrative example of a transmission notification, not a line from your simulation.

For your report, copy actual log lines showing at least one transmitted frame and its reception. Include the corresponding timestamps and node/agent names when available.

## 6. Interpret the Log

A typical log line has four fields:

```text
timestamp | log level | source component | event message
```

| Field | Meaning |
|---|---|
| Timestamp | Time of the logged event |
| Log level | INFO, WARNING, or another logging level |
| Source component | Agent or simulation component that generated the log |
| Event message | Description of the event |

During discrete-event simulation, timestamps generally represent simulated time rather than wall-clock time.

## 7. Count Pings and Replies

Inspect the log for the actual ping request and response events.

Record:

- Number of ping requests sent by node 1.
- Number of replies received from node 3.

Do not count frame transmissions as ping requests: a ping may generate multiple lower-layer frames.

The expected schedule is one ping every 30 seconds over 10 minutes. Depending on whether the schedule includes time zero and whether the endpoint is included, the expected number of scheduled requests may differ. Confirm the actual schedule and count the requests in the log.

Use this table:

| Metric | Count |
|---|---:|
| Ping requests sent | |
| Ping replies received | |
| Requests without replies | |

Requests without replies can be calculated as:

```text
Requests without replies = Requests sent - Replies received
```

## 8. Selected Log Lines

Include no more than 15 actual log lines in your report.

| Log line | Time | Node/Agent | Event interpretation |
|---|---|---|---|
| 1 | | | Simulation initialization |
| 2 | | | Node creation |
| 3 | | | Ping request or transmission |
| 4 | | | Frame reception |
| 5 | | | Ping reply |
| ... | | | |

Replace the blank fields with information from your own log.

## 9. Submission Checklist

- [ ] Original `2-node-network.groovy`.
- [ ] Modified `q6.groovy`, with changes commented.
- [ ] Three-node topology.
- [ ] 10-minute discrete-event run.
- [ ] Periodic ping schedule at 30-second intervals.
- [ ] Actual log lines for transmission and reception.
- [ ] Up to 15 log lines with explanations.
- [ ] Ping request and reply counts.
