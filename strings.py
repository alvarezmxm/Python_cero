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

