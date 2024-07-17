vidas = 3
print("El usuario tiene ", vidas, "vidas")
print("El tipo de datos de las vidas son ", type(vidas))

temperatura = 12.12
print("Estamos a una temperatura de ", temperatura)
print("El tipo de dato de la temperatura es ", type(temperatura))

suma = vidas + temperatura
print("Es una suma entre las vidas y temperatura y es: ", suma)
print("El tipo de dato de la suma es: ", type(suma))


print("==============================================")
print("==============================================")

vidas2 = 2
print("Tenemos ", vidas2, "vidas")
print("Vamos a restar una vida colocando variable = variable -1")
vidas2 = vidas2 -1
print("actualemnte tenemos ", vidas2, "vida")
print("Vamos a restar otra vida pero ahora colocando variable -=1, esta es la mas comun")
vidas2 -=1
print("Actualmente tenemos ", vidas2, "vidas")
print("Vamos a sumar una vida colocando variable +=1")
vidas2 +=1
print("Actualmente tenemos ", vidas2, "vida")
