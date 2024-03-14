"""Завдання 3. Дерева, алгоритм Дейкстри

Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення найкоротших 
шляхів від початкової вершини до всіх інших."""

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_vertex = heapq.heappop(queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    return distances

# Граф для прикладу
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Обчислення найкоротших шляхів
distances = dijkstra(graph, 'A')
print("Найкоротші шляхи від точки А:", distances)

# Створення графа для візуалізації
G = nx.DiGraph()
for node in graph:
    for neighbor, weight in graph[node]:
        G.add_edge(node, neighbor, weight=weight)

pos = nx.spring_layout(G)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Відображення відстаней до кожної вершини
for node, distance in distances.items():
    x, y = pos[node]
    plt.text(x, y-0.1, s=f'd={distance}', bbox=dict(facecolor='yellow', alpha=0.5), horizontalalignment='center')

plt.title('Візуалізація графа з найкоротшими шляхами від A')
plt.axis('off')
plt.show()
