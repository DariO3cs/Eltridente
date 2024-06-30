from Eltridente import conecta_Tridente

def test_ingresa_produc():
    Tridentisimo = conecta_Tridente()
    
    Tridentisimo.Ingresa_produc('Producto Test', 'Descripción Test', 100.0, 10, 'Categoría Test')
    
    if Tridentisimo.verifica_nombre('Producto Test'):
        print("La prueba de ingreso de producto pasó correctamente.")
    else:
        print("La prueba de ingreso de producto falló.")

def test_actualiza_produc():
    Tridentisimo = conecta_Tridente()
    Tridentisimo.Actualiza_produc(1, 'Producto Test Actualizado', 'Descripción Test Actualizada', 200.0, 20, 'Categoría Test Actualizada')

    producto_actualizado = Tridentisimo.consulta_producto(1)  # Asume que consulta_producto es una función que devuelve los detalles de un producto dado su ID
    if (producto_actualizado['Nom_prod'] == 'Producto Test Actualizado' and
        producto_actualizado['Descripcion'] == 'Descripción Test Actualizada' and
        producto_actualizado['Precio'] == 200.0 and
        producto_actualizado['Cant_stock'] == 20 and
        producto_actualizado['Categoria'] == 'Categoría Test Actualizada'):
        print("La prueba de actualización de producto pasó correctamente.")
    else:
        print("La prueba de actualización de producto falló.")

def run_tests():
    test_ingresa_produc()
    test_actualiza_produc()
run_tests()