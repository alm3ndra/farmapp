 
 FARMAPP
=========

+ Este es el README de la nueva aplicación FARMAPP.

 INTRODUCCION
==============

+ Es una aplicación WEB desarrollada específicamente para realizar consultas en el registro de ventas de un laboratorio en particular. 

+ Desarrollada integramente en el lenguaje de programación PYTHON, en su versión 3.*


 MODULOS Y REPOSITORIOS DE 3ros.:
==================================

+ Se utilizaron los siguientes módulos y repositorios, los cuales pueden ser tomados de ejemplo de uso:

++ CSV
++ Flask
++ Bootstrap (flask_bootsrap)
++ Flask_Moment
++ Flask_Script

 FLUJO
=======

+ El programa inicia haciendo un test de disponibilidad de los recursos tales como CSV, y retorna en consola mensajes satisfactorios o de error.

+ Al ser ejecutada en un servidor local, luego de abrir el Navegador e indicar el puerto correspondiente en la barra de navegación (127.0.0.1:5000/) la aplicación nos da la bienvenida en un archivo con extensión .html, donde se invita al usuario a ingresar para poder acceder a las opciones de consulta que brinda.

 ESTRUCTURA DE DATOS
=====================

+ Consta de varios módulos. 

+ El loop principal (o archivo principal) denominado main.py, desde donde se definen las rutas de cada página del sitio de la aplicación, se dirige al usuario hacia la interacción con cada opción disponible y se vincula a cada proceso con un documento HTML. 

+ Los formularios se heredan de FLaskForm(), el cual se uiliza como framework a lo largo de toda la aplicación para agilizar la construcción del Front-End y se guardan en el archivo forms.py.

+ El archivo listados_module consta de funciones que se encargan de resolver la parte lógica para la formulación de consultas a la base de datos ubicada en el fichero farmacia.csv

+ El fichero class_csv.py crea una clase que prepara los datos que se mostrarán en pantalla luego de la consulta, capturando en vectores los campos de la base de datos csv.

+ El fichero validate.py realiza las validaciones que se pidieron para el trabajo práctico, cada vez que se lo importa.

+ La carpeta templates contiene la estructura de la interfaz web, en archivos con extensión .html, por los cuales se navegará para realizar las consultas, el log-in y log-out.


 INTERFAZ Y USABILIDAD
=======================

+ El conjunto de los procesos antes mencionados se encargará de mostrar en pantalla el resutado de las consultas, a las cuales el usuario podrá acceder mediante un menú desplegable ubicado en la esquina superior derecha. Podrá visualizar, una vez pasado el log-in, como primera pantalla un listado de las últimas ventas. Podrá también pedir un listado de productos comprados por el cliente seleccionado, un listado de clientes que compraron un producto y también un listado de los clientes que más gastaron en compras. 

+ Luego de navegar el usuario podrá realizar el log-out, deteniéndose automaticamente su sesión. Volverá a la pantalla de bienvenida.

 CREACION DE CLASES
====================

+ Se han diseñado clases propias para cumplir con los propósitos de la aplicación.
+ form.py: Hereda de la clase FlaskForm(), la cual se encarga de agregar al documento HTML correspondiente las etiquetas "<input>" necesarias por cada nuevo campo que sea creado desde las clases Flogin(), Fproductos() y Fclientes().
+ class_csv.py: Prepara y organiza los datos de los rchivos CSV (base de datos). 
+ validate.py cumple la función de validar los datos antes de ser mostrados en pantalla.
