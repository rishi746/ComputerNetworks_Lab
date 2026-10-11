
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q6: Modified 2-node-network.groovy
//
// CHANGES:
// 1. Use three nodes instead of two.
// 2. Add node 3 with address 3.
// 3. Place nodes 800 m apart.
// 4. Configure a 10-minute discrete-event simulation.
// 5. Schedule pings from node 1 to node 3 every 30 seconds.
///////////////////////////////////////////////////////////////////////////////

platform = DiscreteEventSimulator

channel.model = ProtocolChannelModel
channel.communicationRange = 1000.m
channel.detectionRange = 1200.m
channel.interferenceRange = 1500.m
channel.pDetection = 1
channel.pDecoding = 1

simulate {
    node 'N1', address: 1,
        location: [0.m, 0.m, -15.m],
        web: 8081,
        api: 1101,
        stack: "$home/etc/setup"

    node 'N2', address: 2,
        location: [800.m, 0.m, -15.m],
        web: 8082,
        api: 1102,
        stack: "$home/etc/setup"

    // CHANGED: Added third node, 800 m from node 2.
    node 'N3', address: 3,
        location: [1600.m, 0.m, -15.m],
        web: 8083,
        api: 1103,
        stack: "$home/etc/setup"
}
