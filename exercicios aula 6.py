
#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.


def soma (a,b,c):
    print('a soma dos tres argumentos é:', a+b+c)    

soma(1,2,3)

#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.

def funcao(d):
    if d > 0 :
        return "p"
    elif d == 0:
        return "0"
    else:
        return "n"

d= int(input("digite o valor :"))
print("resultado: ", funcao(d))

#Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, 
# que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.

def somaImposto (taxa,custo):
    custo = custo + (custo * taxa / 100)
    return custo


taxa = float(input('digite o valor da taxa: '))
custo = float(input('digite o valor do custo: '))


custo = somaImposto(taxa, custo)

print("resultado: ",(custo))

#Faça um programa que calcule o salário de um colaborador na empresa XYZ.
#O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.

def extras(vhora, recebe):
  salario= vhora * recebe
  if vhora > 40:
    hextra = vhora - 40
    hextra = hextra * (recebe * 1.5) 
    salario = salario + hextra
    print ("\nO valor da hora extra é: ", hextra)
  print ("Você irá receber: R$", salario)
recebe= float (input("Quanto você recebe por hora? \n")) 
vhora = float (input("\nQuantas horas você trabalho? \n"))
extras (vhora, recebe)

# Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.

]def imc(peso,altura):
    print(f"o indice de massa corporal é : {peso / altura ** 2 :.2f}")

imc(75,1.68)    

#Escreva uma função que, dado um número nota representando a nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).

def conceito(a):
    if a >= 9:
       print("A")
    if a >= 8:
       print("B")
    if a >= 7:
       print("C")
    if a >= 6:
       print("D")
    if a <= 4:
       print("F")

nota = int(input('digite a nota do aluno : '))   

conceito(nota)

# ⦁	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. Se eles forem iguais, imprima que eles são iguais.

def num(a,b):
   if a < b :
      print(a)
   elif b < a: 
      print(b)
   elif b == a:
       print ("numeros iguais")

entrada1 = float(input("digite um numero : "))   
entrada2 = float(input("digite um numero : "))   

num(entrada1,entrada2)








     
    
    




        

