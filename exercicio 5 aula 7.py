def ficha(nome,gols):
    print(f"O nome do jogadoe é : {nome}")
    print(f"{nome} fez o total de {gols} gols:") 


nome_a = str(input("Digite o nome do jogador :"))
gols_a = int(input("Digite a quantidade de gols :"))


ficha(nome_a,gols_a)
