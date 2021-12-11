# Course: 
# Author: 
# Assignment: 
# Description:


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> None:
        """
        TODO: Write this implementation
        """
        self.adj_list[v] = []
        
    def add_edge(self, u: str, v: str) -> None:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
        if u in self.adj_list:
            if v in self.adj_list[u]:
                self.adj_list[u].remove(v)
        if v in self.adj_list:
            if u in self.adj_list[v]:
                self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        TODO: Write this implementation
        """
        if v in self.adj_list.keys():
            self.adj_list.pop(v)
        for key in self.adj_list.keys():
            if v in self.adj_list[key]:
                self.adj_list[key].remove(v)

    def get_vertices(self) -> []:
        """
        TODO: Write this implementation
        """
        l = []
        for key in self.adj_list:
            l.append(key)
        return l

    def get_edges(self) -> []:
        """
        TODO: Write this implementation
        """
        result = []
        checklist = []
        for key in self.adj_list:
            for v in self.adj_list[key]:
                if v not in checklist:
                    result.append((key,v))
            checklist.append(key)
        return result

    def is_valid_path(self, path: []) -> bool:
        """
        TODO: Write this implementation
        """
        if len(path) == 0:
            return True
        if path[0] not in self.adj_list:
            return False
        for i in range(1, len(path)):
            if path[i] not in self.adj_list[path[i - 1]]:
                return False
        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
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
        """
        TODO: Write this implementation
        """
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
                

if __name__ == '__main__':
    
    print("\nPDF - method add_vertex() / add_edge example 1")
    print("----------------------------------------------")
    g = UndirectedGraph()
    print(g)

    for v in 'ABCDE':
        g.add_vertex(v)
    print(g)

    g.add_vertex('A')
    print(g)

    for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
        g.add_edge(u, v)
    print(g)


    print("\nPDF - method remove_edge() / remove_vertex example 1")
    print("----------------------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    g.remove_vertex('DOES NOT EXIST')
    g.remove_edge('A', 'B')
    g.remove_edge('X', 'B')
    print(g)
    g.remove_vertex('D')
    print(g)


    print("\nPDF - method get_vertices() / get_edges() example 1")
    print("---------------------------------------------------")
    g = UndirectedGraph()
    print(g.get_edges(), g.get_vertices(), sep='\n')
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    print("\nPDF - method dfs() and bfs() example 1")
    print("--------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = 'ABCDEGH'
    for case in test_cases:
        print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    print('-----')
    for i in range(1, len(test_cases)):
        v1, v2 = test_cases[i], test_cases[-1 - i]
        print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    print("\nPDF - method count_connected_components() example 1")
    print("---------------------------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print(g.count_connected_components(), end=' ')
    print()

    
    print("\nPDF - method has_cycle() example 1")
    print("----------------------------------")
    edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    g = UndirectedGraph(edges)
    test_cases = (
        'add QH', 'remove FG', 'remove GQ', 'remove HQ',
        'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
        'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
        'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
        'add FG', 'remove GE')
    for case in test_cases:
        command, edge = case.split()
        u, v = edge
        g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
        print('{:<10}'.format(case), g.has_cycle())
