#1
lista = []
for i in range(1, 101):
    if i % 4 == 0:
        lista.append(i)
print(lista)

#2
lista = ["a", "b", "c", "d", "e"]
print(f"Mostrando el penultimo elemento de la lista: {lista[-2]}")

#3
# lista=[]
# elemento1 = input("Agrega un elemento a la lista: ")
# lista.append(elemento1)
# elemento2 = input("Agrega otro elemento a la lista: ")
# lista.append(elemento2)
# elemento3 = input("Agrega otro elemento a la lista: ")
# lista.append(elemento3)
# print(f"Los elementos de la lista son: {lista}")

#4
animales = ["perro", "gato", "conejo", "pez"]
print(f"La lista de animales antes de la modificacion es: {animales}")
animales[-1] = "loro"
animales[-2] = "oso"
print(f"La lista de animales despues de la modificacion es: {animales}")

#5
numeros = [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
#remove.(max()) elimina el maximo de la lista
print(numeros)

#6
lista = [10, 15, 20, 25, 30]	
print(lista[0:2])

#7
autos = ["sedan", "polo", "suran", "gol"]
autos[1] = "fiesta"
autos[2] = "focus"
print(autos)

#8
dobles =[]
dobles.append(2*5)
dobles.append(2*10)
dobles.append(2*15)
print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
#a)
cliente3 = []
cliente3.append(compras)
cliente3.append("jugo")
print(cliente3)
#b)

cliente2 = []
cliente2.append(compras)
cliente2[0][1][1] = "gaseosa"
print(cliente2)
#c)
cliente1 = []
cliente1.append(compras)
cliente1[0][0].remove("pan")
print(cliente1)
#d)
print(compras)

#10
lista_anidada = [15 ,True,[25.5, 57.9, 30.6],False]

print(lista_anidada)