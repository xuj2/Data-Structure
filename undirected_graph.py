class UndirectedGraph:
    def __init__(self, start_edges=None):
        self.adj_list = dict()
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    def add_vertex(self, v: str) -> None:
        self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        if u == v:
            return
        if u not in self.adj_list:
            self.adj_list[u] = []
        if v not in self.adj_list:
            self.adj_list[v] = []
        if v not in self.adj_list[u]:
            if v != u:
                self.adj_list[u].append(v)
        if u not in self.adj_list[v]:
            if v != u:
                self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        if u in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
        if v in self.adj_list:
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        if v in self.adj_list.keys():
            self.adj_list.pop(v)
        for key in self.adj_list.keys():
            if v in self.adj_list[key]:
                self.adj_list[key].remove(v)

    def get_vertices(self) -> []:
        l = []
        for key in self.adj_list:
            l.append(key)
        return l

    def get_edges(self) -> []:
        result = []
        checklist = []
        for key in self.adj_list:
            for v in self.adj_list[key]:
                if v not in checklist:
                    result.append((key,v))
            checklist.append(key)
        return result

    def is_valid_path(self, path: []) -> bool:
        if len(path) == 0:
            return True
        if path[0] not in self.adj_list:
            return False
        for i in range(1, len(path)):
            if path[i] not in self.adj_list[path[i - 1]]:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        if v_start not in self.adj_list.keys():
            return []
        result = []
        stack = [v_start]
        while stack != []:
            v = stack.pop()
            if v not in result:
                result.append(v)
            if v == v_end:
                return result
            l = self.adj_list[v]
            l.sort(reverse = True)
            for key in l:
                if key not in result:
                    stack.append(key)
        return result

    def bfs(self, v_start, v_end=None) -> []:
        if v_start not in self.adj_list.keys():
            return []
        result = []
        queue = [v_start]
        while queue != []:
            v = queue.pop(0)
            if v not in result:
                result.append(v)
            if v == v_end:
                return result
            l = self.adj_list[v]
            l.sort()
            for key in l:
                if key not in result:
                    queue.append(key)
        return result

    def count_connected_components(self):
        l = []
        for v in self.adj_list:
            comp = self.bfs(v)
            comp.sort()
            l.append(comp)
        count = 0
        check = []
        for component in l:
            if component not in check:
                check.append(component)
                count += 1
        return count

    def has_cycle(self):
        prev = None
        for key in self.adj_list:
            visited = []
            stack = [key]
            desc = []
            while stack != []:
                v = stack.pop()
                for value in self.adj_list[v]:
                    if value in visited:
                        if value != prev:
                            return True
                    else:
                        stack.append(value)
                        desc.append(v)
                if v not in visited:
                    visited.append(v)
                if desc != []:
                    prev = desc.pop()
                else:
                    prev = key
        return False
