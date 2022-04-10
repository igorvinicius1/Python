vetor = [0] * 3
v2 = []

valor = input().split()
#a, b, c = [int(z) for z in input().split()] #para inserir numero por numero numa unica linha
a, b, c = valor
v2.append(a)
v2.append(b)
v2.append(c)
v2.sort()

print(v2[0])
print(v2[1])
print(v2[2])
print()
print(a)
print(b)
print(c)


