#nome = input('Digite seu nome: ') #nome recebe o input ao mesmo tempo em que transmite uma mensagem, pode deixar tbm como input()
#print('É um prazer te conecer, {} !'.format(nome))
#print(nome.isalpha()) # muitas opções que retornam com True ou False a respeito de que tipo é a variável

######################################################

#a = int(input('Digite um valor --> '))
#b = int(input('Digite outro valor --> '))
#c = a + b
#print('O resultado de {} + {} é --> {}' .format(a, b, a+b))

######################################################

#n = int(input('Forneça um núemro: '))
#d = n*2
#t = n*3
#r = n**(1/2)
#print('DOBRO: {}, TRIPLO: {}, RAÍZ QUADRADA: {:.2f}'.format(d, t, r))

######################################################

import math #importa a biblioteca de matemática podendo utilizar suas funções como o sqrt (square root), existem muitas bibliotecas para se importar

#n = int(input('Number :'))
#raiz = math.sqrt(n)
#print('raiz: {}' .format(raiz))

######################################################

#p = float(input('input(Qual o preço do produto R$ '))
#p = p - (p * 0.05)
#print('O produto com desconto de 5% fica R$ {:.2f}' .format(p))

######################################################

#n = float(input('n: '))
#print('{:.0f}'.format(n))

######################################################

'''import random

a1 = 'igor'
a2 = 'thiago'
a3 = 'yasmim'
a4 = 'giovani'

lista = [a1, a2, a3, a4]

e = random.choice(lista)
print('Escolhido: {}'.format(e))'''

######################################################

'''import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))

lista = [n1, n2, n3, n4]
random.shuffle(lista) #embaralha a lista kkkk
print('A ordem de apresentação será --->  ', lista)'''

######################################################


'''import pygame #TOCANDO MUSIQUINHAS JOHN CENA

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o Pygame
pygame.init()

pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
pygame.event.wait()'''


######################################################
'''import math

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
print('{} nota(s) de R$ 1,00\n' .format(resto))'''

######################################################

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

