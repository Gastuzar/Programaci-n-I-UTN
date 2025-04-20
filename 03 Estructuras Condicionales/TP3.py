#1)
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

#2)
nota = int(input("Ingrese su nota: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")	

#3)
numero = int(input("Ingrese un numero par: "))
if numero % 2 == 0:
    print("El numero ingresado es par")
else:
    print("Por favor, ingrese un número par")

#4)
edad = int(input("Ingrese su edad: "))
if edad < 12:
    print("Es un niño")
elif 12 <= edad < 18:
    print("Es un adolescente")
elif 18 <= edad < 30:
    print("Es un adulto joven")
else:
    print("Es un adulto")

#5)
password = input("Ingrese su contraseña de 8 a 14 caracteres: ")
if len(password) >= 8 and len(password) <= 14:
    print("La contraseña es correcta")
else:
    print("Por favor, ingrese una contraseña de 8 a 14 caracteres")

#6)
from statistics import mean, median, mode
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

print("Lista de números aleatorios:", numeros_aleatorios)
print("La moda es:", mode(numeros_aleatorios))
print("La media es:", mean(numeros_aleatorios))
print("La mediana es:", median(numeros_aleatorios))
if mean(numeros_aleatorios) > median(numeros_aleatorios) and median(numeros_aleatorios) > mode(numeros_aleatorios):
    print("Hay sesgp positivo o a la derecha")
elif mean(numeros_aleatorios) < median(numeros_aleatorios) and median(numeros_aleatorios) < mode(numeros_aleatorios):
    print("Hay sesgo negativo o a la izquierda")
else:
    print("No hay sesgo")

#7)
frase = input("Ingrese una frase: ")
frasemin = frase.lower()
if frasemin[-1] == "a" or frasemin[-1] == "e" or frasemin[-1] == "i" or frasemin[-1] == "o" or frasemin[-1] == "u":
    print(frase,"!")
else:
    print(frase)

#8)
nombre = input("Ingrese su nombre: ")
opcion1 = int(input("Desea convertir su nombre a mayúsculas, elija la opcion 1: "))
opcion2 = int(input("Desea convertir su nombre a minusculas, elija la opcion 2: "))
opcion3 = int(input("Desea convertir la primer letra de su nombre a mayúsculas, elija la opcion 3: "))
if opcion1 == 1:
    print("Su nombre en mayúsculas es:", nombre.upper())
elif opcion2 == 2:
    print("Su nombre en minusculas es:", nombre.lower())
elif opcion3 == 3:
    print("Su nombre con la primer letra en mayúsculas es:", nombre.title())
else:
    print("Opción no válida")

#9)
terremoto = int(input("Ingrese la magnitud del terremoto: "))
if terremoto <3:
    print("El terremoto es de magnitud 'Muy leve'")
elif 4 <= terremoto < 4:
    print("El terremoto es de magnitud 'Leve'")
elif 4 <= terremoto < 5:
    print("El terremoto es de magnitud 'Moderado'")
elif 5 <= terremoto < 6:
    print("El terremoto es de magnitud 'Fuerte'")
elif 6 <= terremoto < 7:
    print("El terremoto es de magnitud 'Muy Fuerte'")
else:
    print("El terremoto es de magnitud 'Extremo'")

#10)
hemisferio = input("Ingrese el hemisferio (Norte o Sur): ").lower()
mes = input("Ingrese el mes: ").lower()	
dia = input("Ingrese el dia: ").lower()
if hemisferio == "norte" and (mes == "diciembre"and(dia >= 21 and dia <= 31) or mes == "enero" or mes == "febrero" or mes == "marzo" and(dia >= 1 and dia <= 20)):
    print("Estamos en invierno")
elif hemisferio == "norte" and (mes == "marzo"and(dia >= 21 and dia <= 31) or mes == "abril" or mes == "mayo" or mes == "junio" and(dia >= 1 and dia <= 20)):
    print("Estamos en primavera")
elif hemisferio == "norte" and (mes == "junio"and(dia >= 21 and dia <= 31) or mes == "julio" or mes == "agosto" or mes == "septiembre" and(dia >= 1 and dia <= 20)):
    print("Estamos en verano")
elif hemisferio == "norte" and (mes == "septiembre"and(dia >= 21 and dia <= 31) or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and(dia >= 1 and dia <= 20)):
    print("Estamos en otoño")
elif hemisferio == "sur" and (mes == "diciembre"and(dia >= 21 and dia <= 31) or mes == "enero" or mes == "febrero" or mes == "marzo" and(dia >= 1 and dia <= 20)):
    print("Estamos en verano")
elif hemisferio == "sur" and (mes == "marzo"and(dia >= 21 and dia <= 31) or mes == "abril" or mes == "mayo" or mes == "junio" and(dia >= 1 and dia <= 20)):
    print("Estamos en primavera")
elif hemisferio == "sur" and (mes == "junio"and(dia >= 21 and dia <= 31) or mes == "julio" or mes == "agosto" or mes == "septiembre" and(dia >= 1 and dia <= 20)):
    print("Estamos en verano")
elif hemisferio == "sur" and (mes == "septiembre"and(dia >= 21 and dia <= 31) or mes == "octubre" or mes == "noviembre" or mes == "diciembre" and(dia >= 1 and dia <= 20)):
    print("Estamos en otoño")
else:
    print("Mes o dia no valido")