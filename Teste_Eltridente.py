import unittest
from Eltridente import conecta_Tridente  

class TestConectaTridente(unittest.TestCase):
    def setUp(self):
        self.conexion = conecta_Tridente()

    def test_ing_prod(self):
        self.conexion.Ingresa_produc('Agua envase 2L', 'Agua embotellada en envases de 2L no retornables', 1500, 20, 'Envases')
        self.conexion.cursi.execute("select * from Producto where Nom_prod = 'Agua envase 2L'")
        producto = self.conexion.cursi.fetchone()
        self.assertIsNotNone(producto, "roducto ingresado")

    def test_act_produc(self):
        self.conexion.Actualiza_produc(1, 'Agua envase 2.5L', 'Agua embotellada en envases de 2.5L no retornables', 1700, 20, 'Envases 2.0')
        self.conexion.cursi.execute("select * from Producto where ID_prod = 1")
        producto = self.conexion.cursi.fetchone()
        self.assertEqual(producto[1], 'Producto actualizado')

    def test_elimina_prod(self):
        self.conexion.Elimina_produc(1)
        self.conexion.cursi.execute("select * from Producto where ID_prod = 1")
        producto = self.conexion.cursi.fetchone()
        self.assertIsNone(producto, "eliminado")

if __name__ == "__main__":
    unittest.main()