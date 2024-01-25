
print('Código iniciado')
print('')
chosen_number = input('Digite o número teto do desafio, o número tem q ser inteiro: ')

while True:
    if chosen_number.isdigit():
        chosen_number = int(chosen_number)
        break
    else:
        print('O valor informado n é numérico ou n é inteiro.')
        chosen_number = input('\nDigite o número teto do desafio, o número tem q ser inteiro: ')
        continue


from random import randint
random_number = randint(0, chosen_number)

counter = 0

while True:
    user_answer = input(f'\nAdvinhe o número de zero até {chosen_number}: ')

    if user_answer.isdigit():
        user_answer = int(user_answer)
    else:
        print('O valor informado n é numérico ou n é inteiro')
        continue

    counter += 1
    if user_answer == random_number:
        print('\nVc acertou o número')
        break
    elif user_answer > random_number:
        print('o número é menor q esse')
    else:
        print('o número é maior q esse')

print(f'vc acertou c {counter} tentativas')

