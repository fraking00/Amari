import networkx as nx
import matplotlib.pyplot as plt


def modifyNode(g, path):

    adding = True

    while adding:

        nodes = g.nodes()
        edges = g.edges()

        print("Nodes: ", nodes)
        print("Edges: ", edges)
        nx.draw(g, with_labels=True)
        plt.show()

        first_choice = input(
            "Do you want to add/delete/modify a node/edge? (y/n) (n to exit)")

        # add a new node
        if first_choice == "y":

            second_choice = input(
                "Do you want to add a node or an edge or delete a node or an edge or modify a node or an edge? (an/ae/dn/de/mn/me)")

            # add a new node
            if second_choice == "an":
                node_id = input("Enter the ID of the node: ")
                node_name = input("Enter the name of the node: ")
                node_label = input("Enter the label of the node: ")
                if node_id not in nodes:
                    g.add_node(node_id)
                    g.nodes[node_id]["name"] = node_name
                    g.nodes[node_id]["labelV"] = node_label
                else:
                    print("The node already exists")

            # add a new edge
            elif second_choice == "ae":
                first_node = input("Enter the name of the first node: ")
                second_node = input("Enter the name of the second node: ")

                if first_node not in nodes:
                    g.add_node(first_node)
                    fnode_name = input("Enter the name of the node: ")
                    fnode_label = input("Enter the label of the node: ")
                    g.nodes[first_node]["name"] = fnode_name
                    g.nodes[first_node]["labelV"] = fnode_label

                if second_node not in nodes:
                    g.add_node(second_node)
                    snode_name = input("Enter the name of the node: ")
                    snode_label = input("Enter the label of the node: ")
                    g.nodes[second_node]["name"] = snode_name
                    g.nodes[second_node]["labelV"] = snode_label

                g.add_edge(first_node, second_node)
                g.edges[first_node, second_node]["labelE"] = "calls"
                weight = input("Enter the weight of the edge: ")
                g.edges[first_node, second_node]["weight"] = weight
                isDB = input("Is the edge a DB edge? (y/n)")
                if isDB == "y":
                    g.edges[first_node, second_node]["isDB"] = True
                else:
                    g.edges[first_node, second_node]["isDB"] = False

            # delete a node
            elif second_choice == "dn":
                node_name = input("Enter the name of the node: ")
                if node_name in nodes:
                    g.remove_node(node_name)
                else:
                    print("The node doesn't exist")

            # delete an edge
            elif second_choice == "de":
                first_node = input("Enter the name of the first node: ")
                second_node = input("Enter the name of the second node: ")
                if (first_node, second_node) in edges:
                    g.remove_edge(first_node, second_node)
                else:
                    print("The edge doesn't exist")

            # modify a node
            elif second_choice == "mn":
                change_type = input(
                    "Do you want to change the name or the label of the node or the ID or all of them? (n/l/i/a)")
                if change_type == "n":
                    node_name = input("Enter the name of the node: ")
                    if node_name in nodes:
                        new_name = input("Enter the new name of the node: ")
                        g.nodes[node_name]["name"] = new_name
                    else:
                        print("The node doesn't exist")

                elif change_type == "l":
                    node_name = input("Enter the name of the node: ")
                    if node_name in nodes:
                        new_label = input("Enter the new label of the node: ")
                        g.nodes[node_name]["labelV"] = new_label
                    else:
                        print("The node doesn't exist")

                elif change_type == "i":
                    node_name = input("Enter the name of the node: ")
                    if node_name in nodes:
                        new_id = input("Enter the new ID of the node: ")
                        g = nx.relabel_nodes(g, {node_name: new_id})
                    else:
                        print("The node doesn't exist")

                elif change_type == "a":
                    node_name = input("Enter the name of the node: ")
                    if node_name in nodes:
                        new_id = input("Enter the new ID of the node: ")
                        new_name = input("Enter the new name of the node: ")
                        new_label = input("Enter the new label of the node: ")
                        g = nx.relabel_nodes(g, {node_name: new_id})
                        g.nodes[new_id]["name"] = new_name
                        g.nodes[new_id]["labelV"] = new_label
                    else:
                        print("The node doesn't exist")

            # modify an edge
            elif second_choice == "me":
                first_node = input("Enter the ID of the first node: ")
                second_node = input("Enter the ID of the second node: ")
                if (first_node, second_node) in edges:
                    change = input(
                        "Do you want to change the first node or the second node or both? (f/s/b)")
                    if change == "f":
                        new_first_node = input(
                            "Enter the new ID of the first node: ")
                        g.remove_edge(first_node, second_node)
                        if new_first_node not in nodes:
                            g.add_node(new_first_node)
                            fnode_name = input(
                                "Enter the name of the node: ")
                            fnode_label = input(
                                "Enter the label of the node: ")
                            g.nodes[new_first_node]["name"] = fnode_name
                            g.nodes[new_first_node]["labelV"] = fnode_label
                        g.add_edge(new_first_node, second_node)
                    elif change == "s":
                        new_second_node = input(
                            "Enter the new ID of the second node: ")
                        g.remove_edge(first_node, second_node)
                        if new_second_node not in nodes:
                            g.add_node(new_second_node)
                            snode_name = input(
                                "Enter the name of the node: ")
                            snode_label = input(
                                "Enter the label of the node: ")
                            g.nodes[new_second_node]["name"] = snode_name
                            g.nodes[new_second_node]["labelV"] = snode_label
                            g.add_edge(first_node, new_second_node)
                            g.edges[first_node,
                                    new_second_node]["labelE"] = "calls"
                            weight = input("Enter the weight of the edge: ")
                            g.edges[first_node,
                                    new_second_node]["weight"] = weight
                            isDB = input("Is the edge a DB edge? (y/n)")
                            if isDB == "y":
                                g.edges[first_node,
                                        new_second_node]["isDB"] = True
                            else:
                                g.edges[first_node,
                                        new_second_node]["isDB"] = False

                    elif change == "b":
                        new_first_node = input(
                            "Enter the new ID of the first node: ")
                        new_second_node = input(
                            "Enter the new ID of the second node: ")
                        g.remove_edge(first_node, second_node)
                        if new_first_node not in nodes:
                            g.add_node(new_first_node)
                            fnode_name = input(
                                "Enter the name of the node: ")
                            fnode_label = input(
                                "Enter the label of the node: ")
                            g.nodes[new_first_node]["name"] = fnode_name
                            g.nodes[new_first_node]["labelV"] = fnode_label
                        if new_second_node not in nodes:
                            g.add_node(new_second_node)
                            snode_name = input(
                                "Enter the name of the node: ")
                            snode_label = input(
                                "Enter the label of the node: ")
                            g.nodes[new_second_node]["name"] = snode_name
                            g.nodes[new_second_node]["labelV"] = snode_label
                        g.add_edge(new_first_node, new_second_node)
                        g.edges[new_first_node,
                                new_second_node]["labelE"] = "calls"
                        weight = input("Enter the weight of the edge: ")
                        g.edges[new_first_node,
                                new_second_node]["weight"] = weight
                        isDB = input("Is the edge a DB edge? (y/n)")
                        if isDB == "y":
                            g.edges[new_first_node,
                                    new_second_node]["isDB"] = True
                        else:
                            g.edges[new_first_node,
                                    new_second_node]["isDB"] = False
                else:
                    print("The edge doesn't exist")

        elif first_choice == "n":

            nx.write_graphml(g, path)
            adding = False
            return g
