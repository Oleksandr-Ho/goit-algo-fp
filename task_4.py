"""Завдання 4. Візуалізація піраміди

Використовуючи як базу код побудовb бінарних дерев, побудуйте функцію, що буде візуалізувати бінарну купу."""


import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для створення бінарної купи зі списку значень
def create_heap_from_list(values):
    root = Node(values[0])
    nodes_queue = [root]
    i = 1
    while i < len(values):
        current_node = nodes_queue[0]
        if not current_node.left:
            current_node.left = Node(values[i])
            nodes_queue.append(current_node.left)
            i += 1
        elif not current_node.right:
            current_node.right = Node(values[i])
            nodes_queue.append(current_node.right)
            nodes_queue.pop(0)  # Видаляємо вузол з черги, якщо обидві дочірні вузли вже є
            i += 1
    return root

# Створення купи зі списку та її відображення
heap_values = [0, 4, 1, 5, 10, 3]
heap_root = create_heap_from_list(heap_values)
draw_tree(heap_root)