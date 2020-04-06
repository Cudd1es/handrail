# let's imagine that we have successfully let each node knows the location of its neighbours thanks to district labeling
# So each nodes knows its neighbours on the west, east, north and south.


class Node:
    def __init__(self, id):
        self.id = id
        self.survive = True

    def set_west_neighbour(self, nde):
        self.west = nde

    def west_neighbour(self):
        return self.west

    def set_east_neighbour(self, nde):
        self.east = nde

    def east_neighbour(self):
        return self.east

    def set_north_neighbour(self, nde):
        self.north = nde

    def north_neighbour(self):
        return self.north

    def set_south_neighbour(self, nde):
        self.south = nde

    def south_neighbour(self):
        return self.south
