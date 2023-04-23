from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree(tree, node_value):
    node = Node(node_value)
    for child_value in tree[node_value]:
        node.children.append(build_tree(tree, child_value))
    return node


def draw_tree(node, graph):
    for child in node.children:
        graph.add_edge(node.value, child.value)
        draw_tree(child, graph)


def parentToedges(p, d):
    edges = []
    weighted_edges = []
    for i in range(len(p)):
        if (p[i] == 's' and i < len(p)-1):
            root = str(i)
            i=+1
        if (p[i] == 's' and i == len(p) - 1):
            root = str(i)
            break
        edges.append((str(p[i]), str(i)))
        weighted_edges.append((str(p[i]), str(i), d[i]))
    #print(edges,weighted_edges)
    return root, edges, weighted_edges


def dijkstraTree_draw(p, d):
    root, edges, weighted_edges = parentToedges(p, d)
    tree = defaultdict(list)

    for parent, child in edges:
        tree[parent].append(child)

    source = build_tree(tree, root)
    G = nx.DiGraph()
    draw_tree(source, G)
    G.add_weighted_edges_from(weighted_edges)
    nx.draw_circular(G, with_labels=True, node_color='lightblue', node_size=1200, font_size=15)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    pos = nx.circular_layout(G)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=15)
    plt.show()
