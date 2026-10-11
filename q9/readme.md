
# Q9: Multi-Hop Communication with Route Discovery

## 1. Run the Simulation

Save the script as `q9.groovy`.

Run it from your UnetStack installation directory:

```bash
bin/unet q9.groovy
```

Open the web shells:

- Node 1: http://localhost:8081
- Node 2: http://localhost:8082
- Node 3: http://localhost:8083
- Node 4: http://localhost:8084

## 2. Discover the Route

In node 1's shell, subscribe to route-discovery notifications:

```groovy
subscribe rdp
```

Request route discovery to node 4:

```groovy
rreq 4
```

Wait for the discovery process to complete. Then display the routing table:

```groovy
routes
```

Find the entry for destination 4.

Expected route:

```text
1 -> 2 -> 3 -> 4
```

From node 1:
- Destination: 4
- Next hop: 2
- Hop count: 3

Record the actual notifications and routing-table output.

## 3. Send a Datagram to Node 4

From node 1's shell, send a datagram through the router:

```groovy
router << new DatagramReq(
    to: 4,
    protocol: Protocol.USER,
    data: 'hello node four'.getBytes('UTF-8').collect { it & 0xff }
)
```

Observe the datagram at node 4 and confirm that the message was received.

## 4. Move Node 3 Out of Range

Stop the simulation.

In `q9.groovy`, change node 3's location from:

```groovy
location: [1800.m, 0.m, -15.m]
```

to:

```groovy
location: [5000.m, 0.m, -15.m]
```

Restart the simulation.

Node 2 and node 4 are now 1800 m apart, exceeding the 1000 m communication range.

## 5. Repeat Route Discovery

On node 1, run:

```groovy
subscribe rdp
rreq 4
```

Then inspect the routing table:

```groovy
routes
```

The route through node 3 should no longer be available. Record the discovery notifications and the actual result.

Do not configure static routes.

## 6. Results Table

| Experiment | Expected result |
|---|---|
| Initial chain | Route discovered and datagram delivered |
| Node 3 moved to 5000 m | No complete route to node 4 through the chain |

Route discovery can be probabilistic. If discovery fails on the initial connected topology, repeat `rreq 4` and record the actual outcome.

## 7. Submission Checklist

- [ ] `q9.groovy` simulation script.
- [ ] Route-discovery notifications from node 1.
- [ ] Routing table at node 1.
- [ ] Next-hop node and hop count for node 4.
- [ ] Datagram received at node 4.
- [ ] Modified topology for the second experiment.
- [ ] Route-discovery result after moving node 3.
- [ ] Confirmation that no static routes were added.
