n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
media = float(n1*0.2 + n2*0.3+ n3*0.4+ n4*0.1)

print('Media: {:.1f}' .format(media))
if (media >= 7.0):
    print('Aluno aprovado.')
elif (media < 5.0):
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    ex = float(input('Nota do exame: '))
    media = (ex + media) / 2

    if (media >= 5):
        print('Aluno aprovado.')
        print('Media final {:.1f}' .format(media))
        
    else:
        print('Aluno reprovado.')