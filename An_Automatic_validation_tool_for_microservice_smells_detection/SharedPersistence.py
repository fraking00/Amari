import networkx as nx
import matplotlib.pyplot as plt


def SharedPersistence(g):

    nodes = g.nodes()
    edges = g.edges()

    # list of nodes that are connected to the database
    node_connections = []
    # to check if there is a node database
    db_present = False
    # to check which node is the database
    db_node = None

    # list of nodes that are problematic
    problematic_nodes = []

    for edge in edges:

        # to check if there is a node database
        if edges[edge]['isDB'] != False:
            db_node = edge[1]
            db_present = True

    if db_present == True:

        for edge in edges:

            if edge[1] == db_node:
                node_connections.append(edge[0])

        if node_connections != []:
            for node in node_connections:
                node_connections.remove(node)
                if node_connections != []:
                    for node2 in node_connections:
                        if nodes[node]["name"] != nodes[node2]["name"]:
                            problematic_nodes.append(node)
                            problematic_nodes.append(node2)

        if problematic_nodes != []:
            print("there are problematic nodes")
            return [db_node, problematic_nodes]

        elif problematic_nodes == [] and db_node != None:
            print("There are no problematic nodes")
            return [db_node, None]

        else:
            print("There is no database")
            return [None, None]
