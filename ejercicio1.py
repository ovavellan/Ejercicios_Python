# Ingresar el radio de un círculo del usuario y calcule el área.

# ingresar el radio del ciruclo cómo dato de tipo float
radio_circulo=float(input("Por favor ingrese un valor para el radio del círculo: "))

#Valor de pi
pi = 3.14


#Calculos para el área del círculo 
area_circulo = pi * ((radio_circulo)**2) 

#Impresión de resultado 
print("El área del círculo de radio",radio_circulo,"es:",area_circulo)