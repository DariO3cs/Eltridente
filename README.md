Nombre base de datos: ELTRIDENTE.DBF
Nombre base de archivo Python (consola): Eltridente.py
Prueba de funcionalidad: Funcionalidad.py 
Prueba de Integracion: Integracion.py
Prueba de Unitarias: Teste_Eltridente.py
Prueba de Validaciones: Validaciones.py

Manual de uso consola en Pyton

Al ingresar nuestra consola, le indicara primero un menú con 6 opciones, de las cuales
debera escoger una.
_________________Opciones a escoger________________

1. Ingresar producto
2. Actualizar producto
3. Eliminar producto
4. Mostrar productos
5. Mostrar producto por ID
6. Salir

Descripcion de opciones

1. Ingresar producto        : Debe ingresar un producto, en esta opcion debera llenar los siguientes campos:
Nombre producto             : No se puede repetir y tiene un maximo de caracteres 255, o bien ingresar 
                              la palabra salir
Descripcion                 : Debe ingresar una descripcion del producto, no debe superar los 1000 caracteres
Precio                      : Debe ser un valor numerico, puede tener hasta dos decimales, debe ser positivo
Cantidad Stock              : Debe ser un valor numerico, debe ser positivo
Categoria                   : Debe ingresar una categoria valida de las cuales se ofrecen

2. Actualuzar Producto      : Puede actualizar un producto desde su ID, en esta opcion le pedira:
Numero de ID                : Debe ingresar un ID existente o bien ingresar la palabra salir,
                              de lo contrario le pedira nuevamente ingresarID
Nuevo nombre producto       : Debe ingresar un nuevo nombre de producto que no se repita
Nueva descripcion           : Debe ingresar una nueva descripcion
Nueva precio                : Debe ingresar un nuevo precio
Nueva cantidad              : Debe ingresar una nueva cantidad
Nueva categoria             : Debe ingresar una nueva categoria

3. Eliminar producto        : Puede eliminar un producto desde su ID, en esta opcion le pedira:
Ingrese ID                  : Debe ingresar un ID existente o bien ingresar la palabra salir,
                              de lo contrario le pedira nuevamente ingresarID

4. Mostrar productos        : Lista todos los productos ingresados

5. Mostrar producto por ID  : Mostrara un producto segun el ID que ingresemos, en esta opcion le pedira:
Ingrese ID                  : Debe ingresar un ID existente o bien ingresar la palabra salir,
                              de lo contrario le pedira nuevamente ingresarID

6. Salir                    : Con esta opción se cerrara el programa

Fin
