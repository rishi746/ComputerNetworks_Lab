
# Q7: Write a Custom Echo Agent

## 1. Create the Agent

Save `EchoAgent.groovy` in the UnetStack installation's `classes/` directory.

The agent:
- Listens for datagram notifications.
- Accepts only `Protocol.USER` messages.
- Converts received text to uppercase.
- Appends the reception timestamp.
- Replies to the original sender using `Protocol.DATA`.

## 2. Run the Simulation

Save the topology script as `q7.groovy`.

Run:

```bash
bin/unet q7.groovy
```

Open the web shells:

- Node 1: http://localhost:8081
- Node 2: http://localhost:8082

## 3. Load EchoAgent on Node 2

In node 2's shell, run:

```groovy
container.add 'echo', new EchoAgent()
```

Verify that the agent is running:

```groovy
ps
```

Look for `echo: EchoAgent`.

Take a screenshot of the agent list.

## 4. Send Three Messages from Node 1

Subscribe to PHY notifications:

```groovy
subscribe phy
```

Send the first lowercase message:

```groovy
phy << new DatagramReq(
    to: 2,
    protocol: Protocol.USER,
    data: 'hello there'.getBytes('UTF-8').collect { it & 0xff }
)
```

Send two more messages using the same command with different text, for example:

- `unetstack test`
- `echo agent`

Inspect the received datagram notifications and decode the data as UTF-8.

## 5. Expected Replies

| Sent message | Expected reply text |
|---|---|
| `hello there` | `HELLO THERE | Received at: <timestamp>` |
| `unetstack test` | `UNETSTACK TEST | Received at: <timestamp>` |
| `echo agent` | `ECHO AGENT | Received at: <timestamp>` |

The timestamp is generated when the agent receives the message, so its value changes between messages.

## 6. Submission Checklist

- [ ] `EchoAgent.groovy`
- [ ] `q7.groovy`
- [ ] Screenshot showing EchoAgent in node 2's agent list
- [ ] Three lowercase messages sent from node 1
- [ ] Three uppercase replies with timestamps
- [ ] Screenshot showing the messages and replies

## Notes

- Ensure `EchoAgent.groovy` is saved in the `classes/` directory.
- Use `Protocol.DATA` for replies to avoid an infinite echo loop.
- Record actual output from your simulation.
