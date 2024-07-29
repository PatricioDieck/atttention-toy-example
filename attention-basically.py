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

    def value(self):
        # what do i publicly reveal/broadcast to others?
        return self.wvalue @ self.data


class Graph:

    def __init__(self):
        # make 10 nodes
        self.nodes = [Node() for _ in range(10)]
        # make 40 edges
        randi = lambda: np.random.randint(len(self.nodes))
        self.edges = [[randi(), randi()] for _ in range(40)]

    def run(self):

        updates = []
        for i, n in enumerate(self.nodes):

            # what is this node looking for?
            q = n.query()

            # find all edges that are input to this node
            inputs = [self.nodes[ifrom] for (ifrom, ito) in self.edges if ito == i]
            if len(inputs) == 0:
                continue  # ignore
            # gether their keys, i.e what they hold
            keys = [m.key() for m in inputs]
            # calculate their compatibilities
            scores = [k.dot(q) for k in keys]
            # softmax them so they sum to 1
            scores = np.exp(scores)
            scores = scores / np.sum(scores)
            # gather the appropriate values with a weighted sum
            values = [m.value() for m in inputs]
            update = sum([s * v for s, v in zip(scores, values)])
            updates.append(update)

        for n, u in zip(self.nodes, updates):
            n.data = n.data + u  # residual connection

graph = Graph()

print(graph.edges)

# for i in range(len(graph.nodes)):
    # print(graph.nodes[i].data)

