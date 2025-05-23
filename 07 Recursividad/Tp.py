#1 Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
# función para calcular y mostrar en pantalla el factorial de todos los números enteros
# entre 1 y el número que indique el usuario

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
#2Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
# indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
# especifique.

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#3 Crea una función recursiva que calcule la potencia de un número base elevado a un
# exponente, utilizando la fórmula 𝑛
# 𝑚 = 𝑛 ∗ 𝑛(𝑚−1)
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)
    
#4 Crear una función recursiva en Python que reciba un número entero positivo en base
# decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        # n // 2 devuelve la parte entera de la división
        # n % 2 devuelve el residuo de la división
        return decimal_a_binario(n // 2) + str(n % 2)
#5 Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
# cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
# lo es.
def es_palindromo(palabra):
    #si la longitud de la palabra es 0 o 1, es un palíndromo
    if len(palabra) <= 1:
        return True
    #compara el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1]) 
#6Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
#número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)
    
#7 Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
# bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
# último nivel con un solo bloque


def contar_bloques(n):
    if n == 0:
        return 0
    else:
        return n + contar_bloques(n - 1)
    
#8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
# número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
# aparece ese dígito dentro del número.
def contar_digito(numero, digito):
    # si el número es 0, no hay más dígitos que contar
    if numero == 0:
        return 0
    else:
        # si el último dígito del número es igual al dígito buscado
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)