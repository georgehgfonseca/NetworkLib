from graph import Graph

g = Graph()
g.add_node("Bia")
g.add_node("Caio")
g.add_node("Liz")
g.add_node("Alex")

g.add_edge("Caio", "Liz")
g.add_edge("Caio", "Alex")
g.add_edge("Liz", "Caio")
g.add_edge("Alex", "Liz")

g.remove_edge("Bia", "Caio")
print(g)