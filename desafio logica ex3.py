
password = "1234"
entrada_pass = "" 
while (entrada_pass != password):
    entrada_pass = input("Digite sua senha :")
    if entrada_pass == password:
        print('Seja bem vindo:')
    else:
       print("Senha invalida. Tente novamente: ") 

import random
lista_cont = []
sorteio = random.randint(1,10)
num = ""
while (num != sorteio):
    num = int(input('Ola jogador eu pensei em um numero de 1 a 10, você conseguer adivinhar meu pensamento? '))
    lista_cont.append(num)
    if num > sorteio:
       print("o numero que voce digitou e menor do que o numero que eu pensei")
    if num < sorteio:
       print("o numero que eu pensei e maior do que vc esta pensando")  
    if num == sorteio:
       print("Você acertou em", len(lista_cont),"tentativas") 