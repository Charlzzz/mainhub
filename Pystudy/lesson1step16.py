a = int(input())
if a % 10 in [2, 3, 4] and a % 100 not in [12, 13, 14] and (a % 100) // 10 != 1:
    print(a,"программиста")
elif a % 10 == 1 and a != 11 and a % 100 != 11 and (a % 100) // 10 != 1:
    print(a,"программист")
else:
    print(a,"программистов")

'''x = int(input())
if x % 100 in (11, 12, 13, 14) or x % 10 in (5, 6, 7, 8, 9, 0): print(x, 'программистов')
elif x % 10 in (2, 3, 4): print(x, 'программиста')
else: print(x, 'программист')  короткий вариант '''