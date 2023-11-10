# Список смежности
# Методом обхода в глубину вычислить цикломатическую сложность графа
from graph import Graph

# VERTEXES_NAMES: list[str] = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F",
#     "G",
#     "H"
# ]
# EDGES: list[list[str, str, int]] = [
#     ["A", "C", 1],
#     ["A", "B", 1],
#     ["A", "D", 1],
#     ["B", "D", 1],
#     ["B", "E", 1],
#     ["B", "F", 1],
#     ["C", "G", 1],
#     ["C", "E", 1],
#     ["D", "H", 1],
#     ["E", "H", 1],
#     ["F", "H", 1],
#
# ]

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
    ["A", "D", 1],
    ["A", "E", 1],
    ["B", "D", 1],
    ["B", "C", 1],
    ["C", "G", 1],
    ["D", "E", 1],
    ["E", "H", 1],
    ["E", "F", 1],
    ["F", "G", 1],
    ["G", "H", 1],

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
    cc = []
    visited = set()

    def dfs(vertex):
        visited.add(vertex)
        for neighbor, _ in graph1.adjacency_list[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
        if graph1.adjacency_list[vertex]:
            cc.append("1")

    dfs(graph1.vertices[0])
    return len(cc)


if __name__ == '__main__':
    graph = __init_graph()
    graph.print_adjacency_list()
    print(f"Цикломатическая сложность графа - {cyclomatic_complexity_dfs(graph)}")
