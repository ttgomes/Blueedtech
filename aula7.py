def numeros(a,b):
    if a < b :
       print(a)
    elif b < a :
       print(b)  
    else:
       print("valores idênticos") 

valor_a = float(input(" Digite um valor : "))
valor_b = float(input(" Digite um valor : "))

numeros(valor_a,valor_b) 
