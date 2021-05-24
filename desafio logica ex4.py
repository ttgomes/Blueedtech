def dia1(dia) :
    dia2 = ['','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete',
    'dezoito','dezenove','dezesete','dezoito','dezenove','vinte','vinte eu um','vinte dois','vinte três','vinte e quatro','vint e cinco',
    'vinte e seis','vinte e sete','vinte e oito','vinte e  nove','trinta',"trinta e um"]
    dia3 = dia2[dia]
    if dia > 0 or dia <= 31 :
      return dia3  
    else:
      return "Null"   

def mes1(mes) :
    mes2 = ['','janeiro','fevereiro','março','abril','maio',
    'junho','julho','agosto','setembro','novembro','dezembro']
    mes3 = mes2[mes]
    if mes > 0 and mes <= 12:
        return mes3
    else:
        return "Null"
0
def ano1(ano) :
    if ano > 0 and ano <= 3000:
        return ano
    else:
        return "Null"    
    

dia = int(input('Entre com dia :'))    
mes = int(input('Entre com mes :'))    
ano = int(input('Entre com ano  :'))    

dia1(dia)
mes1(mes)
ano1(ano)


print(f"A data digitada é : {dia1(dia)} de {mes1(mes)} de  {ano1(ano)} ")
