# Ingresar un valor en dólares y transformar en Euros y Yen.

#Ingresar valor en dolares para convertir
valor_dolar = float(input("Ingrese un valor en dolares: "))

#Calculos para convertir de dolares a euros
valor_euro = valor_dolar * 0,95

#Calculos para convertir de dolares a Yenes 
valor_yen = valor_dolar * 129,27

#Imprimir resultado de conversión de dolares a euros
print("los",valor_dolar,"dolares que digito, equivalen a",valor_euro,"euros")

#Imprimir resultado de conversión de dolares a yenes
print("los",valor_dolar,"dolares que digito, equivalen a",valor_yen,"yenes")