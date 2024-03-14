"""Завдання 6: Жадібні алгоритми та динамічне програмування

Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування 
для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.

Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, 
а значення — це словник з вартістю та калорійністю.

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, 
не перевищуючи заданий бюджет.

Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв 
для максимізації калорійності при заданому бюджеті."""

# У задачі припускаємо, що кожної страви є по одній, тобто для прикладу жадібний алгоритм не може закупити максимально cola, так як у cola низька вартість однієї калорії

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    for item in items.values():
        item["ratio"] = item["calories"] / item["cost"]
    sorted_items = sorted(items.items(), key=lambda x: x[1]["ratio"], reverse=True)
    
    selected_items_details = []
    total_spent = 0
    total_calories = 0
    for name, item in sorted_items:
        if budget >= item["cost"]:
            budget -= item["cost"]
            total_spent += item["cost"]
            total_calories += item["calories"]
            selected_items_details.append((name, item["cost"], item["calories"], item["cost"]))
    
    return selected_items_details, total_spent, total_calories

def dynamic_programming(items, budget):
    names = list(items.keys())
    costs = [item["cost"] for item in items.values()]
    calories = [item["calories"] for item in items.values()]
    n = len(items)

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(calories[i - 1] + dp[i - 1][w - costs[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    w = budget
    selected_items_details = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items_details.append((names[i-1], costs[i-1], calories[i-1], costs[i-1]))
            w -= costs[i-1]

    selected_items_details.reverse()
    total_calories = dp[n][budget]
    total_spent = sum(cost for _, cost, _, _ in selected_items_details)
    return selected_items_details, total_spent, total_calories

budget = 100

# Greedy Algorithm
print("Greedy Algorithm:")
greedy_items, greedy_spent, greedy_calories = greedy_algorithm(items, budget)
for item in greedy_items:
    print(f"- Item: {item[0]}, Cost: {item[1]}, Calories: {item[2]}, Budget spent on item: {item[3]}")
print(f"Total Spent: {greedy_spent}; Total Calories: {greedy_calories}\n")

# Dynamic Programming
print("Dynamic Programming:")
dp_items, dp_spent, dp_calories = dynamic_programming(items, budget)
for item in dp_items:
    print(f"- Item: {item[0]}, Cost: {item[1]}, Calories: {item[2]}, Budget spent on item: {item[3]}")
print(f"Total Spent: {dp_spent}; Total Calories: {dp_calories}")
