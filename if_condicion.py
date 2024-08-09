#Las condidicones IF siempre se ejecutan con un booleano y agregando ":" dos puntos

if True:
    print("Se imprime si es TRUE")
else:
    print("Se imprime si es False")
    
edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Tiene derecho a tomar")
else:
    print("Eres menor de edad no puede votar")
    
#Usamos doble condicional con elseif

sueldo = int(input("Ingresa tu sueldo mensual: "))

sueldo = sueldo * 12

print(sueldo)

if sueldo >=1000000:
    print("Investigar al ciudadano porque gana " + "$",sueldo)
elif sueldo >=450000 and sueldo <1000000:
    print("El ciudadano debe de pagar al SAT, porque gana: " + "$",sueldo)
else:
    print("El siudadano no debe de pagar al SAT porque gana: " + "$",sueldo)
    
#IF comparando un dato con ==

mascota = input("Que mascota te gusta: ")

if mascota == "perro":
    print("El perro es el mejor amigo del hombre")
elif mascota == "gato":
    print("Los gatos son muy indiferentes con los humanos pero son limpios")
else:
    print("La mascota aun no esta en la base de datos")