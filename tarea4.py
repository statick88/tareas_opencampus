"""
Escribe un programa en la consola de python que pida al usuario su peso (en kg) 
y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
e imprima por pantalla la frase Tu índice de masa corporal es donde es el índice de masa 
corporal calculado redondeado con dos decimales. 

"""

peso = float(input("Por favor ingrese su peso actual (Kg): "))
estatura = float(input("Por favor ingrese su tamaño actual (m): "))

imc = round(peso/estatura**2, 2)
print("Tu índice de masa corporal es {}".format(imc)) 