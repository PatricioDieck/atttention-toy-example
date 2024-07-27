import numpy as np


class Node:

    def __init__(self):

        # the vector is stored at this node
        self.data = np.random.randn(20)

        # weights governing how this node interacts w others
        self.wkey = np.random.randn(20, 20)
        self.wquery = np.random.randn(20, 20)
        self.wvalue = np.random.randn(20, 20)

    def key(self):
        # what do i have?
        return self.wkey @ self.data

    def query(self):
        # what am i looking for?
        return self.query @ self.data

    def value(self):
        # what do i publicly reveal/broadcast to others?
        return self.value @ self.data


n = Node()

print("DATA of node\n", n.data)

print("KEYS node\n", n.key)

key = n.key()
print("COMPUTED KEYS of node\n", key)
