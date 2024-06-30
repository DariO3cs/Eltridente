
from Eltridente import conecta_Tridente
def test_integration():
    Tridentisimo = conecta_Tridente()

    Tridentisimo.Ingresa_produc('Producto Test', 'Descripción Test', 100.0, 10, 'Categoría Test')
    print("Producto creado correctamente.")

    Tridentisimo.Muestra_productos()
    print("Productos leídos correctamente.")

    Tridentisimo.Actualiza_produc(1, 'Producto Test Actualizado', 'Descripción Test Actualizada', 200.0, 20, 'Categoría Test Actualizada')
    print("Producto actualizado correctamente.")

    Tridentisimo.Elimina_produc(1)
    print("Producto eliminado correctamente.")
    
test_integration()
