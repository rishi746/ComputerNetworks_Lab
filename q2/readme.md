
# Q2: Ping and Range Measurement at Different Distances

## 1. Run the Simulation

Save the Groovy script as `q2.groovy`.

Run it using your UnetStack launcher. If supported:

```bash
unet q2.groovy
```

Open node A's web shell:

http://localhost:8081

## 2. Test Three Distances

Run the simulation three separate times.

Change node B's location in `q2.groovy` for each run:

### Run 1: 500 m

```groovy
location: [500.m, 0.m, -15.m]
```

### Run 2: 1000 m

```groovy
location: [1000.m, 0.m, -15.m]
```

### Run 3: 1500 m

```groovy
location: [1500.m, 0.m, -15.m]
```

Keep node A at `[0.m, 0.m, -15.m]` and preserve addresses 10 and 20.

Restart the simulation after each change.

## 3. Ping Node 20

In node A's shell, run:

```groovy
ping 20
```

Collect at least five RTT measurements at each distance.

If the command does not produce five measurements, consult the shell's help and repeat the ping operation until you have at least five RTT values.

Take a screenshot of the ping output for each distance.

## 4. Measure the Range

First list the available agents:

```groovy
ps
```

Identify the ranging agent and use its supported command or request to measure the range to node 20.

The exact ranging command depends on the installed UnetStack version and the available agents. Use the agent's help or supported operations instead of guessing a command.

Record the estimated range and take a screenshot for each distance.

## 5. Calculate Average RTT

Use the following formula:

Average RTT = Sum of all measured RTT values / Number of measurements

For five measurements:

Average RTT = (RTT1 + RTT2 + RTT3 + RTT4 + RTT5) / 5

## 6. Calculate Range Error

Use the absolute error formula:

Range Error = |Estimated Range - Actual Distance|

For example, if the actual distance is 500 m and the estimated range is 480 m:

Range Error = |480 - 500| = 20 m

Use your actual measured values in the report.

## 7. Results Table

| Actual Distance (m) | Average RTT (ms) | Estimated Range (m) | Error (m) |
|---:|---:|---:|---:|
| 500 | | | |
| 1000 | | | |
| 1500 | | | |

Fill in the table using your simulation results.

## 8. Explanation

Underwater acoustic signals travel at approximately 1500 m/s, which is much slower than radio signals in air. As the distance between the nodes increases, signal propagation time increases, generally resulting in a higher round-trip time (RTT). Processing and modem delays can also affect the measured RTT.

## 9. Submission Checklist

- [ ] `q2.groovy` simulation script.
- [ ] Ping and range screenshot at 500 m.
- [ ] Ping and range screenshot at 1000 m.
- [ ] Ping and range screenshot at 1500 m.
- [ ] Completed results table.
- [ ] Explanation of why RTT increases with distance.

## Notes

- Use actual values from your simulation.
- Do not invent RTT or range measurements.
- Ensure a ranging agent is available and configured.
- If commands differ, follow the documentation for your installed UnetStack version.
