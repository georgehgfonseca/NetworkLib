class WeightedGraph:
    
    def __init__(self) -> None:
        self.adj_list = {}
        self.node_count = 0
        self.edge_count = 0

    def add_node(self, node):
        if node in self.adj_list:
            print(f"WARN: Node {node} already exists")
            return
        self.adj_list[node] = {}
        self.node_count += 1

    def add_edge(self, node1, node2, weight):
        if node1 not in self.adj_list:
            self.add_node(node1)
        if node2 not in self.adj_list:
            self.add_node(node2)
        self.adj_list[node1][node2] = weight
        self.edge_count += 1

    def add_nodes(self, nodes):
        for node in nodes:
            self.add_node(node)

    def add_two_way_edge(self, node1, node2, weight):
        self.add_edge(node1, node2, weight)
        self.add_edge(node2, node1, weight)

    def remove_edge(self, node1, node2):
        try:
          self.adj_list[node1].pop(node2)
          self.edge_count -= 1
        except KeyError as e:
            print(f"WARN: Edge {node1} -> {node2} does not exist")

    def __str__(self):
        output = ""
        for node in self.adj_list:
            output += str(node) + " -> " + str(self.adj_list[node]) + "\n"
        return output
    
    def read_file(self, file_name):
        file = open(file_name, 'r')
        i = 0
        for line in file:
            i += 1
            if i == 1:
                continue
            line_content = line.strip().split(" ")
            u = line_content[0]
            v = line_content[1]
            w = int(line_content[2])
            self.add_edge(u, v, w)
        file.close()

    def remove_node(self, node):
        for node2 in self.adj_list:
            if node in self.adj_list[node2]:
                self.adj_list[node2].pop(node)
                self.edge_count -= 1
        self.edge_count -= len(self.adj_list[node])
        self.node_count -= 1
        self.adj_list.pop(node)

    def bellman_ford(self, s):
        dist = {}
        pred = {}
        for node in self.adj_list:
            dist[node] = float('inf')
            pred[node] = None
        dist[s] = 0
        for i in range(self.node_count - 1):
            for u in self.adj_list:
                for v in self.adj_list[u]:
                    w = self.adj_list[u][v]
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
        return (dist, pred)

    def bellman_ford_improved(self, s):
        dist = {}
        pred = {}
        for node in self.adj_list:
            dist[node] = float('inf')
            pred[node] = None
        dist[s] = 0
        for i in range(self.node_count - 1):
            swapped = False
            for u in self.adj_list:
                for v in self.adj_list[u]:
                    w = self.adj_list[u][v]
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        pred[v] = u
                        swapped = True
            if not swapped:
                break
        return (dist, pred)


