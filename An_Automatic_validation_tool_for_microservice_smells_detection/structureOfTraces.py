import networkx as nx
import xml.etree.ElementTree as ET


def export_data(graphml_file_path):
    # Parse the GraphML file using ElementTree
    tree = ET.parse(graphml_file_path)
    root = tree.getroot()

    # Create a DiGraph from the GraphML file using NetworkX
    G = nx.DiGraph()
    for node in root.iter('{http://graphml.graphdrawing.org/xmlns}node'):
        G.add_node(node.attrib['id'])
    for edge in root.iter('{http://graphml.graphdrawing.org/xmlns}edge'):
        G.add_edge(edge.attrib['source'], edge.attrib['target'])

    # Find the root node in the graph (i.e., the node with zero in-degree)
    root_nodes = [node for node, degree in G.in_degree() if degree == 0]
    return extract_all_routes(G, root_nodes[0])


def extract_all_routes(graph, root_node):
    # Create a list of all the routes in the graph
    all_routes = []
    # if not nx.is_directed_acyclic_graph(graph):
    #     # If the graph has cycles, extract a single loop
    #     loop = nx.find_cycle(graph)
    #     all_routes.append([node for node, _ in loop])
    # else:
    for node in graph.nodes():
        if node != root_node:
            # all_routes.append(nx.shortest_path(graph, root_node, node))
            paths = nx.all_simple_paths(graph, root_node, node)
            for path in paths:
                all_routes.append(path)

    for route in all_routes:
        for route2 in all_routes:
            if route != route2:
                if route2 == route[:len(route2)]:
                    all_routes.remove(route2)
                elif route == route2[:len(route)]:
                    all_routes.remove(route)
                    break

    # for route in all_routes:
    #     print(route)
    #     print('\n')
    return all_routes
