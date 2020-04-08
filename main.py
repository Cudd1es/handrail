import message
import torus
from random import seed
from random import randint
from random import sample
import sys

# let's say the size of torus is 4 * 4

# seed random number generator
seed(1)

if sys.argv[1] is None:
    print("usage: python main.py d(d is the longest distance to go straightforwardly")
d = int(sys.argv[1])
# prepare a sequence with distinct ids from 1 to 16
sequence = [i + 1 for i in range(16)]
# nodes = []  # list of nodes
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
# let's say the node on the topleft (a1) is the
# beginning node, and east is the direction to send message and south is the direction of handrail.


# msg_1 = message.Message(d)
# msg_1.set_direction('east')
# msg_1.set_handrail(a1.south)
# msg_1.set_id(a1.id)
# msg_1.set_current_node(a1)


# init a message from the topleft node
# The function that make the message be straightly forwarded within distance d
def straight(msg):
    direction = msg.direction
    current_switcher = {
        'east': msg.current_node.east,
        'west': msg.current_node.west,
        'north': msg.current_node.north,
        'south': msg.current_node.south
    }
    nde = current_switcher.get(direction, 'Invalid direction')
    handrail_switcher = {
        'east': msg.handrail.east,
        'west': msg.handrail.west,
        'north': msg.handrail.north,
        'south': msg.handrail.south
    }
    n_handrail = handrail_switcher.get(direction, 'Invalid direction')
    msg.set_last_node(msg.current_node)
    msg.set_current_node(nde)
    msg.set_handrail(n_handrail)
    msg.set_current_d(msg.current_d + 1)
#    if msg.current_node.id < msg.original_id:
#        msg.saw_smaller = True
#    elif msg.current_node.id > msg.original_id:
#        msg.seen_by_smaller = True
#    else:
#        msg.looking = False


# have a try and see if it works

# print(msg_1.current_node.id, msg_1.current_d, msg_1.handrail.id)
# the result shows "5 0 2"
# straight(msg_1)
# print(msg_1.current_node.id, msg_1.current_d, msg_1.handrail.id)
# the result shows "10 1 16"
# so it seems that the straight() function works

def turn(msg):
    last_node = msg.last_node
    current_node = msg.current_node
    handrail_node = msg.handrail
    if current_node.east_neighbour() == handrail_node:
        n_direction = 'east'
    elif current_node.west_neighbour() == handrail_node:
        n_direction = 'west'
    elif current_node.north_neighbour() == handrail_node:
        n_direction = 'north'
    else:
        n_direction = 'south'
    msg.set_direction(n_direction)
    msg.set_handrail(last_node)
    msg.set_current_d(0)


# have a try and see if it works


# print(msg_1.current_node.id, msg_1.current_d, msg_1.handrail.id)
# the result shows "5 0 2"
# while msg_1.current_d != d:
#    straight(msg_1)
#    print(msg_1.current_node.id, msg_1.current_d, msg_1.handrail.id)
# the result shows "10 1 16", "14, 2, 12"
# turn(msg_1)
# print(msg_1.current_node.id, msg_1.current_d, msg_1.handrail.id)
# the result shows "14 0 10"
# so it seems that the turn() function works

def print_stat(msg):
    print(msg.current_node.id, msg.current_d, msg.handrail.id, msg.direction)


# now, let's have a walkthrough


msg_1 = message.Message(d)
msg_1.set_direction('east')
msg_1.set_handrail(a1.south)
msg_1.set_id(a1.id)
msg_1.set_current_node(a1)

print('the stat of message (current node id, current d, handrail, current direction): ')
print('[beginning]')
print_stat(msg_1)

# go straightforwardly
print('[straightforwardly] ')
while msg_1.current_d < d:
    straight(msg_1)
    print_stat(msg_1)

# first turn
print('[turning]')
turn(msg_1)
print_stat(msg_1)

# go straightforwardly again
print('[straightforwardly] ')
while msg_1.current_d < d:
    straight(msg_1)
    print_stat(msg_1)

# second turn
print('[turning]')
turn(msg_1)
print_stat(msg_1)

# go straightforwardly again
print('[straightforwardly] ')
while msg_1.current_d < d:
    straight(msg_1)
    print_stat(msg_1)

# third turn
print('[turning]')
turn(msg_1)
print_stat(msg_1)

# go straightforwardly again
print('[straightforwardly] ')
while msg_1.current_d < d:
    straight(msg_1)
    print_stat(msg_1)

# now, the message is supposed to be at the starting node
# print("saw smaller:", msg_1.saw_smaller, " seen by smaller:", msg_1.seen_by_smaller, " looking:", msg_1.looking)
