
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return (f'com {idade} anos : nao vota')
    elif 16 > idade < 18:
        return (f'com {idade} anos : opcional')
    else:
        return (f'com {idade} anos : obrigatorio')

entrada = int(input("digite seu ano de nascimento: "))

print(voto(entrada))
