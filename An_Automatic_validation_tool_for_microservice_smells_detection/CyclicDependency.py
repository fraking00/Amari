import networkx as nx
import matplotlib.pyplot as plt


def CyclicDependency(g):

    # presence of a cycle
    cycle = False
    # list of nodes that are part of a cycle
    problematic_lists = []
    # list of nodes that are part of a cycle
    cycleList = []

    nodes = g.nodes()
    edges = g.edges()

    # to check if there is a cycle
    if nx.is_directed_acyclic_graph(g) == False:
        cycle = True

    # to check how many cycles there are
    if cycle == True:
        cycleList = nx.find_cycle(g)

        # to check which nodes are part of a cycle
        for i in cycleList:
            problematic_lists.append(i)

    return [cycle, problematic_lists]
