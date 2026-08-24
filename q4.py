from nest.topology import *

h1 = Node("h1")
h2 = Node("h2")
h3 = Node("h3")
h4 = Node("h4")
s1 = Switch("s1")

eth1, s1eth1 = connect(h1, s1)
eth2, s1eth2 = connect(h2, s1)
eth3, s1eth3 = connect(h3, s1)
eth4, s1eth4 = connect(h4, s1)

eth1.set_address("192.168.1.1/24")
eth2.set_address("192.168.1.2/24")
eth3.set_address("192.168.1.3/24")
eth4.set_address("192.168.1.4/24")

eth1.set_attributes("100mbit", "1ms")
eth2.set_attributes("100mbit", "1ms")
eth3.set_attributes("100mbit", "1ms")
eth4.set_attributes("100mbit", "1ms")

h1.ping(eth2.address)
h3.ping(eth4.address)