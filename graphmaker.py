import math
import numpy as np

with open("Elevation.csv") as f:
    ncols = len(f.readline().split(','))

data = np.loadtxt('Elevation.csv', skiprows=1, usecols=range(1, ncols - 1), delimiter=',')


class Graph:
    def __init__(self, graph, x_start, y_start):
        self.graph = graph
        self.x_start = x_start
        self.y_start = y_start
        # cost dict -> [x,y]:{[x,y+1]:cost,[x+1,y+1]:cost}
        self.cost = {}
        for k in range(len(graph)):
            for i in range((len(graph[0]))):
                adj = [[k + 1, i], [k + 1, i + 1], [k, i + 1], [k - 1, i + 1], [k - 1, i], [k - 1, i - 1], [k, i - 1],
                       [k + 1, i - 1]]
                adj = [tuple(x) for x in adj if 0 <= x[0] < len(graph[0]) and 0 <= x[1] < len(graph)]
                to_add = {}
                for neighbour in adj:
                    energy = math.sqrt(((neighbour[0] - k) ** 2) + ((neighbour[1] - i) ** 2)) + max(0, 10 * (self.graph[neighbour[1]][neighbour[0]] - self.graph[i, k]))
                    energy += max(0, 10 * (self.graph[neighbour[1]][neighbour[0]] - self.graph[i, k]))
                    to_add[neighbour] = energy
                self.cost[(k, i)] = to_add

                
g = Graph(data, -80, 130)