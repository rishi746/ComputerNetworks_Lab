
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q3: Communication range using ProtocolChannelModel
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

channel.model = ProtocolChannelModel

channel.communicationRange = 1500.m
channel.detectionRange = 2000.m
channel.interferenceRange = 2500.m

channel.pDetection = 1
channel.pDecoding = 1

simulate {
    node 'N1', address: 1,
        location: [0.m, 0.m, -15.m],
        web: 8081,
        api: 1101,
        stack: "$home/etc/setup"

    node 'N2', address: 2,
        location: [1200.m, 0.m, -15.m],
        web: 8082,
        api: 1102,
        stack: "$home/etc/setup"

    // Change 2400.m to 1800.m for the second experiment.
    node 'N3', address: 3,
        location: [2400.m, 0.m, -15.m],
        web: 8083,
        api: 1103,
        stack: "$home/etc/setup"
}
