#1
print("\n1) AÑADIR FRUTAS AL DICCIONARIO")


precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
print("Diccionario inicial:", precios_frutas)

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Después de añadir frutas:", precios_frutas)

#2
print("\n2) ACTUALIZAR PRECIOS")



precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Después de actualizar precios:", precios_frutas)

#3
print("\n3) LISTA SOLO CON NOMBRES DE FRUTAS")
print("-" * 35)

lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

#4
print("\n4) AGENDA TELEFÓNICA")
print("-" * 20)

def agenda_telefonica():
    contactos = {}
    
    print("Ingresa 5 contactos:")
    for i in range(5):
        nombre = input(f"Nombre del contacto {i+1}: ")
        telefono = input(f"Teléfono de {nombre}: ")
        contactos[nombre] = telefono
    
    print("\nContactos guardados:", contactos)
    
    # Consultar contacto
    nombre_buscar = input("\nIngresa el nombre a buscar: ")
    if nombre_buscar in contactos:
        print(f"El teléfono de {nombre_buscar} es: {contactos[nombre_buscar]}")
    else:
        print(f"No se encontró el contacto {nombre_buscar}")

agenda_telefonica()


# 5
print("\n5) ANÁLISIS DE FRASE")


def analizar_frase(frase):
    palabras = frase.lower().split()
    
    palabras_unicas = set(palabras)
    print("Palabras únicas:", palabras_unicas)
    
    contador_palabras = {}
    for palabra in palabras:
        contador_palabras[palabra] = contador_palabras.get(palabra, 0) + 1
    
    print("Frecuencia de palabras:", contador_palabras)


frase_ejemplo = "hola mundo hola python mundo"
print(f"Frase ejemplo: '{frase_ejemplo}'")
analizar_frase(frase_ejemplo)

#6
print("\n6) PROMEDIOS DE ALUMNOS")


def calcular_promedios():
    alumnos_notas = {}
    
    print("Ingresa datos de 3 alumnos:")
    for i in range(3):
        nombre = input(f"Nombre del alumno {i+1}: ")
        nota1 = float(input(f"Nota 1 de {nombre}: "))
        nota2 = float(input(f"Nota 2 de {nombre}: "))
        nota3 = float(input(f"Nota 3 de {nombre}: "))
        
        notas = (nota1, nota2, nota3)
        alumnos_notas[nombre] = notas
    
    print("\nPromedios:")
    for nombre, notas in alumnos_notas.items():
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")

alumnos_ejemplo = {
    "Juan": (8.5, 7.0, 9.0),
    "María": (9.5, 8.5, 9.0),
    "Pedro": (7.0, 6.5, 8.0)
}

print("Ejemplo de alumnos y notas:")
for nombre, notas in alumnos_ejemplo.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: Notas {notas} - Promedio: {promedio:.2f}")

#7
print("\n7) ANÁLISIS DE SETS DE ESTUDIANTES")
print("-" * 35)

parcial1 = {101, 102, 103, 104, 105, 106}
parcial2 = {103, 104, 105, 107, 108, 109}

print("Estudiantes que aprobaron Parcial 1:", parcial1)
print("Estudiantes que aprobaron Parcial 2:", parcial2)

ambos_parciales = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos_parciales)

solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los dos:", solo_uno)

al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#8
print("\n8) SISTEMA DE INVENTARIO")
print("-" * 25)

def sistema_inventario():
    inventario = {
        "Manzanas": 50,
        "Peras": 30,
        "Bananas": 25,
        "Naranjas": 40
    }
    
    while True:
        print("\n--- SISTEMA DE INVENTARIO ---")
        print("1. Consultar stock")
        print("2. Agregar stock")
        print("3. Agregar nuevo producto")
        print("4. Ver inventario completo")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            producto = input("Ingresa el producto a consultar: ")
            if producto in inventario:
                print(f"Stock de {producto}: {inventario[producto]} unidades")
            else:
                print(f"El producto {producto} no existe en el inventario")
        
        elif opcion == "2":
            producto = input("Ingresa el producto: ")
            if producto in inventario:
                cantidad = int(input("Cantidad a agregar: "))
                inventario[producto] += cantidad
                print(f"Stock actualizado. {producto}: {inventario[producto]} unidades")
            else:
                print(f"El producto {producto} no existe. Usa la opción 3 para agregarlo.")
        
        elif opcion == "3":
            producto = input("Ingresa el nuevo producto: ")
            if producto not in inventario:
                cantidad = int(input("Ingresa el stock inicial: "))
                inventario[producto] = cantidad
                print(f"Producto {producto} agregado con {cantidad} unidades")
            else:
                print(f"El producto {producto} ya existe")
        
        elif opcion == "4":
            print("Inventario completo:")
            for producto, stock in inventario.items():
                print(f"  {producto}: {stock} unidades")
        
        elif opcion == "5":
            break
        
        else:
            print("Opción inválida")

inventario_ejemplo = {"Manzanas": 50, "Peras": 30, "Bananas": 25}
print("Ejemplo de inventario:", inventario_ejemplo)
print("Consultando stock de Manzanas:", inventario_ejemplo.get("Manzanas", "No encontrado"))

#9
print("\n9) AGENDA DE EVENTOS")
print("-" * 20)

def crear_agenda():
    agenda = {
        ("Lunes", "09:00"): "Reunión de equipo",
        ("Lunes", "14:00"): "Cita médica",
        ("Martes", "10:00"): "Presentación proyecto",
        ("Miércoles", "16:00"): "Dentista",
        ("Jueves", "11:00"): "Llamada cliente",
        ("Viernes", "15:00"): "Revisión código"
    }
    
    print("Agenda actual:")
    for (dia, hora), evento in agenda.items():
        print(f"  {dia} {hora}: {evento}")
    
    dia_consulta = input("\nIngresa el día a consultar: ")
    hora_consulta = input("Ingresa la hora a consultar: ")
    
    clave_consulta = (dia_consulta, hora_consulta)
    if clave_consulta in agenda:
        print(f"Evento: {agenda[clave_consulta]}")
    else:
        print("No hay eventos programados para ese día y hora")

agenda_ejemplo = {
    ("Lunes", "09:00"): "Reunión de equipo",
    ("Martes", "14:00"): "Cita médica",
    ("Miércoles", "10:00"): "Presentación"
}
print("Ejemplo de agenda:", agenda_ejemplo)
print("Consultando Lunes 09:00:", agenda_ejemplo.get(("Lunes", "09:00"), "Sin eventos"))

#10
print("\n10) INVERTIR DICCIONARIO PAÍSES-CAPITALES")
print("-" * 42)

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasília",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "Paraguay": "Asunción",
    "Bolivia": "Sucre",
    "Perú": "Lima",
    "Colombia": "Bogotá"
}

print("Diccionario original (País -> Capital):")
for pais, capital in paises_capitales.items():
    print(f"  {pais}: {capital}")

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}

print("\nDiccionario invertido (Capital -> País):")
for capital, pais in capitales_paises.items():
    print(f"  {capital}: {pais}")

