i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2

n = int(input())
c = 1
while c <= n:
    print("*" * c)
    c += 1

n = int(input())
stars = "*"
while len(stars) <= n:     #len показывает количестов символов в строке
    print(stars)
    stars += 1