dados = {}

nome = input("Digite o nome: ") 
ano = float(input("Digite o ano de nascimento: "))
ano_atual = 2021
idade_cont = ano_atual - ano
dados[nome] = idade_cont

carteira = float(input("Digite o numero da carteira de trabalho: "))
if  carteira != 0 :
    dados['carteira de trabalho'] = carteira
    ano_contrato = float(input("Digite o ano de contratação: "))
    tempo_contribuicao = ano_atual - ano_contrato
    salario = float(input('Digite o valor do salario: '))
    dados["salario"] = salario
    dados["Ano contratado"] = ano_contrato
else:
    dados["Carteira de trabalho"] = "nao tem"

tempo_contribuicao = ano_atual - ano_contrato
aposento = 35 - tempo_contribuicao
dados["Quantidade de anos para se aposentar:"] = aposento

print(dados)