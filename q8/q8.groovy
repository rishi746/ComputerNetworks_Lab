import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q8: Static routing in an out-of-range topology
//
// Nodes 11 and 13 are 1600 m apart, outside the 1000 m communication range.
// Both can directly reach node 12, which is 800 m from either endpoint.
//
// NOTE: This is the topology setup. Static route installation must be added
// using the router API/startup hook supported by your installed UnetStack
// version; see README_Q8.md for the required route entries and test steps.
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

channel.model = ProtocolChannelModel
channel.communicationRange = 1000.m
channel.detectionRange = 1200.m
channel.interferenceRange = 1500.m
channel.pDetection = 1
channel.pDecoding = 1

simulate {
    node 'N11', address: 11,
        location: [0.m, 0.m, -15.m],
        web: 8081, api: 1101,
        stack: "$home/etc/setup"

    node 'N12', address: 12,
        location: [800.m, 0.m, -15.m],
        web: 8082, api: 1102,
        stack: "$home/etc/setup"

    node 'N13', address: 13,
        location: [1600.m, 0.m, -15.m],
        web: 8083, api: 1103,
        stack: "$home/etc/setup"
}
