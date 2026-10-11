
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q4: Send raw frames using the PHY agent
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

channel.model = ProtocolChannelModel
channel.communicationRange = 1500.m
channel.detectionRange = 2000.m
channel.interferenceRange = 2500.m
channel.pDetection = 1
channel.pDecoding = 1

simulate {
    node 'A', address: 10,
        location: [0.m, 0.m, -15.m],
        web: 8081,
        api: 1101,
        stack: "$home/etc/setup"

    node 'B', address: 20,
        location: [1000.m, 0.m, -15.m],
        web: 8082,
        api: 1102,
        stack: "$home/etc/setup"
}
