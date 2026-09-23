from datetime import datetime

from paciente import Paciente
from medico import Medico
from cita import Cita

pacientes = []
medicos = []
citas = []

def pedir_texto(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("Este dato es obligatorio.\n")


def pedir_nombre(mensaje):
    while True:
        valor = input(mensaje).strip()
        if not valor:
            print("El nombre es obligatorio.\n")
        elif not all(parte.replace(".", "").isalpha() for parte in valor.split()):
            print("El nombre no puede contener números.\n")
        else:
            return valor


def pedir_edad(mensaje):
    
    while True:
        valor = input(mensaje).strip()
        try:
            edad = int(valor)
        except ValueError:
            print("La edad es obligatoria y debe ser un número, no letras.\n")
            continue
        if edad < 0:
            print("La edad no puede ser negativa.\n")
        elif edad > 100:
            print("La edad es irreal.\n")
        else:
            return edad


def pedir_fecha(mensaje):
    while True:
        valor = input(mensaje).strip()
        try:
            datetime.strptime(valor, "%d/%m/%Y")
            return valor
        except ValueError:
            print("Fecha inválida. Usa el formato dd/mm/aaaa (ej: 15/09/2026).\n")

def buscar_por_codigo(lista, codigo):
    return next((elemento for elemento in lista if elemento.codigo == codigo), None)


def pedir_codigo_nuevo(lista, mensaje):
    while True:
        codigo = pedir_texto(mensaje)
        if buscar_por_codigo(lista, codigo) is None:
            return codigo
        print(f"El código '{codigo}' ya está registrado. Ingresa uno distinto.\n")


def obtener_existente(lista, mensaje, etiqueta):
    codigo = pedir_texto(mensaje)
    elemento = buscar_por_codigo(lista, codigo)
    if elemento is None:
        print(f"Referencia inválida: {etiqueta} '{codigo}' no existe.\n")
    return elemento


def pedir_especialidad(mensaje="Elige una especialidad:"):
    print(mensaje)
    for numero, especialidad in enumerate(Medico.ESPECIALIDADES, start=1):
        print(f"  {numero}. {especialidad}")
    while True:
        opcion = input("Opción: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= len(Medico.ESPECIALIDADES):
            return Medico.ESPECIALIDADES[int(opcion) - 1]
        print("Opción inválida.\n")


def crear_persona(tipo, codigo, nombre, dato_extra):
    if tipo == "paciente":
        return Paciente(codigo, nombre, dato_extra)
    elif tipo == "medico":
        return Medico(codigo, nombre, dato_extra)
    raise ValueError("Tipo de persona no reconocido.")


def registrar_paciente():
    print("\n--- Registro de Paciente ---")
    codigo = pedir_codigo_nuevo(pacientes, "Código del paciente: ")
    nombre = pedir_nombre("Nombre del paciente: ")
    edad = pedir_edad("Edad del paciente: ")
    try:
        pacientes.append(crear_persona("paciente", codigo, nombre, edad))
    except ValueError as error:
        print(f" No se pudo registrar el paciente: {error}\n")
        return
    print(f" Paciente registrado con éxito: {pacientes[-1].resumen()}\n")


def registrar_medico():
    print("\n--- Registro de Médico ---")
    codigo = pedir_codigo_nuevo(medicos, "Código del médico: ")
    nombre = pedir_nombre("Nombre del médico: ")
    especialidad = pedir_especialidad()
    try:
        medicos.append(crear_persona("medico", codigo, nombre, especialidad))
    except ValueError as error:
        print(f"No se pudo registrar al médico: {error}\n")
        return
    print(f"Médico registrado con éxito: {medicos[-1].resumen()}\n")


def buscar_registro():
    print("\n--- Buscar por código ---")
    tipo = pedir_texto("¿Buscar en (paciente/medico)? ").strip().lower()
    lista = {"paciente": pacientes, "medico": medicos}.get(tipo)
    if lista is None:
        print("Opción inválida,escribe paciente o medico.\n")
        return

    resultado = obtener_existente(lista, "Codigo a buscar: ", f"el {tipo}")
    if resultado is not None:
        print(f"Encontrado: {resultado.resumen()}\n")


def programar_cita():
    print("\n--- Registro de Cita ---")
    if not pacientes or not medicos:
        print("Debes registrar al menos un paciente y un médico antes de programar una cita.\n")
        return

    paciente = obtener_existente(pacientes, "Código del paciente (debe existir): ", "el paciente")
    if paciente is None:
        return
    medico = obtener_existente(medicos, "Código del médico (debe existir): ", "el médico")
    if medico is None:
        return

    codigo = pedir_codigo_nuevo(citas, "Código de la cita: ")
    fecha = pedir_fecha("Fecha de la cita (dd/mm/aaaa): ")

    try:
        citas.append(Cita(codigo, paciente, medico, fecha))
    except ValueError as error:
        print(f"No se pudo programar la cita: {error}\n")
        return
    print(f"La cita se programo con éxito\n{citas[-1].resumen()}\n")


while True:
    print("1. Registrar paciente")
    print("2. Registrar médico")
    print("3. Programar cita")
    print("4. Buscar por código")
    print("5. Salir")

    opcion = input("\nElige una opcion: ").strip()

    if opcion == "1":
        registrar_paciente()
    elif opcion == "2":
        registrar_medico()
    elif opcion == "3":
        programar_cita()
    elif opcion == "4":
        buscar_registro()
    elif opcion == "5":
        break
    else:
        print("\n Opcion invalida\n")
