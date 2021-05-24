'''def notas(na,nb,nc) :
    media = na + nb + nc
    return media // 3 
    
def media1(na,nb,nc):
    media1 = na + nb
    if nb + nc > media1:
       media1 = nb + nc
    if nc + na > media1:
       media1 = nc + na
    return media1 // 2

def maior_nota(na,nb,nc):
    maior = na
    if nb > maior:
       maior = nb
    if nc > maior:
       maior = nc
    return maior

def menor_nota(na,nb,nc):
    menor = na
    if nb < menor:
        menor = nb
    if nc < menor:
     menor = nc
    return menor

prova_a = float(input("Entre com a nota da primeira prova :"))
prova_b = float(input("entre com a nota da segunda prova :"))
prova_c = float(input("entre com a nota da terceira prova :"))


print(f"A média das 3 provas è : {notas(prova_a,prova_b,prova_c)}")
print(f'A média entre as duas maiores notas é : {media1(prova_a,prova_b,prova_c)}')
print(f'Sua maior nota é : {maior_nota(prova_a,prova_b,prova_c)}')
print(f'Sua menor nota é : {menor_nota(prova_a,prova_b,prova_c)}')'''


