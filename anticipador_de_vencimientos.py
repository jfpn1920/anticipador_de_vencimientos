import random
ids = []
nombres = []
descripciones = []
categorias = []
fechas_registro = []
fechas_vencimiento = []
estados = []
observaciones = []
#------------------------------------------------#
#--|menu_principal_anticipador_de_vencimientos|--#
#------------------------------------------------#
while True:
    print("menu principal anticipador de vencimientos")
    print("1) crear registro")
    print("2) editar registro")
    print("3) eliminar registro")
    print("4) buscar registro")
    print("5) lista de datos")
    print("6) salir")
    opcion = input("seleccione una opción: ")
    #--------------------#
    #--|crear_registro|--#
    #--------------------#
    if opcion == "1":
        if len(ids) == 0:
            id_registro = 1
        else:
            id_registro = ids[-1] + 1
        nombre = input("nombre: ")
        descripcion = input("descripción: ")
        categoria = input("categoría: ")
        fecha_registro = input("fecha de registro: ")
        fecha_vencimiento = input("fecha de vencimiento: ")
        estado = input("estado (vigente, próximo a vencer o vencido): ")
        observacion = input("observación: ")
        ids.append(id_registro)
        nombres.append(nombre)
        descripciones.append(descripcion)
        categorias.append(categoria)
        fechas_registro.append(fecha_registro)
        fechas_vencimiento.append(fecha_vencimiento)
        estados.append(estado)
        observaciones.append(observacion)
        print("registro creado correctamente.")
        print("id:", id_registro)
    #---------------------#
    #--|editar_registro|--#
    #---------------------#
    elif opcion == "2":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("editar registro")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos actuales")
                print(f"{ids[posicion]} | {nombres[posicion]} | {fechas_vencimiento[posicion]}")
                nombres[posicion] = input("nuevo nombre: ")
                descripciones[posicion] = input("nueva descripción: ")
                categorias[posicion] = input("nueva categoría: ")
                fechas_registro[posicion] = input("nueva fecha de registro: ")
                fechas_vencimiento[posicion] = input("nueva fecha de vencimiento: ")
                estados[posicion] = input("nuevo estado: ")
                observaciones[posicion] = input("nueva observación: ")
                print("registro actualizado correctamente.")
            else:
                print("id no encontrada.")
    #-----------------------#
    #--|eliminar_registro|--#
    #-----------------------#
    elif opcion == "3":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("eliminar registro")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("datos del registro")
                print(f"{ids[posicion]} | {nombres[posicion]} | {fechas_vencimiento[posicion]}")
                respuesta = input("¿desea eliminar este registro? (s/n): ")
                if respuesta.upper() == "S":
                    ids.pop(posicion)
                    nombres.pop(posicion)
                    descripciones.pop(posicion)
                    categorias.pop(posicion)
                    fechas_registro.pop(posicion)
                    fechas_vencimiento.pop(posicion)
                    estados.pop(posicion)
                    observaciones.pop(posicion)
                    print("registro eliminado correctamente.")
                else:
                    print("el registro no fue eliminado.")
            else:
                print("id no encontrada.")
    #---------------------#
    #--|buscar_registro|--#
    #---------------------#
    elif opcion == "4":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            print("buscar registro")
            id_buscar = int(input("ingrese la id del registro: "))
            if id_buscar in ids:
                posicion = ids.index(id_buscar)
                print("id:", ids[posicion])
                print("nombre:", nombres[posicion])
                print("descripción:", descripciones[posicion])
                print("categoría:", categorias[posicion])
                print("fecha de registro:", fechas_registro[posicion])
                print("fecha de vencimiento:", fechas_vencimiento[posicion])
                print("estado:", estados[posicion])
                print("observación:", observaciones[posicion])
            else:
                print("id no encontrada.")
    #-----------------#
    #--|lista_datos|--#
    #-----------------#
    elif opcion == "5":
        if len(ids) == 0:
            print("no existen registros.")
        else:
            vigentes = 0
            proximos = 0
            vencidos = 0
            print("lista de datos")
            for i in range(len(ids)):
                print(f"{ids[i]} | {nombres[i]} | {categorias[i]} | {estados[i]}")
                if estados[i].lower() == "vigente":
                    vigentes += 1
                elif estados[i].lower() == "próximo a vencer" or estados[i].lower() == "proximo a vencer":
                    proximos += 1
                elif estados[i].lower() == "vencido":
                    vencidos += 1
            print("estadísticas anticipador de vencimientos")
            print("cantidad de registros:", len(ids))
            print("vigentes:", vigentes)
            print("próximos a vencer:", proximos)
            print("vencidos:", vencidos)
            posicion = random.randint(0, len(ids) - 1)
            print("registro seleccionado")
            print("id:", ids[posicion])
            print("nombre:", nombres[posicion])
            print("descripción:", descripciones[posicion])
            print("categoría:", categorias[posicion])
            print("fecha de registro:", fechas_registro[posicion])
            print("fecha de vencimiento:", fechas_vencimiento[posicion])
            print("estado:", estados[posicion])
            print("observación:", observaciones[posicion])
    #------------------------------#
    #--|salir_del_menu_principal|--#
    #------------------------------#
    elif opcion == "6":
        print("gracias por utilizar el anticipador de vencimientos.")
        break
    else:
        print("opción no válida.")