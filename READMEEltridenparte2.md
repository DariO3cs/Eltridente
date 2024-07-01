Nombre base de datos: ELTRIDENTE.DBF
Nombre base de archivo Pyton (consola): Eltridente_parte2.py
Prueba de funcionalidad: Funcionalidadparte2.py 
Prueba de Integracion: Integracionparte2.py
Prueba de Unitarias: Teste_Eltridenteparte2.py
Prueba de Validaciones: Validacionesparte2.py

Manual de uso consola en Pyton

Al ingresar nuestra consola, le indicara primero un indicar si es 'Administrador' o 'Vendedor'

Si es Administrador otorgrara las siguientes opciones

_________________Opciones a escoger________________

1. Ingresar usuario
2. Actualizar usuario
3. Eliminar usuario
4. Listar usuarios
5. Ingresar producto
6. Actualizar producto
7. Eliminar producto
8. Listar productos
9. Regresar al menú principal
Descripcion de opciones

1. Ingresar usuario        : Debe ingresar un usuario, en esta opcion debera llenar los siguientes campos:
Nombre usuario             : Tiene un maximo de caracteres 255 
Roli                       : Debe ingresar si es Administrador o Vendedor

2. Actualuzar usuario      : Puede actualizar un producto desde su ID, en esta opcion le pedira:
Numero de ID_usuario       : Debe ingresar un ID existente
Nuevo nombre usuario       : Debe ingresar un nuevo nombre de usuario
Nueva descripcion          : Debe ingresar un nuevo rol

3. Eliminar usuario        : Puede eliminar un usuario desde su ID, en esta opcion le pedira:
Ingrese ID                 : Debe ingresar un ID existente de lo contrario le pedira nuevamente ingresarID

4. Mostrar usuario         : Lista todos o el que escoga por id los productos ingresados, se dara dos opciones

5. Ingresar producto        : Debe ingresar un producto, en esta opcion debera llenar los siguientes campos:
Nombre producto             : No se puede repetir y tiene un maximo de caracteres 255, o bien ingresar 
                              la palabra salir
Descripcion                 : Debe ingresar una descripcion del producto, no debe superar los 1000 caracteres
Precio                      : Debe ser un valor numerico, puede tener hasta dos decimales, debe ser positivo
Cantidad Stock              : Debe ser un valor numerico, debe ser positivo
Categoria                   : Debe ingresar una categoria valida de las cuales se ofrecen

6. Actualuzar Producto      : Puede actualizar un producto desde su ID, en esta opcion le pedira:
Numero de ID                : Debe ingresar un ID existente o bien ingresar la palabra salir,
                              de lo contrario le pedira nuevamente ingresarID
Nuevo nombre producto       : Debe ingresar un nuevo nombre de producto que no se repita
Nueva descripcion           : Debe ingresar una nueva descripcion
Nueva precio                : Debe ingresar un nuevo precio
Nueva cantidad              : Debe ingresar una nueva cantidad
Nueva categoria             : Debe ingresar una nueva categoria

7. Eliminar producto        : Puede eliminar un producto desde su ID, en esta opcion le pedira:
Ingrese ID                  : Debe ingresar un ID existente o bien ingresar la palabra salir,
                              de lo contrario le pedira nuevamente ingresarID

8. Mostrar productos        : Lista todos los productos ingresados o especifico por ID

9. Regresar al menui principal  : Regresa al menu principal

Fin