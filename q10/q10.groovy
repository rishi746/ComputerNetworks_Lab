
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q10: Measure Basic Network Performance
//
// Topology: 1 --900 m-- 2 --900 m-- 3 --900 m-- 4
// Communication range: 1000 m
//
// Experiments:
// 1. Node 1 -> Node 2 (1 hop)
// 2. Node 1 -> Node 3 (2 hops)
// 3. Node 1 -> Node 4 (3 hops)
//
// Note: This creates the topology. Automated traffic generation and
// timestamp/statistics collection still need a benchmark agent.
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
        web: 8081, api: 1101,
        stack: "$home/etc/setup"

    node 'N2', address: 2,
        location: [900.m, 0.m, -15.m],
        web: 8082, api: 1102,
        stack: "$home/etc/setup"

    node 'N3', address: 3,
        location: [1800.m, 0.m, -15.m],
        web: 8083, api: 1103,
        stack: "$home/etc/setup"

    node 'N4', address: 4,
        location: [2700.m, 0.m, -15.m],
        web: 8084, api: 1104,
        stack: "$home/etc/setup"
}
