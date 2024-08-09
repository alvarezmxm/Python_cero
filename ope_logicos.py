#Operadores Logicos

#En esta parte se una AND y si un boolean no es igual sera falso
print(True and True) #True
print(True and False) #Flase
print(False and False) #False
print(False and True) #False

#Ejemplo de como se puede usar en este caso si un numero es mayor o igual 100 y es menor o igual a 1000 va a hacer verdadero en caso contrario sera falso

stock = input("Ingresa el numero de stock de los juegos: ")
print(type(stock))
stock = int(stock)
print(stock)
print(type(stock))

print(stock >= 100 and stock<= 1000)