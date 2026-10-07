# nome = input('Digite seu nome: ')
# print(nome)

# curso = input('Digite seu curso: ')
# print(curso)

# print(f'Ola meu nome é {nome} e faço {curso} ')

#--------------------------------------------------------------------------------------

# n1 = int(input('Digite o primeiro número: '))
# n2 = int(input('Digite o segundo número: '))

# adiçao = n1 + n2
# subtraçao = n1 - n2
# divisao = n1 / n2
# veses = n1 * n2
# expoente = n1 ** n2
# restoDivisao = n1 % n2
# divisaoInteira = n1 // n2

# print(adiçao)
# print(subtraçao)
# print(divisao)
# print(veses)
# print(expoente)
# print(restoDivisao)
# print(divisaoInteira)
#----------------------------------------------------------------------------------------


#  numero = 22
#  chute = int(input('digite o seu chute para o numero'))
# print(chute)

#  if chute == numero:
#      input('Voce acertou o numero: ')

#  else:
#      input('Voce errou o numero: ')
#------------------------------------------------------------------------------------------


numero = 13
tenta = 5

while tenta > 0:

    chute = int(input('Digite o numero que voce acha o correto '))
    print(chute)

    if chute < numero:
        print('O numero é maior.')

    elif chute > numero:
        print('O numero é menor.')

    else:
        print('Você acertou o numero.')
        break

    tenta -= 1

else:
    print('Acabaram as tentativas.')





    

