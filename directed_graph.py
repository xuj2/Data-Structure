from min_heap import *


class DirectedGraph:
    def __init__(self, start_edges=None):
        self.v_count = 0
        self.adj_matrix = []
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    def add_vertex(self) -> int:
        self.adj_matrix.append([])
        self.v_count += 1;
        for l in self.adj_matrix:
            for i in range(self.v_count):
                if len(l) < self.v_count:
                    l.append(0)
        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        if src < 0 or src >= self.v_count:
            return
        if dst < 0 or dst >= self.v_count:
            return
        if weight <= 0 or src == dst:
            return
        self.adj_matrix[src][dst] = weight
        
        
    def remove_edge(self, src: int, dst: int) -> None:
        if src < 0 or src >= self.v_count:
            return
        if dst < 0 or dst >= self.v_count:
            return
        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        l = []
        for i in range(self.v_count):
            l.append(i)
        return l

    def get_edges(self) -> []:
        l = []
        for i in range(self.v_count):
            for j in range(self.v_count):
                if self.adj_matrix[i][j] != 0:
                    item = i, j, self.adj_matrix[i][j]
                    l.append(item)
        return l

    def is_valid_path(self, path: []) -> bool:
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i+1]
            if self.adj_matrix[a][b] <= 0:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        if v_start < 0 or v_start >= self.v_count:
            return []
        if v_end != None:
            if v_end < 0 or v_end >= self.v_count:
                return []
        visited = []
        stack = [v_start]
        while stack != []:
            v = stack.pop()
            if v not in visited:
                visited.append(v)
            if v == v_end:
                return visited
            add = []
            for i in range(len(self.adj_matrix[v])):
                if self.adj_matrix[v][i] > 0:
                    index = i
                    if index not in visited:
                        add.append(index)
            add.sort(reverse = True)
            for item in add:
                stack.append(item)
        return visited

    def bfs(self, v_start, v_end=None) -> []:
        if v_start < 0 or v_start >= self.v_count:
            return []
        if v_end != None:
            if v_end < 0 or v_end >= self.v_count:
                return []
        visited = []
        queue = [v_start]
        while queue != []:
            v = queue.pop(0)
            if v not in visited:
                visited.append(v)
            if v == v_end:
                return visited
            add = []
            for i in range(len(self.adj_matrix[v])):
                if self.adj_matrix[v][i] > 0:
                    index = i
                    if index not in visited:
                        add.append(index)
            add.sort()
            for item in add:
                queue.append(item)
        return visited

    def has_cycle(self):
        for i in range(self.v_count):
            visited = []
            stack = [i]
            while stack != []:
                v = stack.pop()
                for e in self.adj_matrix[v]:
                    if e > 0:
                        if v not in visited:
                            visited.append(v)
                            break
                for j in range(len(self.adj_matrix[v])):
                    if self.adj_matrix[v][j] > 0:
                        if j in visited:
                            return True
                        else:
                            stack.append(j)
        return False        

    def dijkstra(self, src: int) -> []:
        result = []
        for i in range(self.v_count):
            visited = {}
            q = MinHeap()
            q.add((0, src))
            while q.is_empty() == False:
                d, v = q.remove_min()
                if v == i:
                    result.append(d)
                    break
                if v not in visited.keys():
                    visited[v] = d
                    for j in range(self.v_count):
                        if self.adj_matrix[v][j] > 0:
                            di = self.adj_matrix[v][j]
                            q.add((d + di, j))
            if len(result) <= i:
                result.append(float('inf'))
        return result
