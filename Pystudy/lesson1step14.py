x = str(input())
if x == ("прямоугольник"):
    a = int(input())
    b = int(input())
    s = (a * b)
    print(s);
if x == ("круг"):
    a = int(input())
    pi = float(3.14)
    s = float(pi * a ** 2)
    print(s);
if x == ("треугольник"):
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2  # 6
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s);
