a = int(input())
b = int(input())
s = min(a,b)
if a == b:
    print(s)
else :
    while s % a != 0 or s % b != 0 :
        s += 1
        x = s % a
        y = s % b
        if x == 0 and y == 0:
            print(s)

#a=int(input())
#b=int(input())
#d=a
#while d%a!=0 or d%b!=0:
#    d+=1
#print(d)  короткий код