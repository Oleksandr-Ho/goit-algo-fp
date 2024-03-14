"""Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала
“дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач повинен 
мати можливість вказати рівень рекурсії."""

import turtle
import math

def draw_tree(t, branch_length, level=8):
    if level > 0:
        t.forward(branch_length)
        t.left(45)
        draw_tree(t, branch_length / math.sqrt(2), level - 1)
        t.right(90)
        draw_tree(t, branch_length / math.sqrt(2), level - 1)
        t.left(45)
        t.backward(branch_length)

def main():
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = turtle.Turtle()
    t.speed('fastest')
    t.penup()
    t.goto(0, -250)
    t.pendown()
    t.left(90)

    level = int(input("Введіть рівень рекурсії (Рекомендомано 8): "))  # Запитуємо рівень рекурсії у користувача
    draw_tree(t, 100, level)

    screen.exitonclick()  # Виходить з програми після кліка мишею

if __name__ == '__main__':
    main()