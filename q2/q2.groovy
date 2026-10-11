
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q2: Ping and range measurement at different distances
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

channel.model = ProtocolChannelModel
channel.communicationRange = 2000.m
channel.detectionRange = 2200.m
channel.interferenceRange = 2500.m
channel.pDetection = 1
channel.pDecoding = 1

simulate {
    node 'A', address: 10,
        location: [0.m, 0.m, -15.m],
        web: 8081,
        api: 1101,
        stack: "$home/etc/setup"

    // Run 1: 500 m
    // Change 500.m to 1000.m and 1500.m for runs 2 and 3.
    node 'B', address: 20,
        location: [500.m, 0.m, -15.m],
        web: 8082,
        api: 1102,
        stack: "$home/etc/setup"
}
