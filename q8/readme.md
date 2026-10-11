
# Q8: Static Routing in an Out-of-Range Topology

## 1. Objective

Create three nodes with addresses 11, 12, and 13. Nodes 11 and 13 must communicate through node 12 using static routes.

## 2. Run the Simulation

Save the topology script as `q8.groovy`.

Run:

```bash
bin/unet q8.groovy
```

Open the node shells:

- Node 11: http://localhost:8081
- Node 12: http://localhost:8082
- Node 13: http://localhost:8083

## 3. Test Before Adding Routes

Initially, do not configure static routes.

From node 11, attempt to send a datagram to node 13.

Record the failed delivery or timeout.

Take a screenshot showing the unsuccessful attempt.

## 4. Configure Static Routes

Configure the following routes at startup:

On node 11:

```text
Destination: 13
Next hop: 12
```

On node 13:

```text
Destination: 11
Next hop: 12
```

Node 12 must forward traffic between nodes 11 and 13.

Restart the simulation after configuring the routes.

## 5. Display Routing Tables

On node 11, run:

```groovy
routes
```

On node 13, run:

```groovy
routes
```

Verify that node 11 routes destination 13 through node 12 and node 13 routes destination 11 through node 12.

Take screenshots of both routing tables.

## 6. Test Communication

Send a datagram from node 11 to node 13.

Then send a reply from node 13 to node 11.

Confirm that both datagrams are delivered successfully.

## 7. Verify the Route

Use the available routing trace or simulation logs to confirm that the packet passed through node 12.

Record the relevant log lines.

## 8. Expected Routing Table

| Node | Destination | Next hop |
|---|---:|---:|
| 11 | 13 | 12 |
| 13 | 11 | 12 |

## 9. Submission Checklist

- [ ] `q8.groovy` topology script.
- [ ] Output showing failure before routes are configured.
- [ ] Static routes configured at startup.
- [ ] Routing table screenshot from node 11.
- [ ] Routing table screenshot from node 13.
- [ ] Successful datagram from node 11 to node 13.
- [ ] Successful reply from node 13 to node 11.
- [ ] Log excerpt showing forwarding through node 12.
