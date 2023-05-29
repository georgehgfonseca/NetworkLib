from graph import Graph

# Lesson 1 - Graph creation 
g = Graph()
g.add_node("Bia")
g.add_node("Caio")
g.add_node("Liz")
g.add_node("Alex")

g.add_edge("Caio", "Liz")
g.add_edge("Caio", "Alex")
g.add_edge("Liz", "Caio")
g.add_edge("Alex", "Liz")
print(g)

# Lesson 2 - Degree-related methods
print("Out-degree of node Liz:", g.degree_out("Liz"))
print("In-degree of node Liz:", g.degree_in("Liz"))
print("Highest out-degree:", g.highest_degree_out())
print("Highest in-degree:", g.highest_degree_in())

# Lesson 3 - Graph properties
print("Density:", g.density())
print("Is complete:", g.is_complete())
print("There is edge (Caio, Liz):", g.there_is_edge("Caio", "Liz"))
print("Neighbors of Caio:", g.neighbors("Caio"))
print("Is oriented:", g.is_oriented())
print("Is regular:", g.is_regular())

# Lesson 4 - Graph properties (pt. 2)
print("Complement of g:", g.complement()) 
g2 = Graph()
g2.add_nodes(["Bia", "Caio", "Alex"])
g2.add_two_way_edge("Bia", "Caio")
g2.add_two_way_edge("Alex", "Bia")
print("Is subgraph of g2:", g.is_subgraph_of(g2))

# Lesson 5 - Graph walks 

# Lesson 6 - Graph search

# Lesson 7 - Shortest-path algorithms