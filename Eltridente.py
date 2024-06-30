import cx_Oracle;

class conecta_Tridente ():
    def __init__(self):
        self.ConexionElTridente=cx_Oracle.connect(
            user = "TRIDENTE",
            password = "6217",
            dsn = "localhost/xe"
        );
        
        self.cursi = self.ConexionElTridente.cursor();
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
        print(".    .    .      .     .    CONEXION ESTABLECIDA A LA BD   .    .     .    . ");
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
        
    def verifica_nombre(self, Nom_prod):
        self.cursi.execute(f"select * from Producto WHERE Nom_prod = '{Nom_prod}'")
        return bool(self.cursi.fetchone())
    
    def verifica_id(self, ID_prod):
        self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_prod}")
        return bool(self.cursi.fetchone())
    
    def Muestra_producto_por_id(self, ID_prod):
        self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_prod}")
        registro = self.cursi.fetchone()
        if registro is None:
            print("No se encontró ningún producto con ese ID.")
        else:
            print(f"ID del producto: {registro[0]}, Nombre del producto: {registro[1]}, Descripción: {registro[2]}, Precio: {registro[3]}, Cantidad en stock: {registro[4]}, Categoría: {registro[5]}")
        
    def Ingresa_produc(self, Nom_prod, Descripcion, Precio, Cant_stock, Categoria):
        while Categoria not in ['Bidones', 'Envases']:
            print("Categoría no válida. Por favor, ingrese 'Bidones' o 'Envases'.")
            Categoria = input("Ingrese la categoría del producto: ")
        query = f"""
        INSERT INTO Producto (Nom_prod, Descripcion, Precio, Cant_stock, Categoria)
        VALUES ('{Nom_prod}', '{Descripcion}', {Precio}, {Cant_stock}, '{Categoria}')
        """
        self.cursi.execute(query)
        self.ConexionElTridente.commit()

    def Actualiza_produc(self, ID_prod, Nom_prod, Descripcion, Precio, Cant_stock, Categoria):
        while Categoria not in ['Bidones', 'Envases']:
            print("Categoría no válida. Por favor, ingrese 'Bidones' o 'Envases'.")
            Categoria = input("Ingrese la nueva categoría del producto: ")
        query = f"""
        UPDATE Producto
        SET Nom_prod = '{Nom_prod}', Descripcion = '{Descripcion}', Precio = {Precio}, Cant_stock = {Cant_stock}, Categoria = '{Categoria}'
        WHERE ID_prod = {ID_prod}
        """
        self.cursi.execute(query)
        self.ConexionElTridente.commit()

    def Elimina_produc(self, ID_prod):
        query = f"DELETE FROM Producto WHERE ID_prod = {ID_prod}"
        self.cursi.execute(query)
        self.ConexionElTridente.commit()

    def Muestra_productos(self):
        self.cursi.execute("SELECT * FROM Producto")
        Registros = self.cursi.fetchall()
        print(":::::::::::::::::::")
        print("Listado solicitado:")
        print(":::::::::::::::::::")
        print("")
        for registro in Registros:
            print(f"ID del producto: {registro[0]}, Nombre del producto: {registro[1]}, Descripción: {registro[2]}, Precio: {registro[3]}, Cantidad en stock: {registro[4]}, Categoría: {registro[5]}")
            print("")


def menu():
    Tridentisimo = conecta_Tridente()
    while True:
        print("1. Ingresar producto")
        print("2. Actualizar producto")
        print("3. Eliminar producto")
        print("4. Mostrar productos")
        print("5. Mostrar producto por ID")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            while True:
                Nom_prod = input("Ingrese el nombre del producto o 'salir' para regresar al menú: ")
                if Nom_prod.lower() == 'salir':
                    break
                if Tridentisimo.verifica_nombre(Nom_prod):
                    print("El nombre del producto ya existe. Por favor, ingrese un nombre diferente.")
                    continue
                Descripcion = input("Ingrese la descripción del producto: ")
                while True:
                    Precio = float(input("Ingrese el precio del producto: "))
                    if Precio > 0:
                        break
                    print("Por favor, ingrese un precio positivo.")
                while True:
                    Cant_stock = int(input("Ingrese la cantidad en stock del producto: "))
                    if Cant_stock > 0:
                        break
                    print("Por favor, ingrese una cantidad en stock positiva.")
                Categoria = input("Ingrese la categoría del producto: 'Bidones' o 'Envases': ")
                Tridentisimo.Ingresa_produc(Nom_prod, Descripcion, Precio, Cant_stock, Categoria)
                
        elif opcion == '2':
            while True:
                ID_prod = input("Ingrese el ID del producto a actualizar o 'salir' para regresar al menú: ")
                if ID_prod.lower() == 'salir':
                    break
                if not Tridentisimo.verifica_id(int(ID_prod)):
                    print("El ID del producto no existe. Por favor, ingrese un ID válido.")
                    continue
                Nom_prod = input("Ingrese el nuevo nombre del producto: ")
                Descripcion = input("Ingrese la nueva descripción del producto: ")
                Precio = float(input("Ingrese el nuevo precio del producto: "))
                Cant_stock = int(input("Ingrese la nueva cantidad en stock del producto: "))
                Categoria = input("Ingrese la nueva categoría del producto: 'Bidones' o 'Envases': ")
                Tridentisimo.Actualiza_produc(ID_prod, Nom_prod, Descripcion, Precio, Cant_stock, Categoria)
        elif opcion == '3':
            while True:
                ID_prod = input("Ingrese el ID del producto a eliminar o 'salir' para regresar al menú: ")
                if ID_prod.lower() == 'salir':
                    break
                Tridentisimo.Elimina_produc(ID_prod)
        elif opcion == '4':
            Tridentisimo.Muestra_productos()
        elif opcion == '5':
            while True:
                ID_prod = input("Ingrese el ID del producto a mostrar o 'salir' para regresar al menú: ")
                if ID_prod.lower() == 'salir':
                    break
                if not Tridentisimo.verifica_id(int(ID_prod)):
                    print("El ID del producto no existe. Por favor, ingrese un ID válido.")
                    continue
                Tridentisimo.Muestra_producto_por_id(int(ID_prod))
        elif opcion == '6':
            return 
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

menu()