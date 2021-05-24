#exerciocio 1
"""a = float(input('digite o primeiro numero : '))
b = float(input('digite o segundo numero : '))

soma = (a+b)
multi = (a*b)
div = (a//b)

print("soma : " ,soma)
print()
print("multiplicação : ",multi)
print()
print("divisão : ",div)
print()

if a > b:
   print(a)
elif b > a:
   print(b)
else:

 if (soma%2) == 0:
    print("A soma dos numeros é : Par")
 else:
    print("A soma dos numeros é : Ímpar")

print()
c = multi * multi
d = c // div


if multi > 40 :
   print("o resultado maior que 40 é : " , multi % div)
else:
   print("A multiplição nao foi maior que 40")  """


#exercicio 2


"""frase = input('Digite uma frase: ')
vogais = 0
resposta = ""

for letra in frase:
    if letra in "aeiou":
        vogais += 1
for letra in frase:
    if not letra in('aeiouAEIOU'):
        resposta += letra 
print(resposta)
print('A frase tinha %d vogais ' %(vogais))"""


#exercicio 3





#exercicio 4

'''def dia1(dia) :
    dia2 = ['','um','doi','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete',
    'dezoito','dezenove','dezesete','dezoito','dezenove','vinte','vinte eu um','vinte dois','vinte três','vinte e quatro','vint e cinco',
    'vinte e seis','vinte e sete','vinte e oito','vinte e  nove','trinta']
    dia3 = dia2[dia]
    if dia > 0 or dia <= 31 :
      return dia3  
    else:
      return "Null"   

def mes1(mes) :
    mes2 = ['','janeiro','fevereiro','março','abril','maio',
    'junho','julho','agosto','setembro','novembro','dezembro']
    mes3 = mes2[mes]
    if mes > 0 and mes <= 12:
        return mes3
    else:
        return "Null"
0
def ano1(ano) :
    if ano > 0 and ano <= 3000:
        return ano
    else:
        return "Null"    
    
    
dia = int(input('Entre com dia :'))    
mes = int(input('Entre com mes :'))    
ano = int(input('Entre com ano  :'))    

dia1(dia)
mes1(mes)
ano1(ano)


print(f"A data digitada é : {dia1(dia)} de {mes1(mes)} de  {ano1(ano)} ")'''

#exercicio 5


"""frase = input('Digite uma frase: ')
vogais = 0
resposta = ""

for letra in frase:
    if letra in "aeiou":
        vogais += 1
for letra in frase:
    if not letra in('aeiouAEIOU'):
        resposta += letra 
print(resposta)
print('Foi extraido %d letras da frase original ' %(vogais))"""

#exercicio 6


'''password = "1234"
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
       print("Você acertou em", len(lista_cont),"tentativas")      '''
       



#exercicio 7

'''' lista_de_resposta = []

print("Responda com (S) ou (N) as seguintes perguntas")
     
telefone = input("Telefonou para a vítima?")
lista_de_resposta.append(telefone)
local = input("Esteve no local do crime?")
lista_de_resposta.append(local)
mora = input("Mora perto da vítima?")
lista_de_resposta.append(mora)
devia = input("Devia para a vítima?")
lista_de_resposta.append(devia)
trabalhou = input("Já trabalhou com a vítima?")
lista_de_resposta.append(trabalhou)

letras_s = 0

for letra in lista_de_resposta:
    if letra in "s" :
        letras_s += 1

if letras_s <= 2 :
   print("Suspeito")
if letras_s == 3 or letras_s == 4:
   print('Cumplice')
if letras_s == 5:
   print('Assasino')        '''

#exercicio 8 
"""dados = {}

nome = input("Digite o nome: ") 
ano = float(input("Digite o ano de nascimento: "))
ano_atual = 2021
idade_cont = ano_atual - ano
dados[nome] = idade_cont

carteira = float(input("Digite o numero da carteira de trabalho: "))
if  carteira != 0 :
    dados['carteira de trabalho'] = carteira
    ano_contrato = float(input("Digite o ano de contratação: "))
    tempo_contribuicao = ano_atual - ano_contrato
    salario = float(input('Digite o valor do salario: '))
    dados["salario"] = salario
    dados["Ano contratado"] = ano_contrato
else:
    dados["Carteira de trabalho"] = "nao tem"

tempo_contribuicao = ano_atual - ano_contrato
aposento = 35 - tempo_contribuicao
dados["Quantidade de anos para se aposentar:"] = aposento

print(dados)"""

#exercicio 7

from time import sleep
lista = []
listapares =[]
listaimpares= []
listafinal = []
while len(lista) <7:
    numero = int(input(f'digite um numero:'))
    lista.append(numero)
    sleep(1)

for nmrs in lista:
    if nmrs %2 ==0:
        listapares.append(nmrs)
    else:
        listaimpares.append(nmrs)

listapares.sort()
listaimpares.sort()
listafinal.extend(listapares)
listafinal.extend(listaimpares)

print(listafinal)
