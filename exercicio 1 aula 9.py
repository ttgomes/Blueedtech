estoque = {
    "pão": [2000, 0.5],
    "salgado": [2000, 2.50],
    "pão de queijo": [4000, 0.30],
    "bolo": [0, 2]
    }
totalprodutos =0
totalvalor= 0 
continuar = True

while continuar == True:
      produto = input("Nome do produto (fim para sair):")
      if produto == "fim":
       break

      if produto in estoque:
        print("produto em estoque! ")
        print()
        qtd= int(input(f'quantos {produto} você quer comprar? '))
        print()
        if estoque[produto][0] < qtd:
        
         print("quantidade não disponivel para a compra")
        
        else: 
            print(f'vo