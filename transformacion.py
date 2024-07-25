#Transformacion de numero a string y vicerza

nombre = input("Agrega tu nombre: ")
edad = int(input("Agrega tu edad: ")) #Hacemos la transformacion de string a numeros esteros
fechaNacimiento = input("Agrega tu fecha de nacimiento: ") #El numero ingresado es string

print(F"Mi nombre es {nombre} y tengo {edad} años y naciste en {fechaNacimiento}")

print(nombre)
print(type(nombre))
print(edad)
print(type(edad))
print(fechaNacimiento)
print(type(fechaNacimiento))

fechaNacimiento = int(fechaNacimiento) #Transformamos de string a numeros enteros
print(type(fechaNacimiento))