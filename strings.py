#Creacion de una variable con "comillas dobles"
nombre = "Alfredo"

#Creacion de una variable con 'comillas simples'
apellido = "Alvarez"

#Creacion de variable para concatenar variables
templete = "Hola, mi nombre es " + nombre + " " + apellido

#Imprimimos las variables
print(templete)

#Creacion de una variable para crar un formato sin tener que concatenar.
#En este caso solo usamos .format() dentro de los parentesis colocamos las variables
templete2 = "Hola, mi nombre es {} {}".format(nombre, apellido)

print(templete2)

#Creacin de una variable para un formato en string 
#Solo agregaremos f"MENSAJE {VAR}" esta forma es mas limpa
templete3 = f"Hola, mi nombre es {nombre} {apellido}"

print(templete3)

#Esto solo es una prueba para ver como funciona al git branch
templete4 = f"Hola se hizo bien la rama y el merge por {nombre} {apellido}"
print(templete4)
