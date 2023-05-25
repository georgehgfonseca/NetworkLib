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

print("Out-degree of node Liz:", g.degree_out("Liz"))
print("In-degree of node Liz:", g.degree_in("Liz"))
print("Highest out-degree:", g.highest_degree_out())
print("Highest in-degree:", g.highest_degree_in())
print(g)