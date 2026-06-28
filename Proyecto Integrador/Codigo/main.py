import json
import os

ARCHIVO = "incidentes.json"

incidentes = []

tipos_incidente = ("Alarma", "Robo", "Hurto", "Falla técnica", "Emergencia")
estados = ("Pendiente", "En proceso", "Finalizado")

if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        incidentes = json.load(archivo)

while True:
    print("\n______________SISTEMA DE INCIDENTES ______________")
    print("1. Registrar incidente")
    print("2. Ver incidentes")
    print("3. Buscar incidente")
    print("4. Cambiar estado")
    print("5. Eliminar incidente")
    print("6. Estadísticas")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("\n--- REGISTRAR INCIDENTE ---")

        codigo = input("Código del incidente: ")

        repetido = False
        for incidente in incidentes:
            if incidente["codigo"] == codigo:
                repetido = True
                break

        if repetido:
            print("Ya existe un incidente con ese código.")
            continue

        fecha = input("Fecha: ")
        lugar = input("Lugar: ")

        print("\nTipos de incidente:")
        for i in range(len(tipos_incidente)):
            print(f"{i + 1}. {tipos_incidente[i]}")

        tipo_opcion = input("Seleccione el tipo de incidente: ")

        if not tipo_opcion.isdigit():
            print("Debe ingresar un número.")
            continue

        tipo_opcion = int(tipo_opcion)

        if tipo_opcion >= 1 and tipo_opcion <= len(tipos_incidente):
            tipo = tipos_incidente[tipo_opcion - 1]
        else:
            print("Tipo inválido.")
            continue

        responsable = input("Responsable: ")
        descripcion = input("Descripción: ")
        estado = estados[0]

        incidente = {
            "codigo": codigo,
            "fecha": fecha,
            "lugar": lugar,
            "tipo": tipo,
            "responsable": responsable,
            "descripcion": descripcion,
            "estado": estado
        }

        incidentes.append(incidente)

        with open(ARCHIVO, "w", encoding="utf-8") as archivo:
            json.dump(incidentes, archivo, indent=4, ensure_ascii=False)

        print("Incidente registrado correctamente.")

    elif opcion == "2":
        print("\n--- LISTA DE INCIDENTES ---")

        if len(incidentes) == 0:
            print("No existen incidentes registrados.")
        else:
            for incidente in incidentes:
                print("______________")
                print("Código:", incidente["codigo"])
                print("Fecha:", incidente["fecha"])
                print("Lugar:", incidente["lugar"])
                print("Tipo:", incidente["tipo"])
                print("Responsable:", incidente["responsable"])
                print("Descripción:", incidente["descripcion"])
                print("Estado:", incidente["estado"])

    elif opcion == "3":
        print("\n--- BUSCAR INCIDENTE ---")

        codigo_buscar = input("Ingrese el código del incidente: ")
        encontrado = False

        for incidente in incidentes:
            if incidente["codigo"] == codigo_buscar:
                print("\nIncidente encontrado:")
                print("Código:", incidente["codigo"])
                print("Fecha:", incidente["fecha"])
                print("Lugar:", incidente["lugar"])
                print("Tipo:", incidente["tipo"])
                print("Responsable:", incidente["responsable"])
                print("Descripción:", incidente["descripcion"])
                print("Estado:", incidente["estado"])
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un incidente con ese código.")

    elif opcion == "4":
        print("\n--- CAMBIAR ESTADO ---")

        codigo_buscar = input("Ingrese el código del incidente: ")
        encontrado = False

        for incidente in incidentes:
            if incidente["codigo"] == codigo_buscar:
                encontrado = True

                print("\nEstados disponibles:")
                for i in range(len(estados)):
                    print(f"{i + 1}. {estados[i]}")

                estado_opcion = input("Seleccione el nuevo estado: ")

                if not estado_opcion.isdigit():
                    print("Debe ingresar un número.")
                    continue

                estado_opcion = int(estado_opcion)

                if estado_opcion >= 1 and estado_opcion <= len(estados):
                    incidente["estado"] = estados[estado_opcion - 1]

                    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                        json.dump(incidentes, archivo, indent=4, ensure_ascii=False)

                    print("Estado actualizado correctamente.")
                else:
                    print("Estado inválido.")
                break

        if not encontrado:
            print("No se encontró el incidente.")

    elif opcion == "5":
        print("\n--- ELIMINAR INCIDENTE ---")

        codigo_buscar = input("Ingrese el código del incidente: ")
        encontrado = False

        for incidente in incidentes:
            if incidente["codigo"] == codigo_buscar:
                incidentes.remove(incidente)
                encontrado = True

                with open(ARCHIVO, "w", encoding="utf-8") as archivo:
                    json.dump(incidentes, archivo, indent=4, ensure_ascii=False)

                print("Incidente eliminado correctamente.")
                break

        if not encontrado:
            print("No se encontró el incidente.")

    elif opcion == "6":
        print("\n--- ESTADÍSTICAS ---")

        total = len(incidentes)
        pendientes = 0
        proceso = 0
        finalizados = 0

        for incidente in incidentes:
            if incidente["estado"] == "Pendiente":
                pendientes += 1
            elif incidente["estado"] == "En proceso":
                proceso += 1
            elif incidente["estado"] == "Finalizado":
                finalizados += 1

        print("Total de incidentes:", total)
        print("Pendientes:", pendientes)
        print("En proceso:", proceso)
        print("Finalizados:", finalizados)

    elif opcion == "7":
        print("Gracias por usar el sistema.")
        break

    else:
        print("Opción inválida. Intente nuevamente.")