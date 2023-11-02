import networkx as nx
import matplotlib.pyplot as plt


def NoAPIGateway(g):

    # to check if there is a node API Gateway
    api_present = False
    # to check which node is the API Gateway
    api_node = None
    # if it is true there is no path from API Gateway to one of the other nodes
    no_path = False
    # list of nodes that are not connected to the API Gateway
    problematic_nodes = []
    # edge 1 for root extraction
    edges_one = []

    nodes = g.nodes()
    edges = g.edges()

    for node in nodes:
        for edge in edges:
            edges_one.append(edge[1])
        if node not in edges_one:
            api_present = True
            api_node = node

    # to check if there is a path from API Gateway to other nodes
    if api_node != None:
        for node in nodes:
            if node != api_node:
                check_node = node
                if nx.has_path(g, api_node, check_node) == False:
                    no_path = True
                    problematic_nodes.append(check_node)

    if api_present == False:
        print("No API Gateway found")
        return [None, None, True]

    elif api_present == True and no_path == True:
        print("No API Gateway found")
        return [api_node, problematic_nodes, True]

    elif api_present == True and no_path == False and "gateway" not in nodes[api_node]['name'].lower():
        print("No API Gateway found")
        return [api_node, None, True]

    else:
        print("API Gateway found")
        return [api_node, None, False]
