#1)
for i in range(2, 21):
    if i % 2 == 0:
        print(i, end=", ")
print("\n")
#2)
print("ingrese numeros hasta que la suma supere 100: ")
suma = 0
while suma < 100:
    num = int(input("ingrese un numero: "))
    suma += num
print("la suma es: ",suma, "se supero 100")
#3)
frutas = ["apple", "banana", "avocado"]
for fruta in frutas:
    if fruta[0] == "a":
        print(fruta, end=", ")
print("\n")
#4)
tabla_del_7 = 7
for i in range(1, 11):
    print(tabla_del_7, "*", i, "=", tabla_del_7 * i)
#5)
texto = input("ingrese un texto: ")
texto = texto.lower()
for vocal in texto:
    if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u":
        cant_vocales_a = texto.count("a") #count sirve para contar la cantidad de veces que aparece un elemento en una lista o string
        cant_vocales_e = texto.count("e")
        cant_vocales_i = texto.count("i")
        cant_vocales_o = texto.count("o")
        cant_vocales_u = texto.count("u")
print("En el texto hay: ", cant_vocales_a, "vocales a", cant_vocales_e, "vocales e", cant_vocales_i, "vocales i", cant_vocales_o, "vocales o", cant_vocales_u, "vocales u")
print("\n")
#6)
lista= [3, 1, 3, 5, 1]
new_lista = []
for i in lista:
    if i not in new_lista:
        new_lista.append(i)
print("Lista sin duplicados: ", new_lista)
#7)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=", ")
    elif i % 3 == 0:
        print("Fizz", end=", ")
    elif i % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(i, end=", ")
print("\n")
#8)
cadena = "hola hola mundo"
cadena = cadena.split()
# Separa la cadena en palabras
diccionario = {}
for palabra in cadena:
    if palabra in diccionario:
        diccionario[palabra] += 1
    else:
        diccionario[palabra] = 1
print(diccionario)
#9)
cadena = input("ingrese una cadena: ")
for i in cadena:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        cadena = cadena.replace(i, "")
print("la cadena sin vocales es: ", cadena)
#10)
num = int(input("ingrese un numero primo: "))
for i in range(2, num + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=", ")