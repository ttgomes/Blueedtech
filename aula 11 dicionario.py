contatos_lista = [("Gustavo",'1234-5678'),("Marcelo",'9999-9999'),
("Paulo",'8888,8888'),("Laura",'2222-2222')]
print(contatos_lista[3][1])
# para criar dicionarios  utiiza-se {}
# para lista usamos []

contatos = dict(contatos_lista)
print(contatos)
print()
print(contatos["Paulo"])
print()
print(contatos.get("Marcelo","Paulo"))#get funciona igual if e eles

print('2222-2222' in contatos.values())

print("adicionando contatos no dicionario")
print()
contatos ['Mulher Maravilha'] = "2222-9785"
contatos ['Deadpool'] = "6666-6666"
print(contatos)

#a = input('digite o nome do contato : ')
#b = input('digite o numero do telfone :')
#contatos[a]=b
#print(contatos)

contatos [input('digite o nome:')] = input('digite o telefone : ')
print(contatos)
print()
print("_-=_"*10)
#print('removendo contatos do dicionario')
print()

 
del contatos['Mulher Maravilha']
print(contatos)

print(contatos.pop("Deadpool",'Contato não encotrado'))
print(contatos)
#contatos.clear()#limpa tudp
print()
print('.~.~.'*15)
print()

contatos_matheus = [("Tiago",'8888,8881'),("Launeda",'2522-2222'),
("Paulop",'8888,8788'),("Llaa",'2222-22622')]  
contatos2 = dict(contatos_matheus)
#for nome in contatos2:  adicionando uma lista na outra
 #   contatos[nome] = contatos2[nome]
#print(contatos)

contatos.update(contatos2)

print(contatos)