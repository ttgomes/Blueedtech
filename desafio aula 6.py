def dia1(dia) :
    if dia > 0 and dia <= 31 :
      return dia  
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

print(f"A data digitada é : {dia1(dia)}/{mes1(mes)}/{ano1(ano)} ")

