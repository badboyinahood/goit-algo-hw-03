import turtle

def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)
        t.right(120)
        koch_snowflake(t, length, level - 1)
        t.left(60)
        koch_snowflake(t, length, level - 1)

if __name__ == "__main__":
    import sys

    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 2 або 3): "))
    except ValueError:
        print("Некоректне значення! Має бути ціле число.")
        sys.exit(1)

    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-300, 150)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, 600, level)
        t.right(120)

    turtle.done()
