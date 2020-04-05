import message
import torus
from random import seed
from random import randint
from random import sample

# let's say the size of torus is 4 * 4

# seed random number generator
seed(1)
# prepare a sequence with distinct ids from 1 to 16
sequence = [i + 1 for i in range(16)]
nodes = []  # list of nodes
nodes = sample(sequence, 16)

# for i in range(len(nodes)):
#    print(str(nodes[i]))

row_1 = nodes[0:4]
row_2 = nodes[4:8]
row_3 = nodes[8:12]
row_4 = nodes[12:]

print(row_1)
print(row_2)
print(row_3)
print(row_4)

# create objects for each node
a1 = torus.Node(nodes[0])
a2 = torus.Node(nodes[1])
a3 = torus.Node(nodes[2])
a4 = torus.Node(nodes[3])
b1 = torus.Node(nodes[4])
b2 = torus.Node(nodes[5])
b3 = torus.Node(nodes[6])
b4 = torus.Node(nodes[7])
c1 = torus.Node(nodes[8])
c2 = torus.Node(nodes[9])
c3 = torus.Node(nodes[10])
c4 = torus.Node(nodes[11])
d1 = torus.Node(nodes[12])
d2 = torus.Node(nodes[13])
d3 = torus.Node(nodes[14])
d4 = torus.Node(nodes[15])

# it looks like
#   |  |  |  |
# -a1-a2-a3-a4-
#   |  |  |  |
# -b1-b2-b3-b4-
#   |  |  |  |
# -c1-c2-c3-c4-
#   |  |  |  |
# -d1-d2-d3-d4-
#   |  |  |  |

a1.set_east_neighbour(a2)
a1.set_west_neighbour(a4)
a1.set_north_neighbour(d1)
a1.set_south_neighbour(b1)

a2.set_east_neighbour(a3)
a2.set_west_neighbour(a1)
a2.set_north_neighbour(d2)
a2.set_south_neighbour(b2)

a3.set_east_neighbour(a4)
a3.set_west_neighbour(a2)
a3.set_north_neighbour(d3)
a3.set_south_neighbour(b3)

a4.set_east_neighbour(a3)
a4.set_west_neighbour(a1)
a4.set_north_neighbour(d4)
a4.set_south_neighbour(b4)

b1.set_east_neighbour(b2)
b1.set_west_neighbour(b4)
b1.set_north_neighbour(a1)
b1.set_south_neighbour(c1)

b2.set_east_neighbour(b3)
b2.set_west_neighbour(b1)
b2.set_north_neighbour(a2)
b2.set_south_neighbour(c2)

b3.set_east_neighbour(b4)
b3.set_west_neighbour(b2)
b3.set_north_neighbour(a3)
b3.set_south_neighbour(c3)

b4.set_east_neighbour(b1)
b4.set_west_neighbour(b3)
b4.set_north_neighbour(a4)
b4.set_south_neighbour(c4)

c1.set_east_neighbour(c2)
c1.set_west_neighbour(c4)
c1.set_north_neighbour(b1)
c1.set_south_neighbour(d1)

c2.set_east_neighbour(c3)
c2.set_west_neighbour(c1)
c2.set_north_neighbour(b2)
c2.set_south_neighbour(d2)

c3.set_east_neighbour(c4)
c3.set_west_neighbour(c2)
c3.set_north_neighbour(b3)
c3.set_south_neighbour(d3)

c4.set_east_neighbour(c1)
c4.set_west_neighbour(c3)
c4.set_north_neighbour(b4)
c4.set_south_neighbour(d4)

d1.set_east_neighbour(d2)
d1.set_west_neighbour(d4)
d1.set_north_neighbour(c1)
d1.set_south_neighbour(a1)

d2.set_east_neighbour(d3)
d2.set_west_neighbour(d1)
d2.set_north_neighbour(c2)
d2.set_south_neighbour(a2)

d3.set_east_neighbour(d4)
d3.set_west_neighbour(d2)
d3.set_north_neighbour(c3)
d3.set_south_neighbour(a3)

d4.set_east_neighbour(d1)
d4.set_west_neighbour(d3)
d4.set_north_neighbour(c4)
d4.set_south_neighbour(a4)

# print(a1.id)
# print(a1.east.id)
# print(a1.east.east.id)
# print(a1.south.east.id)

# now, all nodes are connected to their neighbours, like a real torus

