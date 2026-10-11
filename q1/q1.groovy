
import org.arl.fjage.*
import org.arl.unet.*
import org.arl.unet.sim.channels.*

///////////////////////////////////////////////////////////////////////////////
// Q1: Build a 2-node network and inspect its agents
///////////////////////////////////////////////////////////////////////////////

platform = RealTimePlatform

channel.model = ProtocolChannelModel

simulate {
    node 'A', address: 10,
        location: [0.m, 0.m, -15.m],
        web: 8081,
        api: 1101,
        stack: "$home/etc/setup"

    node 'B', address: 20,
        location: [1200.m, 0.m, -15.m],
        web: 8082,
        api: 1102,
        stack: "$home/etc/setup"
}
