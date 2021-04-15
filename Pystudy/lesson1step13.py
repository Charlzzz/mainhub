a = float(input())
b = float(input())
x = str(input())
if x == ("*") :
    print(a*b)
if x == ("-") :
    print(a-b)
if x == ("+") :
    print(a+b)
if x == ("pow") :
    print(a**b)
if x == ("div") and b != 0.0:
    print(a // b)
if x == ("/") and b != 0.0:
    print(a / b)
if x == ("mod") and b!= 0.0:
    print(a % b)
elif b == 0.0 and (x == ("mod") or x == ("/") or x == ("div")) :
    print("Деление на 0!")
