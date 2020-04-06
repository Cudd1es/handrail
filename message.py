# a message contains the following properties:
# longest straightforward distance, handrail, states(looking, saw_smaller, seen_by_smaller)


class Message:
    def __init__(self, d):
        self.d = d
        self.current_d = 0
        self.looking = True
        self.saw_smaller = False
        self.seen_by_smaller = False
        self.original_id = -1

    def set_handrail(self, handrail):
        self.handrail = handrail

    def handrail(self):
        return self.handrail

    def set_direction(self, direction):
        self.direction = direction

    def direction(self):
        return self.direction

    def set_last_node(self, nde):
        self.last_node = nde

    def set_current_node(self, nde):
        self.current_node = nde

    def current_node(self):
        return self.current_node

    def set_id(self, id):
        self.original_id = id

    def set_current_d(self, cd):
        self.current_d = cd

    def current_d(self):
        return self.current_d

