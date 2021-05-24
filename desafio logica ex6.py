lista_de_resposta = []

print("Responda com (S) ou (N) as seguintes perguntas")
     
telefone = input("Telefonou para a vítima? : ")
lista_de_resposta.append(telefone)
local = input("Esteve no local do crime? : ")
lista_de_resposta.append(local)
mora = input("Mora perto da vítima? : ")
lista_de_resposta.append(mora)
devia = input("Devia para a vítima? : ")
lista_de_resposta.append(devia)
trabalhou = input("Já trabalhou com a vítima? : ")
lista_de_resposta.append(trabalhou)

letras_s = 0

for letra in lista_de_resposta:
    if letra in "s" :
        letras_s += 1
print()
if letras_s <= 2 :
   print("Classificado como Suspeito")
if letras_s == 3 or letras_s == 4:
   print('Classificado como Cumplice')
if letras_s == 5:
   print('Classificadao como Assasino')       