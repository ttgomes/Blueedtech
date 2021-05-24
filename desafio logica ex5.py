
frase = input('Digite uma frase: ')
vogais = 0
resposta = ""

for letra in frase:
    if letra in "aeiou":
        vogais += 1
for letra in frase:
    if not letra in('aeiouAEIOU'):
        resposta += letra 
print(resposta)
print('Foi extraido %d letras da frase original ' %(vogais))