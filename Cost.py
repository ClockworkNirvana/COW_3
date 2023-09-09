import math
import numpy as np

with open("Elevation.csv") as f:
    ncols = len(f.readline().split(','))

data = np.loadtxt('Elevation.csv', skiprows=1, usecols=range(1, ncols - 1), delimiter=',')


def to_num(tup):
    return tup[0] * 241 + tup[1]


def to_tup(num):
    return tuple([int(math.floor(num / 241)), int(num % 241)])

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
                    energy = math.sqrt(((neighbour[0] - k) ** 2) + ((neighbour[1] - i) ** 2))
                    energy += max(0, 10 * (self.graph[neighbour[1]][neighbour[0]] - self.graph[i, k]))
                    to_add[neighbour] = energy
                self.cost[(k, i)] = to_add


# Python3 implementation to find the
# shortest path in a directed
# graph from source vertex to
# the destination vertex
class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


infi = 1000000000;

# Class of the node
class Node:

    # Adjacency list that shows the
    # vertexNumber of child vertex
    # and the weight of the edge
    def __init__(self, vertexNumber:tuple):
        self.vertexNumber = vertexNumber
        self.children = []

    # Function to add the child for
    # the given node
    def Add_child(self, vNumber, length):
        p = Pair(vNumber, length);
        self.children.append(p);


# Function to find the distance of
# the node from the given source
# vertex to the destination vertex
def dijkstraDist(g, s, path):
    # Stores distance of each
    # vertex from source vertex
    dist = [infi for i in range(len(g))]

    # bool array that shows
    # whether the vertex 'i'
    # is visited or not
    visited = [False for i in range(len(g))]

    for i in range(len(g)):
        path[i] = -1
    dist[s] = 0;
    path[s] = -1;
    current = s;

    # Set of vertices that has
    # a parent (one or more)
    # marked as visited
    sett = set()
    while (True):

        # Mark current as visited
        visited[current] = True;
        for i in range(len(g[current].children)):
            v = g[current].children[i].first;
            if (visited[v]):
                continue;

            # Inserting into the
            # visited vertex
            sett.add(v);
            alt = dist[current] + g[current].children[i].second;

            # Condition to check the distance
            # is correct and update it
            # if it is minimum from the previous
            # computed distance
            if (alt < dist[v]):
                dist[v] = alt;
                path[v] = current;
        if current in sett:
            sett.remove(current);
        if (len(sett) == 0):
            break;

        # The new current
        minDist = infi;
        index = 0;

        # Loop to update the distance
        # of the vertices of the graph
        for a in sett:
            if (dist[a] < minDist):
                minDist = dist[a];
                index = a;
        current = index;
    return dist;


# Function to print the path
# from the source vertex to
# the destination vertex
def printPath(path, i, s):
    if (i != s):

        # Condition to check if
        # there is no path between
        # the vertices
        if (path[i] == -1):
            print("Path not found!!");
            return;
        printPath(path, path[i], s);
        print(path[i] + " ");


# Driver Code
if __name__ == '__main__':

    g = Graph(data, -80, 130)
    v = []
    s = (80, 130)

    # Loop to create the nodes
    for b in g.cost.keys():
        a = Node(to_num(b))
        v.append(a)

    for b in g.cost:
        d = g.cost[b]
        for n in d:
            v[to_num(b)].Add_child(to_num(n), d[n])

    path = [0 for i in range(len(v))]
    dist = dijkstraDist(v, to_num(s), path)

    # Loop to print the distance of
    # every node from source vertex
    for i in range(len(dist)):
        if dist[i] == infi:
            print("{0} and {1} are not " +
                  "connected".format(i, s))
            continue
        print("Distance of vertex{} from source vertex {} is: {}".format(
            to_tup(i), s, dist[i]))

    # This code is contributed by pratham76


g = Graph(data, -80, 130)
