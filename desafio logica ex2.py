frase = input('Digite uma frase: ')
vogais_a = 0
vogais_e = 0
vogais_i = 0
vogais_o = 0
vogais_u = 0
resposta = ""

for letra in frase:
    if letra in "a":
        vogais_a += 1
for letra in frase:
    if letra in "e":
        vogais_e += 1
for letra in frase:
    if letra in "i":
        vogais_i += 1
for letra in frase:
    if letra in "o":
        vogais_o += 1
for letra in frase:
    if letra in "u":
        vogais_u += 1                                
for letra in frase:
    if not letra in('aeiou'):
        resposta += letra 
print(resposta)
print('A frase tinha %d vogais a ' %(vogais_a))
print('A frase tinha %d vogais e' %(vogais_e))
print('A frase tinha %d vogais i' %(vogais_i))
print('A frase tinha %d vogais o' %(vogais_o))
print('A frase tinha %d vogais u' %(vogais_u))