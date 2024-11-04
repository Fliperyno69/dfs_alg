class Graph:
    def __init__(self):
        self.graph = {} # reprezentace grafu ve slovníku

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start):
        visited = []
        stack = [start]
        # TODO: zjistit proc funguje ten ext v revu
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.append(vertex)
                stack.extend(reversed(self.graph.get(vertex, [])))
        return visited

# usecase:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 5)

print("DFS pořadí:", g.dfs(1))
