from datetime import datetime
import networkx as nx


def jsonConverter(traces, path):
    g = nx.read_graphml(path)
    nested_list = []
    db_node = None
    db_list = []
    number = 0

    for edge in g.edges():
        if g.edges[edge]['isDB'] != False:
            db_node = edge[1]
            db_list.append(g.nodes[edge[1]]['name'])

    for trace in traces:
        nodes = []
        number += 1
        for node in trace:
            nodes.append(g.nodes[node])
        now = datetime.now().timestamp() * 1000000
        now_int = int(now)

        # Add the parent to each node
        for node in nodes:
            if node != nodes[0]:
                node['parent'] = nodes[nodes.index(node) - 1]['name'] + '_id'
            else:
                node['parent'] = nodes[nodes.index(node)]['name'] + '_id'

        # Convert the nodes into a nested list
        node_list = [{
            'traceId': "trace"+str(number),
            'parentId': node['parent'],
            'id': node['name'] + '_id',
            'timestamp': now_int,
            'duration': 377,
            'localEndpoint': {
                **({'serviceName': node['name']} if 'name' in node else {}),
                **({'ipv4': node['ip']} if 'ip' in node else {}),
                **({'port': node['port']} if 'port' in node else {}),
            },
            **({'remoteEndpoint': {**({'serviceName': nodes[nodes.index(node)+1]['name'], } if 'name' in node else {}), **({'ipv4': nodes[nodes.index(node)+1]['ip']} if 'ip' in node else {}), **({'port': nodes[nodes.index(node)+1]['port']} if 'port' in node else {}), }}if nodes.index(node)+1 < len(nodes) and nodes[nodes.index(node)+1]['name'] in db_list else {}),
            **({'tags': {'db.system': nodes[nodes.index(node)+1]['name']}} if nodes.index(node)+1 < len(nodes) and nodes[nodes.index(node)+1]['name'] in db_list else {}),
        } for node in nodes if node['name'] not in db_list]

        # Add the nested list to the main list
        nested_list.append(node_list)

    return nested_list
