import csv
from datetime import datetime
import os

filename ='Bitácora.csv'

def menu():
    print("Registro de Bitácoras - Empresa de Ferrocarriles del Estado")
    print("1.- Registrar nueva bitácora. ")
    print("2.- Listar Bitácoras realizadas. ")
    print("3.- Exportar bitácoras. ")
    print("4.-Salir del sistema")
    opcion = input("Seleccione una opción: ")
    return int(opcion)

def registrar_bitacora():
    fecha_registro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cantidad_vagones = int(input("Ingrese la cantidad de vagones (Hasta 10): "))
    mensaje_falla = input("Ingrese el mensaje de falla (Máximo 30 caracteres): ")
    nombre_responsable = input("Ingres eel nombre del responsable: ")

    if cantidad_vagones > 10:
        print("La cantidad máxima de vagones es de 10.")
        return
    
    filename = f"Bitácora {len(obtener_bitacoras()) + 1}.csv"

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Cantidad de Vagones", "Mensaje de Falla", "Nombre del Responsable"])
        writer.writerow([fecha_registro, cantidad_vagones, mensaje_falla, nombre_responsable])
    
    print(f"Bitácora registrada exitosamente en {filename}")

def listar_bitacoras():
    bitacoras = obtener_bitacoras()
    for i, bitacora in enumerate(bitacoras):
        print(f"\nBitácora {i+1}:")
        print(f"Fecha: {bitacora['Fecha']}")
        print(f"Cantidad de Vagones: {bitacora['Cantidad de Vagones']}")
        print(f"Mensaje de Falla: {bitacora['Mensaje de Falla']}")
        print(f"Nombre del Responsable: {bitacora['Nombre del Responsable']}\n")

def exportar_bitacoras():
    bitacoras = obtener_bitacoras()
    with open('Bitácoras.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Fecha", "Cantidad de Vagones", "Mensajke de Falla","Nombre del Responsable"])
        for bitacora in bitacoras:
            writer.writerow(list(bitacora.values()))
        
    

def obtener_bitacoras():
    bitacoras = []
    for i in range(1,100):
        filename = f"Bitácora {i}.csv"
        if os.path.exists(filename):
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    bitacora ={
                        "Fecha": row[0],
                        "Cantidad de Vagones": int(row[1]),
                        "Mensaje de Falla": row[2],
                        "Nombre del Responsable": row[3]
                    }
                    bitacoras.append(bitacora)
    return bitacoras

    


while True: 
    opcion = menu()
    if opcion == 1:
        registrar_bitacora()
    elif opcion == 2:
        listar_bitacoras()
    elif opcion == 3:
        exportar_bitacoras()
    elif opcion == 4:
        print("Chau bro")
        break
    else:
        print("Opción errónea. Por favor, intente nuevamente.")


