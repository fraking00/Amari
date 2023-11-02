import networkx as nx
import matplotlib.pyplot as plt
import json
from NoAPIGateway import NoAPIGateway
from graphModifier import modifyNode
from SharedPersistence import SharedPersistence
from CyclicDependency import CyclicDependency
from jsonConverterByTraces import jsonConverter
from structureOfTraces import export_data

path_name = input("Insert the folder in which is the graphml: ")
path = "../JsonPerTesting/newTest/" + path_name + "/graph.graphml"
g = nx.read_graphml(path)

searching = True
modify = False

while searching:

    nodes = g.nodes()
    edges = g.edges()

    ngadata = []

    print("Nodes: ", nodes)
    print("Edges: ", edges)
    nx.draw(g, with_labels=True)
    plt.show()

    first_choice = input(
        "What do you want to check in the graph? (nga(No Gataway API), sp(Shared Persistance), cd(Cyclic Dependency), e(exit))")

    # check if there is a No Gateway API
    if first_choice == "nga":
        ngadata = NoAPIGateway(g)

        if ngadata[2] == True:
            print("root node: ", g.nodes[ngadata[0]]['name'])
            print("root id: " + ngadata[0])
            print("Problematic nodes: ", ngadata[1])
            forth_choise = input(
                "Do you want to add one or modify the graph? (y/n)")
            if forth_choise == "y":
                searching = False
                modify = True
            else:
                searching = True

        else:
            print("There is a Gateway API")
            print("Gateway API node: ", g.nodes[ngadata[0]]['name'])
            print("Gateway id: " + ngadata[0])
            searching = True

    # check if there is a Shared Persistence
    elif first_choice == "sp":
        spdata = SharedPersistence(g)

        if spdata[0] != None and spdata[1] != None:
            print("There is a Shared Persistence")
            print("Database node: ", g.nodes[spdata[0]]['name'])
            print("Database id: " + spdata[0])
            print("Problematic nodes: ", spdata[1])
            second_choice = input(
                "Do you want to modify the problematic nodes? (y/n)")
            if second_choice == "y":
                searching = False
                modify = True
            else:
                searching = True
        else:
            print("There is no Shared Persistence")
            searching = True

    # check if there is a Cyclic Dependency
    elif first_choice == "cd":
        cdData = CyclicDependency(g)

        if cdData[0] == True:
            print("There is a Cyclic Dependency")
            print("Problematic nodes: ", cdData[1])
            second_choice = input(
                "Do you want to modify the problematic nodes? (y/n)")
            if second_choice == "y":
                searching = False
                modify = True
            else:
                searching = True
        else:
            print("There is no Cyclic Dependency")
            searching = True

    else:
        searching = False
        file_name = input("Insert the name of the file: ")
        traces = export_data(path)
        json_data = jsonConverter(traces, path)
        with open(file_name + ".json", "w") as outfile:
            json.dump(json_data, outfile)
        break

while modify:

    g = modifyNode(g, path)

    third_choice = input("Do you want to modify it again? (y/n)")
    if third_choice == "y":
        modify = True
    else:
        modify = False
        file_name = input("Insert the name of the file: ")
        traces = export_data(path)
        json_data = jsonConverter(traces, path)
        with open(file_name + ".json", "w") as outfile:
            json.dump(json_data, outfile)
