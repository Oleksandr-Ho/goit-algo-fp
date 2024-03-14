"""Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком

Для реалізації однозв'язного списку необхідно:
1. написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
2. розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
3. написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список."""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    

# Функція, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

# функції сортування злиттям
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head

        middle = self.get_middle(head)
        next_to_middle = middle.next

        middle.next = None

        left = self.merge_sort(head)
        right = self.merge_sort(next_to_middle)

        sorted_list = self.sorted_merge(left, right)
        return sorted_list

    def get_middle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left, right):
        result = None

        if left is None:
            return right
        if right is None:
            return left

        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)
        return result
    
# функція об'єднання двох відсортованих списків
    def merge_sorted_lists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.data <= list2.data:
            result = list1
            result.next = self.merge_sorted_lists(list1.next, list2)
        else:
            result = list2
            result.next = self.merge_sorted_lists(list1, list2.next)
        return result
    

if __name__ == "__main__":
    # Тестування реверсування
    print("Тестування реверсування списку:")
    llist = LinkedList()
    for data in [1, 2, 3, 4, 5]:
        llist.insert_at_end(data)
    print("Оригінальний список:")
    llist.print_list()

    llist.reverse()
    print("Список після реверсування:")
    llist.print_list()
    print("-" * 50)

    # Тестування сортування злиттям
    print("Тестування сортування злиттям:")
    llist = LinkedList()
    for data in [5, 2, 3, 1, 4]:
        llist.insert_at_end(data)
    print("Оригінальний список:")
    llist.print_list()

    llist.head = llist.merge_sort(llist.head)
    print("Відсортований список:")
    llist.print_list()
    print("-" * 50)

    # Тестування об'єднання двох відсортованих списків
    print("Тестування об'єднання двох відсортованих списків:")
    llist1 = LinkedList()
    llist2 = LinkedList()
    for data in [1, 3, 5]:
        llist1.insert_at_end(data)
    for data in [2, 4, 6]:
        llist2.insert_at_end(data)

    print("Перший відсортований список:")
    llist1.print_list()
    print("Другий відсортований список:")
    llist2.print_list()

    merged_list = LinkedList()
    merged_list.head = merged_list.merge_sorted_lists(llist1.head, llist2.head)
    print("Об'єднаний відсортований список:")
    merged_list.print_list()