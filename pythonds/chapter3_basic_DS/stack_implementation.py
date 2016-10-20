

class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "< %s >" % ','.join([str(i) for i in self.items])

    def __contains__(self, item):
        return item in self.items
