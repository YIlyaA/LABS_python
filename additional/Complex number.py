import cmath

l = input().split()
a = int(l[0])
b = int(l[-1][:-1])
z = complex(a, b)
print(cmath.polar(z)[0])
print(cmath.polar(z)[1])
