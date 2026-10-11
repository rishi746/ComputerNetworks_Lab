
# Q10: Measure Basic Network Performance

## 1. Objective

Measure network performance for 1-hop, 2-hop, and 3-hop paths using a four-node chain.

Send 50 datagrams from node 1, one every 20 seconds, in three separate experiments:

- Node 1 to node 2: 1 hop
- Node 1 to node 3: 2 hops
- Node 1 to node 4: 3 hops

## 2. Run the Simulation

Save the script as `q10.groovy`.

Run it using your installed UnetStack launcher:

```bash
bin/unet q10.groovy
```

The simulation uses `DiscreteEventSimulator`.

## 3. Configure Routing

Use the automatic route-discovery procedure from Q9.

Before each experiment, verify that node 1 has a working route to the destination.

Do not add static routes if the assignment requires automatic route discovery.

## 4. Generate Traffic

For each destination, the benchmark logic must:

1. Send 50 uniquely identified datagrams from node 1.
2. Schedule one datagram every 20 simulated seconds.
3. Record each packet's ID and send timestamp.
4. Record each received packet's ID and receive timestamp.
5. Match received packets to their corresponding send timestamps.
6. Count packets sent and received.

The topology script alone does not generate this traffic. Implement the traffic generator and timestamp collection using the APIs supported by your installed UnetStack version.

## 5. Calculate Performance Metrics

### Packet Delivery Ratio

```text
PDR (%) = (Packets received / Packets sent) * 100
```

### Average End-to-End Delay

```text
Packet delay = Receive time - Send time

Average delay = Sum of received packet delays / Packets received
```

If no packets are received, report average delay as N/A.

### Throughput

```text
Throughput (bits/s) =
Total successfully received payload bits / Measurement duration
```

Use the same measurement-duration convention for all three experiments and state it in the report.

## 6. Results Table

| Path | Hops | Sent | Received | PDR (%) | Average delay (s) | Throughput (bits/s) |
|---|---:|---:|---:|---:|---:|---:|
| 1 → 2 | 1 | 50 | | | | |
| 1 → 3 | 2 | 50 | | | | |
| 1 → 4 | 3 | 50 | | | | |

Fill in the values from the actual simulation.

## 7. Expected Terminal Output

Print the following statistics after each run:

```text
Destination: <address>
Hops: <number>
Packets sent: 50
Packets received: <measured count>
Packet delivery ratio: <measured percentage> %
Average end-to-end delay: <measured value> s
Throughput: <measured value> bits/s
```

## 8. Submission Checklist

- [ ] q10.groovy simulation script.
- [ ] Automated generator sending 50 packets every 20 seconds.
- [ ] Send and receive timestamps recorded per packet.
- [ ] Separate runs for destinations 2, 3, and 4.
- [ ] Terminal statistics for all runs.
- [ ] Completed performance comparison table.

## Important Note

The supplied Groovy file creates the network topology. It does not yet implement the benchmark agent, automatic packet generation, or metric calculations. Those components are necessary to satisfy the full assignment.
