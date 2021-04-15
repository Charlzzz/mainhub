a = int(input())
b = int(input())
c = int(input())
m = a + b + c
#l = list[a,b,c]
#print.max(l)
#a = list(map(int, input().split()))
#b = list(map(int, input().split()))
#c = list(map(int, input().split()))
print(max(a,b,c))
print(min(a,b,c))
print(m - max(a,b,c) - min(a,b,c) )
