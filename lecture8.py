# %%
# Licensing Information: You are free to use or extend this file for
# educational purposes provided that (1) you retain this notice, and
# (2) you provide clear attribution to the University of Melbourne,
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# August 2021, derived from material created in January 2020 for
# the same subject

# An annoying Colab issue:
# matplotlib 3.2 seems to be the default, so we tell it to install
# a newer version. This will cause an error when you first run it,
# telling you that you need to restart the runtime. After seeing
# that error choose Runtime -> Restart runtime from the menu above.
# Then execute this part again and things should work OK.

# %%

def DFS(G):
    # G is a graph (adjacency matrix), G is a matrix
    global count
    mark = [0] * len(G)
    count = 0
    for v in range(len(G)): # v indexes nodes of G, v indexes rows of G
    
        if mark[v] == 0:
            DFSExplore(v, G, mark)

def DFSExplore(v, G, mark):
    global count
    # G is a graph (adjacency matrix), G is a matrix
    # v indexes nodes of G, v indexes rows of G
    count = count + 1
    mark[v] = count
    for w in range(len(G)): # w indexes nodes of G, w indexes cols of G
     
        if G[v][w] != 0:
            if mark[w] == 0:
                DFSExplore(w, G, mark)


G = [[0, 1, 0, 1],
     [1, 0, 0, 1],
     [0, 0, 0, 1],
     [1, 1, 1, 0]]
DFS(G)

# %%
# simulate a queue using Python lists
class Queue:
    def __init__(self):
        self._items = []

    def empty(self):
        return (len(self._items) == 0)

    def enqueue(self,v):
        self._items.append(v)

    def dequeue(self):
        h = self._items[0]
        self._items = self._items[1:]
        return h

    def __str__(self):
        return str(self._items)


def BFS(G):
    # G is a matrix, G is a graph (adjacency matrix)
    mark = [0] * len(G)
    count = 0
    Q = Queue()
    for v in range(len(G)): # v indexes rows of G, v indexes nodes of G
        
        if mark[v] == 0:
            count = count + 1
            mark[v] = count
            Q.enqueue(v)
            while not Q.empty():
                
                u = Q.dequeue()
                # u indexes rows of G, u indexes nodes of G
                for w in range(len(G)):
                    # w indexes cols of G, w indexes nodes of G
                    
                    if G[u][w] != 0:
                        if mark[w] == 0:
                            count = count + 1
                            mark[w] = count
                            Q.enqueue(w)


BFS(G)



