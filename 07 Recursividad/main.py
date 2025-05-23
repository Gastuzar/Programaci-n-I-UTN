from Tp import factorial, fibonacci, potencia, decimal_a_binario, es_palindromo, suma_digitos, contar_bloques, contar_digito
#1
def mainTp1():
    num = int(input("Ingrese un numero: "))
    for i in range(1, num + 1):
        print(f"El factorial de {i} es: {factorial(i)}")
if __name__ == "__main__":
    mainTp1()

#2
def mainTp2():
    num = int(input("Ingrese un numero: "))
    print(f"La serie de Fibonacci hasta la posicion {num} es:")
    for i in range(num + 1):
        print(fibonacci(i), end=" ")
    print()
if __name__ == "__main__":
    mainTp2()

#3
def mainTp3():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")
if __name__ == "__main__":
    mainTp3()

#4
def mainTp4():
    num = int(input("Ingrese un numero entero positivo: "))
    if num < 0:
        print("El numero debe ser positivo.")
    else:
        binario = decimal_a_binario(num)
        print(f"La representacion en binario de {num} es: {binario}")
if __name__ == "__main__":
    mainTp4()
#5
def mainTp5():
    palabra = input("Ingrese una palabra: ")
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo.")
    else:
        print(f"{palabra} no es un palíndromo.")
if __name__ == "__main__":
    mainTp5()

#6
def mainTp6():
    num = int(input("Ingrese un numero entero positivo: "))
    if num < 0:
        print("El numero debe ser positivo.")
    else:
        suma = suma_digitos(num)
        print(f"La suma de los digitos de {num} es: {suma}")
if __name__ == "__main__":
    mainTp6()

#7
def mainTp7():
    num = int(input("Ingrese un numero entero positivo: "))
    if num < 0:
        print("El numero debe ser positivo.")
    else:
        bloques = contar_bloques(num)
        print(f"El numero {num} tiene {bloques} bloques.")
if __name__ == "__main__":
    mainTp7()
#8
def mainTp8():
    numero = int(input("Ingrese un numero entero positivo: "))
    digito = int(input("Ingrese un digito (0-9): "))
    if numero < 0 or digito < 0 or digito > 9:
        print("El numero debe ser positivo y el digito debe estar entre 0 y 9.")
    else:
        cantidad = contar_digito(numero, digito)
        print(f"El digito {digito} aparece {cantidad} veces en el numero {numero}.")
if __name__ == "__main__":
    mainTp8()