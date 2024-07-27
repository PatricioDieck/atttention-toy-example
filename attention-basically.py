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
        return self.wquery @ self.data
    # explain what is happening when we do @ here 
    # we are doing a dot product of the weight matrix and the data vector

    def value(self):
        # what do i publicly reveal/broadcast to others?
        return self.wvalue @ self.data

class Graph :

    def __init__(self):
        # make 10 nodes
        self.nodes = [Node() for _ in range(10)]
        # make 40 edges 
        randi = lambda: np.random.randint(len(self.nodes))
        self.edges = [[randi(), randi()] for _ in range(40)]











n = Node()

print("DATA of node\n", n.data)
print("WKEY of node\n", n.wkey)

print("KEYS node\n", n.key)

key = n.key()
print("COMPUTED KEYS of node\n", key)
