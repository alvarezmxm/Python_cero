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
    