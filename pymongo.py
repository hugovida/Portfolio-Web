import pymongo

def conectar_a_mongodb(url="mongodb://localhost:27017/", nombre_base_datos="colegio"):
    
    try:
        cliente = MongoClient(url)
        base_de_datos = cliente[nombre_base_datos]
        print("Conexión exitosa a la base de datos.")
        return base_de_datos
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None


    
# Función para crear una colección en la base de datos
def crear_coleccion(db, nombre_coleccion):
    try:
        return db.create_collection(nombre_coleccion)
    except Exception as e:
        print(f"Error al crear la colección: {e}")
        return None

# Función para insertar un documento en una colección
def insertar_documento(coleccion, documento):
    try:
        coleccion.insert_one(documento)
        print("Documento insertado exitosamente.")
    except Exception as e:
        print(f"Error al insertar documento: {e}")

# Función para buscar documentos en una colección
def buscar_documentos(coleccion, filtro):
    try:
        resultados = coleccion.find(filtro)
        print("\nResultados de la búsqueda:")
        for resultado in resultados:
            print(resultado)
    except Exception as e:
        print(f"Error al buscar documentos: {e}")

# Función para actualizar documentos en una colección
def actualizar_documento(coleccion, filtro, actualizacion):
    try:
        resultado = coleccion.update_many(filtro, actualizacion)
        print(f"{resultado.modified_count} documentos actualizados exitosamente.")
    except Exception as e:
        print(f"Error al actualizar documentos: {e}")

# Menú principal
def menu():
    db = None
    coleccion = None

    while True:
        print("\n------ Menú Principal ------")
        print("1. Conexión a la base de datos")
        print("2. Crear una colección")
        print("3. Insertar documento")
        print("4. Buscar documentos")
        print("5. Actualizar documentos")
        print("0. Salir")

        opcion = input("Ingrese la opción deseada: ")

        if opcion == "1":
            db = conectar_a_mongodb()

        elif opcion == "2":
            if db:
                nombre_coleccion = input("Ingrese el nombre de la colección: ")
                coleccion = crear_coleccion(db, nombre_coleccion)
                if coleccion:
                    print(f"Colección '{nombre_coleccion}' creada exitosamente.")
            else:
                print("Primero debes conectar a la base de datos.")

        elif opcion == "3":
            if coleccion:
                documento = {
                    "nombre": input("Nombre del estudiante: "),
                    "edad": int(input("Edad del estudiante: ")),
                    "grado": int(input("Grado del estudiante: ")),
                    "materias": input("Materias del estudiante (separadas por comas): ").split(",")
                }
                insertar_documento(coleccion, documento)
            else:
                print("Primero debes crear una colección.")

        elif opcion == "4":
            if coleccion:
                nombre = input("Ingrese el nombre para la búsqueda: ")
                buscar_documentos(coleccion, {"nombre": nombre})
            else:
                print("Primero debes crear una colección.")

        elif opcion == "5":
            if coleccion:
                nombre = input("Ingrese el nombre del estudiante a actualizar: ")
                actualizacion = {
                    "$set": {
                        "edad": int(input("Nueva edad del estudiante: ")),
                        "grado": int(input("Nuevo grado del estudiante: "))
                    }
                }
                actualizar_documento(coleccion, {"nombre": nombre}, actualizacion)
            else:
                print("Primero debes crear una colección.")

        elif opcion == "0":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    menu()
