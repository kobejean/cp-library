import cp_library.vis.__header__

def plot_graph(G):
    N = len(G)
    import networkx as nx
    import matplotlib.pyplot as plt
    # Create NetworkX graph
    graph = nx.Graph()

    # Add edges to the graph
    for u in range(N):
        for e in G[u]:
            if isinstance(e, tuple):
                v, w = e
                graph.add_edge(u, v, weight=w)
            else:
                graph.add_edge(u, e)

    # Set up the plot
    plt.figure(figsize=(12, 8))

    # Create a layout for the graph
    pos = nx.spring_layout(graph)

    # Draw the graph
    nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_edges(graph, pos)
    nx.draw_networkx_labels(graph, pos)

    # Draw edge labels
    edge_labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

    # Set title and display the plot
    plt.title("Graph Visualization")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
