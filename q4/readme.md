
# Q4: Send Raw Frames Using the PHY Agent

## 1. Run the Simulation

Save the simulation script as `q4.groovy`.

Run it using your UnetStack launcher. If supported:

```bash
unet q4.groovy
```

Open the web shells:

- Node A (address 10): http://localhost:8081
- Node B (address 20): http://localhost:8082

## 2. Subscribe to PHY Notifications on Node B

Open node B's shell.

Identify the PHY agent using:

```groovy
ps
```

Subscribe to the PHY agent's notifications using the supported subscription command for your UnetStack version.

Keep node B's shell open so you can observe incoming frame notifications.

## 3. Prepare the Roll Number Bytes

Open node A's shell.

Replace `YOUR_ROLL_NUMBER` with your actual roll number.

```groovy
def payload = "YOUR_ROLL_NUMBER".getBytes("UTF-8").collect {
    it & 0xff
}
```

The resulting list contains the byte values of the roll number.

## 4. Transmit on the CONTROL Channel

Use the PHY agent to send a `TxFrameReq` with the CONTROL frame type.

The request must contain the payload bytes and use the CONTROL channel/frame type supported by your installed UnetStack version.

Observe the transmit request and `TxFrameNtf` at node A.

## 5. Transmit on the DATA Channel

Send the same payload using a second `TxFrameReq`, this time using the DATA frame type supported by your installed UnetStack version.

Observe the transmit request and `TxFrameNtf` at node A.

Check node B's shell for the corresponding `RxFrameNtf` notifications and received bytes.

**Note:** Verify the exact `TxFrameReq` fields, frame-type constants, and PHY notification subscription syntax against your installed UnetStack version. Do not assume that a command succeeds merely because it was entered.

## 6. Record Frame Parameters

Inspect the PHY agent and its supported parameters. Record the frame length and data rate for each channel.

| Parameter | CONTROL | DATA |
|---|---:|---:|
| Frame length (bytes) | | |
| Data rate (bits/s) | | |
| Transmission duration (s) | | |

Calculate the nominal transmission duration using:

```text
Transmission duration = (Frame length in bytes * 8) / Data rate in bits per second
```

Use the actual frame length and data rate reported by your simulation.

## 7. Expected Output

### Node A

- CONTROL-channel transmit request.
- CONTROL-channel `TxFrameNtf`.
- DATA-channel transmit request.
- DATA-channel `TxFrameNtf`.

### Node B

- Received-frame notification for the CONTROL transmission.
- Received-frame notification for the DATA transmission.
- Received bytes corresponding to the roll number.

## 8. Submission Checklist

- [ ] `q4.groovy` simulation script.
- [ ] Screenshot of CONTROL transmission at node A.
- [ ] Screenshot of DATA transmission at node A.
- [ ] Screenshot of received frames at node B.
- [ ] Frame length recorded for both channels.
- [ ] Data rate recorded for both channels.
- [ ] Transmission duration calculated for both channels.
- [ ] Comparison table completed.

## Notes

- Nodes A and B must remain 1000 m apart.
- Use the actual PHY parameters and frame notifications from your simulation.
- If a frame is not received, check the channel configuration, frame type, notification subscription, and supported request fields.
