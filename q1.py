from nest.topology import *

h1 = Node("h1")
h2 = Node("h2")

eth1, eth2 = connect(h1, h2)

eth1.set_address("192.168.1.1/24")
eth2.set_address("192.168.1.2/24")

eth1.set_attributes("5mbit", "5ms")
eth2.set_attributes("10mbit", "100ms")

h1.ping(eth2.address)