import networkx as nx
from pyvis.network import Network

canvas = Network('650px', '650px')
directedGraph = nx.DiGraph()
directedGraph.add_nodes_from([('Ciudad A', {'color': 'red'}), ('Ciudad B', {'color': 'blue'}), ('Ciudad C', {'color': 'green'})])
directedGraph.add_edges_from([('Ciudad A', 'Ciudad B'), ('Ciudad A', 'Ciudad C')])
canvas.from_nx(directedGraph)
canvas.show('test.html')
