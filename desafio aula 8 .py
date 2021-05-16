def custo_aviao(aviao):
    a = 312.00
    b = 447.00
    c = 831.00
    d = 986.00
    if aviao == 1:
       return a
    if aviao == 2:
       return b
    if aviao == 3:
        return c
    if aviao == 4: 
        return d
    elif aviao == 0 or aviao > 5:
        return False
 
def custo_hotel(hotel):
    noite = hotel * 140.00
    return noite

def custo_carro(carro):
    diaria = carro * 40.00
    desconto7 = 50.00
    desconto3 = 30.00
    if carro >= 3  and carro < 7:
        return diaria - desconto3
    elif carro >= 7:
        return diaria - desconto7
    else:
        return diaria  

def total(extras):
    a = extras
    b = custo_carro(carro) 
    e = custo_hotel(hotel)
    d = custo_aviao(aviao)
    return a + d + b + e

aviao = int(input('''
São paulo digite    (1)
Porto Alegre digite (2)
Recife digite       (3) 
Manaus digite       (4)

digite um numero referente a cidade que você quer viajar :'''))

hotel  = int(input(f"digite a quantidade de dias para hospedagem : "))
carro = int(input(f"digite a quantidade de dias para locação de carro : "))
extras = int(input(f"digite um valor caso tenha despesas extras : "))

custo_hotel(hotel)
custo_carro(carro) 
custo_aviao(aviao)
total(extras)

print(f"o valor total da viagem é : R$ {total(extras)}")


