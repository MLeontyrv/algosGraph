# Список смежности
# Методом обхода в глубину вычислить цикломатическую сложность графа
from graph import Graph

VERTEXES_NAMES: list[str] = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H"
]
EDGES: list[list[str, str, int]] = [
    ["B", "G", 1],
    ["B", "E", 2],
    ["B", "F", 4],
    ["C", "H", 7],
    ["C", "B", 9],
    ["D", "E", 3],
    ["D", "H", 5],
    ["D", "A", 6],
    ["E", "F", 0],
    ["H", "A", 4],
    ["H", "F", 2],
]


def __init_graph():
    g = Graph()
    for vertex in VERTEXES_NAMES:
        g.add_v(vertex)
    for edge in EDGES:
        g.add_e(edge[0], edge[1], edge[2])
    return g


def cyclomatic_complexity_dfs(graph1):
    # Инициализация переменных.
    cc = 1
    visited = set()

    # Вызов рекурсивной функции обхода в глубину.
    def dfs(vertex):
        # Пометить вершину как посещенную.
        visited.add(vertex)

        # Обработать все смежные вершины.
        for neighbor, _ in graph1.adjacency_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor)

        # Если вершина имеет исходящие ребра, то увеличить цикломатическую сложность.
        if graph1.adjacency_list[vertex]:
            cc += 1

    # Выполнение обхода в глубину.
    dfs(graph1.vertices[0])

    # Возвращение цикломатической сложности графа.
    return cc


def compute_cyclomatic_complexity(graph1):
    # Инициализируем состояния вершин.
    visited = [0] * len(graph1.vertices)

    # Запускаем обход в глубину из произвольной вершины.
    for vertex in range(len(graph1.vertices)):
        if visited[vertex] == 0:
            depth_first_search(graph1, vertex, visited)

    # Подсчитываем количество ребер, по которым были найдены циклы.
    return sum(visited)


def depth_first_search(graph1, vertex, visited):
    # Отмечаем вершину как посещенную.
    visited[vertex] = 1

    # Для каждой исходящей из текущей вершины ребре...
    for neighbor in graph1.adjacency_list[vertex]:
        # Если соседняя вершина не была посещена, то запускаем обход в глубину из нее.
        if visited[neighbor] == 0:
            depth_first_search(graph1, neighbor, visited)
        # Если соседняя вершина была посещена, то проверяем, является ли она предком текущей вершины.
        elif visited[neighbor] == 1:
            # Если соседняя вершина является предком текущей вершины, то это означает, что мы нашли цикл.
            visited[vertex] = 2


if __name__ == '__main__':
    graph = __init_graph()

    # graph.print_adjacency_list()
    # print(compute_cyclomatic_complexity(graph))
    print(graph.adjacency_list)