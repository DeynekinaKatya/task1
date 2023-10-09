def equation_of_line(point1, point2):
    # координати точок
    x1, y1 = point1
    x2, y2 = point2

    # значення a і b
    a = y2 - y1
    b = x1 - x2

    # Знаходження значення c за одним із рівнянь
    c = a * x1 + b * y1

    # Завдання 2.Повернення  рівняння прямої
    return f"{a}x + {b}y = {c}"


pointA = (3, 2)
pointB = (5, 7)
result = equation_of_line(pointA, pointB)
print(result)