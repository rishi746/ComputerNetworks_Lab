
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q9: Multi-hop communication with automatic route discovery
//
// Initial topology: 1 --900 m-- 2 --900 m-- 3 --900 m-- 4
// Communication range: 1000 m
//
// No static routes are configured.
//
// Experiment 2:
// Move node 3 to 5000 m by changing its x-coordinate below, then restart.
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

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

    // Change 1800.m to 5000.m for experiment 2.
    node 'N3', address: 3,
        location: [1800.m, 0.m, -15.m],
        web: 8083, api: 1103,
        stack: "$home/etc/setup"

    node 'N4', address: 4,
        location: [2700.m, 0.m, -15.m],
        web: 8084, api: 1104,
        stack: "$home/etc/setup"
}
