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

# VERTEXES_NAMES: list[str] = [
#     "A",
#     "B",
#     "C",
#     "D",
#     "E",
#     "F",
#     "G",
#     "H",
# ]
# EDGES: list[list[str, str, int]] = [
#     ["A", "D", 1],
#     ["A", "E", 1],
#     ["B", "D", 1],
#     ["B", "C", 1],
#     ["C", "G", 1],
#     ["D", "E", 1],
#     ["E", "H", 1],
#     ["E", "F", 1],
#     ["F", "G", 1],
#     ["G", "H", 1],
#
# ]
VERTEXES_NAMES: list[str] = [
    "0",
    "1",
    "2",
    "3",
    "4"
]
EDGES: list[list[str, str, int]] = [
    ["0", "1", 1],
    ["0", "2", 1],
    ["1", "3", 1],
    ["2", "3", 1],
    ["3", "4", 1]
]

def __init_graph():
    g = Graph()
    for vertex in VERTEXES_NAMES:
        g.add_v(vertex)
    for edge in EDGES:
        g.add_e(edge[0], edge[1], edge[2])
    return g


# def cyclomatic_complexity_dfs(graph1):
#     # Инициализация переменных.
#     cc = []
#     visited = set()
#
#     def dfs(vertex):
#         visited.add(vertex)
#         for neighbor, _ in graph1.adjacency_list[vertex]:
#             if neighbor not in visited:
#                 dfs(neighbor)
#         if graph1.adjacency_list[vertex]:
#             cc.append("1")
#
#     dfs(graph1.vertexes[0])
#     return len(cc)
def dfs(graph1: Graph, start: str, visited: dict[str, bool]):
    visited[start] = True

    for neighbor, _ in graph1.adjacency_list[start]:
        if not visited[neighbor]:
            dfs(graph1, neighbor, visited)


def calculate_cyclomatic_complexity(graph1):
    visited = {}
    for vertex in graph1.vertexes:
        visited[vertex] = False
    count_edges = 0

    for vertex in graph1.adjacency_list:
        print(vertex)
        if not visited[vertex]:
            dfs(graph1, vertex, visited)
            count_edges += 1

    return count_edges - len(graph1.adjacency_list) + 2


if __name__ == '__main__':
    graph = __init_graph()
    graph.print_adjacency_list()
    print(f"Цикломатическая сложность графа - {calculate_cyclomatic_complexity(graph)}")
