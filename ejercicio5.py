# Hallar la potencia de cualquier número

#Ingresar como dato de tipo float el número que será la base dentro del ejercicio de potencia
x = float(input("Escriba la base que desea elevar a una determinada potencia: "))

#Ingresar cómo dato de tipo float el número que será el exponente dentro del ejercicio de potencia
y = float(input("Escriba el exponente al que desea elevar su base: "))

#Cálculo para elevar un número a una determinada potencia
potencia = x**y

#Imprimir el resultado del ejercicio de potencia
print(x,"elevado a la potencia",y,"da cómo resultado",potencia)