#1
def imprimir_hola_mundo():
    return "Hola Mundo"
imprimir_hola_mundo()
#2
def saludar_usuario(nombre):
    return "Hola " + nombre
print(saludar_usuario(input("Ingrese su nombre: ")))

#3
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, Tengo {edad} y vivo en {residencia}"

print(informacion_personal(input("Ingrese su nombre: "), input("Ingrese su apellido: "), input("Ingrese su edad: "), input("Ingrese su residencia: ")))

#4
def calcular_area_circulo(radio):
    pi = 3.14
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    pi = 3.14
    return 2 * pi * radio
radio = float(input("Ingrese el radio del círculo: "))
print("El área del círculo es:", calcular_area_circulo(radio), "\nEl perímetro del círculo es:", calcular_perimetro_circulo(radio))

#5
def  segundos_a_horas(segundos):
    horas = segundos // 3600
    return horas
print("La cantidad de horas es:", segundos_a_horas(int(input("Ingrese la cantidad de segundos: "))))

#6
def  tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
print(tabla_multiplicar(int(input("Ingrese un número: "))))

#7
def operaciones_basicas(a, b):
    try:
        suma = a + b
        resta = a - b
        multiplicacion = a * b
        division = a / b
        return f"Suma: {suma}, Resta: {resta}, Multiplicación: {multiplicacion}, División: {division}"
    except ZeroDivisionError:
        return "Error: División por cero no permitida."
        
print(operaciones_basicas(int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: "))))

#8
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    #El :.2f es para limitar la cantidad de decimales a 2
    return f"Tu IMC es: {imc:.2f}"

print(calcular_imc(float(input("Ingrese su peso en kg: ")), float(input("Ingrese su altura en metros: "))))

#9
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    #El :.2f es para limitar la cantidad de decimales a 2
    return f"La temperatura en Fahrenheit es: {fahrenheit:.2f}"

print(celsius_a_fahrenheit(float(input("Ingrese la temperatura en Celsius: "))))
    
#10
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return f"El promedio es: {promedio:.2f}"
print(calcular_promedio(int(input("Ingrese el primer número: ")), int(input("Ingrese el segundo número: ")), int(input("Ingrese el tercer número: "))))