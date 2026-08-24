from nest.topology import *

h1 = Node("h1")
h2 = Node("h2")
r1 = Router("r1")
r2 = Router("r2")

eth1, etr1a = connect(h1, r1)
etr1b, etr2a = connect(r1, r2)
etr2b, eth2 = connect(r2, h2)

eth1.set_address("192.168.1.1/24")
etr1a.set_address("192.168.1.2/24")

etr1b.set_address("192.168.2.1/24")
etr2a.set_address("192.168.2.2/24")

etr2b.set_address("192.168.3.1/24")
eth2.set_address("192.168.3.2/24")

eth1.set_attributes("5mbit", "5ms")
etr1a.set_attributes("10mbit", "100ms")

etr1b.set_attributes("5mbit", "5ms")
etr2a.set_attributes("10mbit", "100ms")

etr2b.set_attributes("5mbit", "5ms")
eth2.set_attributes("10mbit", "100ms")

h1.add_route("DEFAULT", eth1)
r1.add_route("DEFAULT", etr1b)
r2.add_route("DEFAULT", etr2b)
h2.add_route("DEFAULT", eth2)

h1.ping(eth2.address)