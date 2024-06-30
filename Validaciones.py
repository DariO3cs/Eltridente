from Eltridente import conecta_Tridente

def test_validaciones():
    Tridentisimo = conecta_Tridente()

    Tridentisimo.Ingresa_produc('Producto Test', 'Descripción Test', 100.0, 10, 'Categoría Test')
    try:
        Tridentisimo.Ingresa_produc('Producto Test', 'Descripción Test', 100.0, 10, 'Categoría Test')
    except Exception as e:
        print("La validación del nombre del producto al ingresar un producto pasó correctamente.")

    try:
        Tridentisimo.Ingresa_produc('Producto Test 2', 'Descripción Test', -100.0, -10, 'Categoría Test')
    except Exception as e:
        print("La validación del precio y la cantidad en stock al ingresar un producto pasó correctamente.")

    Tridentisimo.Actualiza_produc(1, 'Producto Test', 'Descripción Test Actualizada', 200.0, 20, 'Categoría Test Actualizada')
    try:
        Tridentisimo.Actualiza_produc(2, 'Producto Test', 'Descripción Test Actualizada', 200.0, 20, 'Categoría Test Actualizada')
    except Exception as e:
        print("La validación del nombre del producto al actualizar un producto pasó correctamente.")

    try:
        Tridentisimo.Actualiza_produc(1, 'Producto Test Actualizado', 'Descripción Test Actualizada', -200.0, -20, 'Categoría Test Actualizada')
    except Exception as e:
        print("La validación del precio y la cantidad en stock al actualizar un producto pasó correctamente.")

    try:
        Tridentisimo.Actualiza_produc(999, 'Producto Test Actualizado', 'Descripción Test Actualizada', 200.0, 20, 'Categoría Test Actualizada')
    except Exception as e:
        print("La validación del ID del producto al actualizar un producto pasó correctamente.")

test_validaciones()