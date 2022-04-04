import math

v = int(input())
a = v / 100
a = math.floor(a)
b = (v % 100) / 50
b = math.floor(b)
resto = v - (100 * a) - (50 * b)
c = resto / 20
c = math.floor(c)
d = resto % 20
d = d / 10
d = math.floor(d)
resto = resto - (c * 20) - (d * 10)
e = resto / 5
e = math.floor(e)
f = resto % 5
f = f / 2
f = math.floor(f)
resto = resto - (e * 5) - (f * 2)


print('{} nota(s) de R$ 100,00\n' .format(a))
print('{} nota(s) de R$ 50,00\n' .format(b))
print('{} nota(s) de R$ 20,00\n' .format(c))
print('{} nota(s) de R$ 10,00\n' .format(d))
print('{} nota(s) de R$ 5,00\n' .format(e))
print('{} nota(s) de R$ 2,00\n' .format(f))
print('{} nota(s) de R$ 1,00\n' .format(resto))