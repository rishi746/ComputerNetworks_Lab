
# Q5: Unicast and Broadcast Datagrams

## 1. Run the Simulation

Save the Groovy script as `q5.groovy`.

Run it using your UnetStack launcher. If supported:

```bash
unet q5.groovy
```

Open the node shells:

- Node 1: http://localhost:8081
- Node 2: http://localhost:8082
- Node 3: http://localhost:8083

## 2. Inspect the Agents

Run this command in each node shell:

```groovy
ps
```

Identify the agent that handles datagrams. In a standard UnetStack configuration, this is commonly the `uwlink` agent.

## 3. Prepare the Message

On node 1, replace `YOUR_ROLL_NUMBER` with your actual roll number.

```groovy
def msg = "HELLO-YOUR_ROLL_NUMBER"
def payload = msg.getBytes("UTF-8").collect {
    it & 0xff
}
```

## 4. Send a Unicast Datagram

Send the message from node 1 to node 3 using `DatagramReq` and `Protocol.USER`.

```groovy
uwlink << new DatagramReq(
    to: 3,
    protocol: Protocol.USER,
    data: payload
)
```

Expected result:

- Node 3 receives the message.
- Node 2 should not receive this unicast datagram.

## 5. Send a Broadcast Datagram

Send a broadcast from node 1:

```groovy
uwlink << new DatagramReq(
    to: 0,
    protocol: Protocol.USER,
    data: payload
)
```

Expected result:

- Node 2 receives the broadcast.
- Node 3 receives the broadcast.

Address `0` is used for broadcast addressing in this setup. Confirm this against the installed UnetStack version.

## 6. Observe Received Datagrams

On nodes 2 and 3, subscribe to notifications from the datagram-handling agent using the subscription syntax supported by your shell.

Watch for `DatagramNtf` notifications.

Record the sender, destination, protocol and received data. Decode the data bytes as UTF-8 to verify the message.

If the shell does not support the example request syntax, inspect the agent's help and use the equivalent supported operation.

## 7. Expected Results

| Transmission | Destination | Node 2 | Node 3 |
|---|---:|---|---|
| Unicast | 3 | Should not receive | Should receive |
| Broadcast | 0 | Should receive | Should receive |

The decoded message should be:

`HELLO-YOUR_ROLL_NUMBER`

Replace the placeholder with your actual roll number.

## 8. Submission Checklist

- [ ] `q5.groovy` simulation script.
- [ ] Screenshot showing the unicast request at node 1.
- [ ] Screenshot showing the unicast notification at node 3.
- [ ] Screenshot showing the broadcast request at node 1.
- [ ] Screenshot showing broadcast reception at nodes 2 and 3.
- [ ] Decoded message text at the receivers.
- [ ] Completed results table.

## Notes

- The three nodes are configured within the 1500 m communication range.
- Use `Protocol.USER` for both transmissions.
- Use `DatagramReq` for application datagrams, not `TxFrameReq`, which is intended for raw PHY frames.
- Record actual results from the running simulation rather than assuming delivery.
