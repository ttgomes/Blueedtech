filmes =["Os vingadores","HP","Forrest Gump","A Procura da Felicidade",
         "Como eu era antes de você","O lobo de wall street",
         "Dois coelhos","lagoa azul"]
print()
filmes.append('Power Rangers')#adiciona um item ao final da lista
print(filmes)
print()
#a = input("digite um filme: ")
#filmes.append(a)
filmes_novos = ["historias cruzadas","esqueceram de mim","desventuras em serie ","poderoso chefao 2"]
filmes.extend(filmes_novos)#adiciona uma variavel com varios elementos
print(filmes)
print()
filmes.sort()#organiza por ordem alfabetica ou ordem numero do menor para o maior                                      
print(filmes)
print()
#filmes.reverse()#organiza ao contrario da ordem alfabetica e do maior para o menor numero
print()


filmes.insert(1,"pianista")#insere uma string ou um numero a uma posicao espefica na lista
filmes.insert(10,"projeto x")

filmes.remove("HP")
print()
print(filmes) 
filmes.remove("desventuras em serie ")#remove o intem digitado da lista
print()
print(filmes)
filmes.pop(8)#remove um item da lista pelo numero de indice
filmes.pop()#remove o ultimo item da lista
del filmes[1]#remove o item da lista pelo numero do indice
del filmes[0:3]#remove os itens da lista a dentro de intervalo especificado
#del filmes[:]#CUIDADO APAGA TUDO NAO SER PARA NADAAAAAAAAAAAAA





for filme in filmes:
    print(filme)

print(len(filmes))
