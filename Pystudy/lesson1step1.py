
>>> fib = lambda x : 1 if x<= 2 else fib(x - 1) + fib(x - 2)
>>> fib(31)
1346269
>>> 2 + 5
7
>>> 3+5*4
23
>>> 3+5*4
23
>>> 40 // 5
8
>>> 40 / 5
8.0
>>> 42 % 8
2
>>> 42 // (4 + 2 * (-2)
... 42 / (4 + 2 * (-2)
  File "<stdin>", line 2
    42 / (4 + 2 * (-2)
    ^
SyntaxError: invalid syntax
>>> 239 % 10
9
>>> 239//9
26
>>> 2014 ** 14
18064773765607550801425251468864907833685590016
>>> - 42
-42
>>>  + 24\
  File "<stdin>", line 1
    + 24\
IndentationError: unexpected indent
>>>  + 24
  File "<stdin>", line 1
    + 24
IndentationError: unexpected indent
>>> +-+42
-42
>>> -*42
  File "<stdin>", line 1
    -*42
     ^
SyntaxError: invalid syntax
>>> *(-42)
  File "<stdin>", line 1
SyntaxError: can't use starred expression here
>>> print("test")
test
>>> 5 // 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
>>> 0.5
0.5
>>> 0.5 + 0.3
0.8
>>>  5 / 2
  File "<stdin>", line 1
    5 / 2
IndentationError: unexpected indent
>>> 5 / 2
2.5
>>> 5 // 2
2
>>> 1 / 3
0.3333333333333333
>>> 1 // 3
0
>>> 0.3 + 0.3 +0.3
0.8999999999999999
>>> 2 ** 5
32
>>> 9 ** 0.5
3.0
>>> 5e-1
0.5
>>> e2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'e2' is not defined
>>> 1e2
100.0
>>> 1.2345e3
1234.5
>>> 1.2345e-3
0.0012345
>>> 2014.0**14
1.806477376560755e+46
>>> 7/3
2.3333333333333335
>>> 7 // 3
2
>>> 7 / 3
2.3333333333333335
>>> int(2.99)
2
>>> int(-1.6)
-1
>>> 9 ** 19 - int(float(9**19))
89
>>> type(7)
<class 'int'>
>>>