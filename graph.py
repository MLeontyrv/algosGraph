class Graph:
    def __init__(self):
        self.vertexes = []
        self.adjacency_list = {}

    def print_adjacency_list(self):
        if not self.vertexes:
            return []
        result = {}
        for vertex in self.vertexes:
            result[vertex] = []
            for edge in self.adjacency_list[vertex]:
                result[vertex].append(edge[0])
        print("Список смежности\nвершина: смежная вершина")
        for key, value in result.items():
            print(f"{key}: {', '.join(value)}")

    def first(self, v):
        if v not in self.adjacency_list:
            return None
        return list(self.adjacency_list[v])[0]

    def next(self, v, i):
        if v not in self.adjacency_list:
            return None
        if i == len(self.adjacency_list[v]) - 1:
            return None
        return list(self.adjacency_list[v])[i + 1]

    def vertex(self, v, i):
        if v not in self.adjacency_list:
            raise ValueError(f"Вершина {v} не существует")
        if i >= len(self.adjacency_list[v]):
            raise ValueError(f"Индекс {i} выходит за границы списка смежности вершины {v}")
        return list(self.adjacency_list[v])[i]

    def add_v(self, name, label=None, mark=None):
        if name in self.vertexes:
            raise ValueError(f"Вершина с именем {name} уже существует")
        self.vertexes.append(name)
        self.adjacency_list[name] = []
        if label is not None:
            self.vertexes[-1] = label
        if mark is not None:
            self.vertexes[-1] = mark

    def add_e(self, v1, v2, c):
        if v1 not in self.vertexes:
            raise ValueError(f"Вершина {v1} не существует")
        if v2 not in self.vertexes:
            raise ValueError(f"Вершина {v2} не существует")
        self.adjacency_list[v1].append((v2, c))
        self.adjacency_list[v2].append((v1, c))

    def del_v(self, v):
        if v not in self.vertexes:
            raise ValueError(f"Вершина {v} не существует")
        for vertex in self.vertexes:
            if v in self.adjacency_list[vertex]:
                self.adjacency_list[vertex].remove(v)
        del self.vertexes[self.vertexes.index(v)]
        del self.adjacency_list[v]

    def del_e(self, v1, v2):
        if v1 not in self.vertexes:
            raise ValueError(f"Вершина {v1} не существует")
        if v2 not in self.vertexes:
            raise ValueError(f"Вершина {v2} не существует")
        self.adjacency_list[v1].remove((v2, None))
        self.adjacency_list[v2].remove((v1, None))

    def edit_v(self, v, new_label=None, new_mark=None):
        if v not in self.vertexes:
            raise ValueError(f"Вершина {v} не существует")
        if new_label is not None:
            self.vertexes[self.vertexes.index(v)] = new_label
        if new_mark is not None:
            self.vertexes[self.vertexes.index(v)] = new_mark

    def edit_e(self, v1, v2, new_c):
        if v1 not in self.vertexes:
            raise ValueError(f"Вершина {v1} не существует")
        if v2 not in self.vertexes:
            raise ValueError(f"Вершина {v2} не существует")
        for edge in self.adjacency_list[v1]:
            if edge[0] == v2:
                edge[1] = new_c
                break
        for edge in self.adjacency_list[v2]:
            if edge[0] == v1:
                edge[1] = new_c
                break