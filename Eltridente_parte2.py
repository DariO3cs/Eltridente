import cx_Oracle;
import getpass
class conecta_Tridente ():
    def __init__(self):
        user = 'Tridente'
        password = '6217'
        self.ConexionElTridente=cx_Oracle.connect(
            user = 'Tridente',
            password= password,
            dsn = "localhost/xe"
        );
        
        self.cursi = self.ConexionElTridente.cursor();
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
        print(".    .    .      .     .    CONEXION ESTABLECIDA A LA BD   .    .     .    . ");
        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::");
        
        self.rol = input("Ingrese su rol (Administrador/Vendedor): ")
        
        if self.rol == 'Administrador':
            self.administrador()
        elif self.rol == 'Vendedor':
            self.vendedor()
        else:
            print("Rol no reconocido. Por favor, ingrese 'Administrador' o 'Vendedor'.")
            
    def ingresar_usuario(self):
        Nom_usu = input("Ingrese nombre de usuario: ")
        Rol = input("Ingrese rol de usuario: ")
        self.cursi.execute(f"INSERT INTO Usuario (Nom_usu, Rol) VALUES ('{Nom_usu}', '{Rol}')")
        self.ConexionElTridente.commit()
        
    def actualizar_usuario(self):
        while True:
            ID_Usu = input("Ingrese ID de usuario a actualizar: ")
            self.cursi.execute(f"SELECT * FROM Usuario WHERE ID_Usu = {ID_Usu}")
            usuario = self.cursi.fetchone()
            if usuario is not None:
                break
            else:
                print("ID de usuario no encontrado. Por favor, intente de nuevo.")
        Nom_usu = input("Ingrese nuevo nombre de usuario: ")
        Rol = input("Ingrese nuevo rol de usuario: ")
        self.cursi.execute(f"UPDATE Usuario SET Nom_usu = '{Nom_usu}', Rol = '{Rol}' WHERE ID_Usu = {ID_Usu}")
        self.ConexionElTridente.commit()
        print("Usuario actualizado con éxito.")    
    
    def eliminar_usuario(self):
        while True:
            ID_Usu = input("Ingrese ID de usuario a eliminar: ")
            self.cursi.execute(f"SELECT * FROM Usuario WHERE ID_Usu = {ID_Usu}")
            usuario = self.cursi.fetchone()
            if usuario is not None:
                break
            else:
                print("ID de usuario no encontrado. Por favor, intente de nuevo.")
        self.cursi.execute(f"DELETE FROM Usuario WHERE ID_Usu = {ID_Usu}")
        self.ConexionElTridente.commit()
        print("Usuario eliminado con éxito.")
        
    def listar_usuarios(self):
        opcion = input("¿Deseas listar todos los usuarios o un usuario específico? (todos/específico): ")
        if opcion.lower() == 'todos':
            self.cursi.execute("SELECT * FROM Usuario")
            usuarios = self.cursi.fetchall()
            if usuarios:
                for usuario in usuarios:
                    print(usuario)
            else:
                print("No hay usuarios en la base de datos.")
        elif opcion.lower() == 'específico':
            while True:
                ID_Usu = input("Ingrese el ID del usuario: ")
                self.cursi.execute(f"SELECT * FROM Usuario WHERE ID_Usu = {ID_Usu}")
                usuario = self.cursi.fetchone()
                if usuario is not None:
                    print(usuario)
                    break
                else:
                    print("ID de usuario no encontrado. Por favor, intente de nuevo.")
        else:
            print("Opción no reconocida. Por favor, intenta de nuevo.")
            
    def ingresar_producto(self):
        while True:
            Nom_prod = input("Ingrese nombre del producto: ")
            self.cursi.execute(f"SELECT * FROM Producto WHERE Nom_prod = '{Nom_prod}'")
            producto = self.cursi.fetchone()
            if producto is None:
                break
            else:
                print("Nombre de producto ya en uso. Por favor, intente de nuevo.")
        Descripcion = input("Ingrese descripción del producto: ")
        Precio = input("Ingrese precio del producto: ")
        Cant_stock = input("Ingrese cantidad en stock del producto: ")
        Categoria = input("Ingrese categoría del producto: ")
        self.cursi.execute(f"INSERT INTO Producto (Nom_prod, Descripcion, Precio, Cant_stock, Categoria) VALUES ('{Nom_prod}', '{Descripcion}', {Precio}, {Cant_stock}, '{Categoria}')")
        self.ConexionElTridente.commit()
        print("Producto ingresado con éxito.")

    def actualizar_producto(self):
        while True:
            ID_prod = input("Ingrese ID del producto a actualizar: ")
            self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_prod}")
            producto = self.cursi.fetchone()
            if producto is not None:
                break
            else:
                print("ID de producto no encontrado. Por favor, intente de nuevo.")
        while True:
            Nom_prod = input("Ingrese nuevo nombre del producto: ")
            self.cursi.execute(f"SELECT * FROM Producto WHERE Nom_prod = '{Nom_prod}' AND ID_prod != {ID_prod}")
            producto = self.cursi.fetchone()
            if producto is None:
                break
            else:
                print("Nombre de producto ya en uso. Por favor, intente de nuevo.")
        Descripcion = input("Ingrese nueva descripción del producto: ")
        Precio = input("Ingrese nuevo precio del producto: ")
        Cant_stock = input("Ingrese nueva cantidad en stock del producto: ")
        Categoria = input("Ingrese nueva categoría del producto: ")
        self.cursi.execute(f"UPDATE Producto SET Nom_prod = '{Nom_prod}', Descripcion = '{Descripcion}', Precio = {Precio}, Cant_stock = {Cant_stock}, Categoria = '{Categoria}' WHERE ID_prod = {ID_prod}")
        self.ConexionElTridente.commit()
        print("Producto actualizado con éxito.")
    
    def eliminar_producto(self):
        while True:
            ID_prod = input("Ingrese ID del producto a eliminar: ")
            self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_prod}")
            producto = self.cursi.fetchone()
            if producto is not None:
                break
            else:
                print("ID de producto no encontrado. Por favor, intente de nuevo.")
        self.cursi.execute(f"DELETE FROM Producto WHERE ID_prod = {ID_prod}")
        self.ConexionElTridente.commit()
        print("Producto eliminado con éxito.")

    def listar_productos(self):
        opcion = input("¿Deseas listar todos los productos o un producto específico? (todos/específico): ")
        if opcion.lower() == 'todos':
            self.cursi.execute("SELECT * FROM Producto")
            productos = self.cursi.fetchall()
            if productos:
                for producto in productos:
                    print(producto)
            else:
                print("No hay productos en la base de datos.")
        elif opcion.lower() == 'específico':
            while True:
                ID_prod = input("Ingrese el ID del producto: ")
                self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_prod}")
                producto = self.cursi.fetchone()
                if producto is not None:
                    print(producto)
                    break
                else:
                    print("ID de producto no encontrado. Por favor, intente de nuevo.")
    def ingresar_venta(self):
        while True:
            ID_Prod = input("Ingrese ID del producto vendido: ")
            self.cursi.execute(f"SELECT * FROM Producto WHERE ID_prod = {ID_Prod}")
            producto = self.cursi.fetchone()
            if producto is not None:
                break
            else:
                print("ID de producto no encontrado. Por favor, intente de nuevo.")
        Cantidad = input("Ingrese cantidad vendida: ")
        Fecha = input("Ingrese fecha de la venta (formato YYYY-MM-DD): ")
        ID_Vend = input("Ingrese su ID de vendedor: ")
        self.cursi.execute(f"INSERT INTO Venta (ID_Prod, Cantidad, Fecha, ID_Vend) VALUES ({ID_Prod}, {Cantidad}, TO_DATE('{Fecha}', 'YYYY-MM-DD'), {ID_Vend})")
        self.ConexionElTridente.commit()
        print("Venta ingresada con éxito.")

    def listar_ventas(self):
        opcion = input("¿Deseas listar todas las ventas o una venta específica? (todas/específica): ")
        if opcion.lower() == 'todas':
            self.cursi.execute("SELECT * FROM Venta")
            ventas = self.cursi.fetchall()
            if ventas:
                for venta in ventas:
                    print(venta)
            else:
                print("No hay ventas en la base de datos.")
        elif opcion.lower() == 'específica':
            while True:
                ID_Venta = input("Ingrese el ID de la venta: ")
                self.cursi.execute(f"SELECT * FROM Venta WHERE ID_Venta = {ID_Venta}")
                venta = self.cursi.fetchone()
                if venta is not None:
                    print(venta)
                    break
                else:
                    print("ID de venta no encontrado. Por favor, intente de nuevo.")
    def menu_principal(self):
        while True:
            print("Bienvenido a El Tridente. ¿Qué rol tienes?")
            print("1. Administrador")
            print("2. Vendedor")
            print("3. Salir")
            opcion = input("Por favor, selecciona una opción: ")
            if opcion == '1':
                self.administrador()
            elif opcion == '2':
                self.vendedor()
            elif opcion == '3':
                print("¡Hasta luego!")
                break
            else:
                print("Opción no reconocida. Por favor, intenta de nuevo.")

    def administrador(self):
        while True:
            print("Bienvenido, Administrador. ¿Qué te gustaría hacer?")
            print("1. Ingresar usuario")
            print("2. Actualizar usuario")
            print("3. Eliminar usuario")
            print("4. Listar usuarios")
            print("5. Ingresar producto")
            print("6. Actualizar producto")
            print("7. Eliminar producto")
            print("8. Listar productos")
            print("9. Regresar al menú principal")
            opcion = input("Por favor, selecciona una opción: ")
            if opcion == '1':
                self.ingresar_usuario()
            elif opcion == '2':
                self.actualizar_usuario()
            elif opcion == '3':
                self.eliminar_usuario()
            elif opcion == '4':
                self.listar_usuarios()
            elif opcion == '5':
                self.ingresar_producto()
            elif opcion == '6':
                self.actualizar_producto()
            elif opcion == '7':
                self.eliminar_producto()
            elif opcion == '8':
                self.listar_productos()
            elif opcion == '9':
                break
            else:
                print("Opción no reconocida. Por favor, intenta de nuevo.")

    def vendedor(self):
        while True:
            print("Bienvenido, Vendedor. ¿Qué te gustaría hacer?")
            print("1. Ingresar venta")
            print("2. Listar ventas")
            print("3. Regresar al menú principal")
            opcion = input("Por favor, selecciona una opción: ")
            if opcion == '1':
                self.ingresar_venta()
            elif opcion == '2':
                self.listar_ventas()
            elif opcion == '3':
                break
            else:
                print("Opción no reconocida. Por favor, intenta de nuevo.")

app = conecta_Tridente()
app.menu_principal()