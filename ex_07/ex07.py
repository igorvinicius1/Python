vetor = [0] * 100
x = float(input())
vetor[0] = x

print('N[0] = {:.4f}' .format(vetor[0]))

for i in range(1, 100):
    vetor[i] = vetor[i-1] / 2
    print('N[{}] = {:.4f}' .format(i, vetor[i]))

    