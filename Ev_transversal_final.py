# --- FUNCIONES DE VALIDACIÓN

# Valida que el titulo no este vacio ni sea solo espacios
def validar_titulo(titulo):
    # .strip() elimina espacios al inicio y final. Si queda vacio, retorna False
    if titulo.strip() == "":
        return False
    return True


# Valida que las copias sean un entero mayor o igual a cero
def validar_copias(copias_str):
    try:
        valor = int(copias_str)
        if valor >= 0:
            return True
        return False
    except ValueError:
        
        return False


# Valida que los dias de prestamo sean un entero mayor a cero
def validar_prestamo(prestamo_str):
    try:
        valor = int(prestamo_str)
        if valor > 0:
            return True
        return False
    except ValueError:
        return False


# Solo muestra las opciones en pantalla sin retornar nada
def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


# Lee la opcion elegida, la valida y la retorna
def pedir_opcion():
    while True:
        opcion = input("Seleccione una opción (1-6): ").strip()
        if opcion in ["1", "2", "3", "4", "5", "6"]:
            return opcion
        print("Error: Opción inválida. Intente nuevamente.")



#  Agrega un libro validando cada campo por separado
def agregar_libro(lista_libros):
    print("\n--- AGREGAR NUEVO LIBRO ---")
    
    titulo = input("Ingrese el título del libro: ")
    if not validar_titulo(titulo):
        print("Error: El nombre no puede estar vacío ni ser solo espacios en blanco.")
        return 

    copias_raw = input("Ingrese la cantidad de copias: ")
    if not validar_copias(copias_raw):
        print("Error: Las copias deben ser un número entero mayor o igual que cero.")
        return

    prestamo_raw = input("Ingrese el período de préstamo en días: ")
    if not validar_prestamo(prestamo_raw):
        print("Error: El período de préstamo debe ser un número entero mayor que cero.")
        return

    
    nuevo_libro = {
        "titulo": titulo.strip(),
        "copias": int(copias_raw),
        "prestamo": int(prestamo_raw),
        "disponible": False 
    }
    
    lista_libros.append(nuevo_libro)
    print(f"¡Libro '{titulo}' registrado exitosamente!")


#  Busca un libro y retorna su posicion en la lista, o -1 si no existe
def buscar_libro(lista_libros, titulo_buscar):
   
    for i in range(len(lista_libros)):
        
        if lista_libros[i]["titulo"].lower() == titulo_buscar.lower():
            return i # Retorna la posicion del libro
    return -1 


# Elimina un libro usando la funcion de busqueda anterior
def eliminar_libro(lista_libros):
    print("\n--- ELIMINAR LIBRO ---")
    titulo_eliminar = input("Ingrese el título del libro que desea eliminar: ").strip()
    
    # Buscamos la posicion del libro
    posicion = buscar_libro(lista_libros, titulo_eliminar)
    
    if posicion != -1:
       
        libro_eliminado = lista_libros.pop(posicion)
        print(f"El libro '{libro_eliminado['titulo']}' fue eliminado con éxito.")
    else:
        print(f"El libro '{titulo_eliminar}' no se encuentra registrado.")


# Actualiza el estado disponible de todos los libros de la lista
def actualizar_disponibilidad(lista_libros):
    for libro in lista_libros:
        if libro["copias"] >= 1:
            libro["disponible"] = True
        else:
            libro["disponible"] = False


# Actualiza disponibilidades y muestra el listado formateado
def mostrar_libros(lista_libros):
    
    actualizar_disponibilidad(lista_libros)
    
    print("\n=== LISTA DE LIBROS ===")
    if len(lista_libros) == 0:
        print("No hay libros registrados en la biblioteca.")
        return
        
    for libro in lista_libros:
       
        estado_texto = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
        
        print(f"Título: {libro['titulo']}")
        print(f"Copias: {libro['copias']}")
        print(f"Préstamo: {libro['prestamo']}")
        print(f"Estado: {estado_texto}")
        print("********************************************")




def main():
  
    biblioteca = []
    
    while True:
        mostrar_menu()
        opcion = pedir_opcion()
        
        if opcion == "1":
            agregar_libro(biblioteca)
            
        elif opcion == "2":
            print("\n--- BUSCAR LIBRO ---")
            titulo_buscar = input("Ingrese el título a buscar: ").strip()
            
            pos = buscar_libro(biblioteca, titulo_buscar)
            
            
            if pos != -1:
                libro = biblioteca[pos]
                estado_actual = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
                print(f"\n[Libro Encontrado en posición {pos}]")
                print(f"Título: {libro['titulo']} | Copias: {libro['copias']} | Préstamo: {libro['prestamo']} días | Estado: {estado_actual}")
            else:
                print("El libro no se encuentra registrado.")
                
        elif opcion == "3":
            eliminar_libro(biblioteca)
            
        elif opcion == "4":
            actualizar_disponibilidad(biblioteca)
            print("\n¡Disponibilidad de todos los libros actualizada correctamente!")
            
        elif opcion == "5":
            mostrar_libros(biblioteca)
            
        elif opcion == "6":
            print("\nGracias por usar el sistema. Vuelva Pronto")
            break



if __name__ == "__main__":
    main()