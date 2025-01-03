---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "'''\n\u257A\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\
    \u2578\n             https://kobejean.github.io/cp-library               \n'''\n\
    \ndef plot_graph(G):\n    N = len(G)\n    import networkx as nx\n    import matplotlib.pyplot\
    \ as plt\n    # Create NetworkX graph\n    graph = nx.Graph()\n\n    # Add edges\
    \ to the graph\n    for u in range(N):\n        for e in G[u]:\n            if\
    \ isinstance(e, tuple):\n                v, w = e\n                graph.add_edge(u,\
    \ v, weight=w)\n            else:\n                graph.add_edge(u, e)\n\n  \
    \  # Set up the plot\n    plt.figure(figsize=(12, 8))\n\n    # Create a layout\
    \ for the graph\n    pos = nx.spring_layout(graph)\n\n    # Draw the graph\n \
    \   nx.draw_networkx_nodes(graph, pos, node_color='lightblue', node_size=500)\n\
    \    nx.draw_networkx_edges(graph, pos)\n    nx.draw_networkx_labels(graph, pos)\n\
    \n    # Draw edge labels\n    edge_labels = nx.get_edge_attributes(graph, 'weight')\n\
    \    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)\n\n   \
    \ # Set title and display the plot\n    plt.title(\"Graph Visualization\")\n \
    \   plt.axis('off')\n    plt.tight_layout()\n    plt.show()\n"
  code: "import cp_library.vis.__header__\n\ndef plot_graph(G):\n    N = len(G)\n\
    \    import networkx as nx\n    import matplotlib.pyplot as plt\n    # Create\
    \ NetworkX graph\n    graph = nx.Graph()\n\n    # Add edges to the graph\n   \
    \ for u in range(N):\n        for e in G[u]:\n            if isinstance(e, tuple):\n\
    \                v, w = e\n                graph.add_edge(u, v, weight=w)\n  \
    \          else:\n                graph.add_edge(u, e)\n\n    # Set up the plot\n\
    \    plt.figure(figsize=(12, 8))\n\n    # Create a layout for the graph\n    pos\
    \ = nx.spring_layout(graph)\n\n    # Draw the graph\n    nx.draw_networkx_nodes(graph,\
    \ pos, node_color='lightblue', node_size=500)\n    nx.draw_networkx_edges(graph,\
    \ pos)\n    nx.draw_networkx_labels(graph, pos)\n\n    # Draw edge labels\n  \
    \  edge_labels = nx.get_edge_attributes(graph, 'weight')\n    nx.draw_networkx_edge_labels(graph,\
    \ pos, edge_labels=edge_labels)\n\n    # Set title and display the plot\n    plt.title(\"\
    Graph Visualization\")\n    plt.axis('off')\n    plt.tight_layout()\n    plt.show()\n"
  dependsOn: []
  isVerificationFile: false
  path: cp_library/vis/plot_graph_weighted_fn.py
  requiredBy: []
  timestamp: '2025-01-03 12:10:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: cp_library/vis/plot_graph_weighted_fn.py
layout: document
redirect_from:
- /library/cp_library/vis/plot_graph_weighted_fn.py
- /library/cp_library/vis/plot_graph_weighted_fn.py.html
title: cp_library/vis/plot_graph_weighted_fn.py
---
