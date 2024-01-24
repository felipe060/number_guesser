print('Código iniciado')
print('')
chosen_number = input('Digite o número teto do desafio: ')

if chosen_number.isdigit():
    chosen_number = int(chosen_number)
    print('numérico')
else:
    print('O valor informado n é numérico. Execute o código novamente e digite um número')
    quit()

from random import randint
random_number = randint(0, chosen_number)

while True:



#da p transformar o if numa função