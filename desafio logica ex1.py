a = float(input('digite o primeiro numero : '))
b = float(input('digite o segundo numero : '))
print()
soma = (a+b)
multi = (a*b)
div = (a//b)

print("soma = " ,soma)
print()
print("multiplicação = ",multi)
print()
print("divisão = ",div)
print()

if a > b:
   print(a)
elif b > a:
   print(b)
else:

 if (soma%2) == 0:
    print("A soma dos numeros é Par")
 else:
    print("A soma dos numeros é Ímpar")

print()
c = multi 
d = c // div

if multi > 40 :
   print("o resultado maior que 40 é : " , d)
else:
   print("A multiplicação nao foi maior que 40") 