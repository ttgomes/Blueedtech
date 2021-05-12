def notas(na,nb,nc) :
    soma_media = na + nb + nc
    media_3 = soma_media / 3
    return media_3

prova_a = float(input("Entre com a nota da primeira prova :"))
prova_b = float(input("entre com a nota da segunda prova :"))
prova_c = float(input("entre com a nota da terceira prova :"))

notas(prova_a,prova_b,prova_c)

print(f"A média das 3 provas è : {notas(prova_a,prova_b,prova_c)}")