import sys

num=123456789
to=num.to_bytes(10,'big')

a = sys.getsizeof(to)
b = sys.getsizeof(num)
print(a)
print(b)