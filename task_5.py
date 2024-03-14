"""Завдання 5. Візуалізація обходу бінарного дерева

Використовуючи код для побудови бінарного дерева, необхідно створити програму на Python, 
яка візуалізує обходи дерева: у глибину та в ширину.

Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу."""

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.uuid = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node:
        graph.add_node(node.uuid, label=node.value)
        pos[node.uuid] = (x, y)
        if node.left:
            graph.add_edge(node.uuid, node.left.uuid)
            add_edges(graph, node.left, pos, x - 1 / 2 ** layer, y - 1, layer + 1)
        if node.right:
            graph.add_edge(node.uuid, node.right.uuid)
            add_edges(graph, node.right, pos, x + 1 / 2 ** layer, y - 1, layer + 1)

def interpolate_colors(n):
    start_rgb = np.array([0x00, 0x00, 0xFF])  # темно-синій
    end_rgb = np.array([0xAD, 0xD8, 0xE6])  # світло-синій
    return ['#' + ''.join([f'{int(rgb):02X}' for rgb in (start_rgb + (end_rgb - start_rgb) * i / (n-1))]) for i in range(n)]

def dfs(node, visited=None):
    if visited is None:
        visited = []
    if node:
        visited.append(node.uuid)
        dfs(node.left, visited)
        dfs(node.right, visited)
    return visited

def bfs(root):
    visited, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        if node:
            visited.append(node.uuid)
            queue.append(node.left)
            queue.append(node.right)
    return visited

def draw_trees(root):
    fig, axes = plt.subplots(1, 2, figsize=(20, 10))  # Створюємо 2 субплоти поруч
    
    for i, traversal_func in enumerate([dfs, bfs]):
        visited = traversal_func(root)
        colors = interpolate_colors(len(visited))
        color_map = {uuid: colors[i] for i, uuid in enumerate(visited)}

        G = nx.DiGraph()
        pos = {}
        add_edges(G, root, pos)
        node_colors = [color_map[node] for node in G.nodes()]

        labels = nx.get_node_attributes(G, 'label')
        title = "DFS Traversal" if i == 0 else "BFS Traversal"
        nx.draw(G, pos, labels=labels, with_labels=True, node_color=node_colors, node_size=1000, ax=axes[i])
        axes[i].set_title(title, size=15)

    plt.show()

root = Node('Root')
root.left = Node('Left')
root.right = Node('Right')
root.left.left = Node('Left.Left')
root.left.right = Node('Left.Right')

draw_trees(root)
