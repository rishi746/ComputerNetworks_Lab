from nest.topology import *

h1 = Node("h1")
h2 = Node("h2")
h3 = Node("h3")
h4 = Node("h4")
h5 = Node("h5")
h6 = Node("h6")

s1 = Switch("s1")
s2 = Switch("s2")

r1 = Router("r1")

eth1, ets1a = connect(h1, s1)
eth2, ets1b = connect(h2, s1)
eth3, ets1c = connect(h3, s1)

eth4, ets2a = connect(h4, s2)
eth5, ets2b = connect(h5, s2)
eth6, ets2c = connect(h6, s2)

ets1d, etr1a = connect(s1, r1)
ets2d, etr1b = connect(s2, r1)

eth1.set_address("192.168.1.1/24")
eth2.set_address("192.168.1.2/24")
eth3.set_address("192.168.1.3/24")
s1.set_address("192.168.1.4/24")
etr1a.set_address("192.168.1.5/24")

eth4.set_address("192.168.2.1/24")
eth5.set_address("192.168.2.2/24")
eth6.set_address("192.168.2.3/24")
s2.set_address("192.168.2.4/24")
etr1b.set_address("192.168.2.5/24")

eth1.set_attributes("100mbit", "1ms")
eth2.set_attributes("100mbit", "1ms")
eth3.set_attributes("100mbit", "1ms")
eth4.set_attributes("100mbit", "1ms")
eth5.set_attributes("100mbit", "1ms")
eth6.set_attributes("100mbit", "1ms")

etr1a.set_attributes("10mbit", "10ms")
etr1b.set_attributes("10mbit", "10ms")

h1.add_route("DEFAULT", eth1, etr1a.address)
h2.add_route("DEFAULT", eth2, etr1a.address)
h3.add_route("DEFAULT", eth3, etr1a.address)

h4.add_route("DEFAULT", eth4, etr1b.address)
h5.add_route("DEFAULT", eth5, etr1b.address)
h6.add_route("DEFAULT", eth6, etr1b.address)

h1.ping(eth4.address)
h2.ping(eth5.address)
h3.ping(eth6.address)