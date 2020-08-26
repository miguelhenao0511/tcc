Teoría de la computación y compilación

Integrantes
* Juan Pablo Rivera Sierra
* Daniel Andrés Toro Aguirre
* Miguel Ángel Henao Higuita
* Felipe Villarreal Piedrahita
*  ̶L̶u̶i̶s̶ ̶F̶e̶l̶i̶p̶e̶ ̶M̶a̶r̶í̶n̶ ̶B̶u̶i̶t̶r̶a̶g̶o̶
* Sebastián López Mazo
* Santiago Cano

Herramienta de diagramas
*  ̶D̶r̶a̶w̶.̶i̶o̶  BPMN.IO

Tipo de archivo de entrada:
* XML

Lenguaje objetivo
* Python

Framework
* Django

Producto terminado
* Aplicativo web

Reglas 
* El evento inicio creará el proyecto en django (django-admin startproject nombredelsitio) y dependiendo del nombre del evento inicio será el nombre del proyecto y otra palabra clave que puede disparar una acción que crea una base de datos; base de datos con datos ficticios o no crear una base de datos.
* Las piscinas definen usuarios (clases que crearán instancias si las hay en la base de datos) del sistema donde cada uno debe tener un nombre de usuario y contraseña, a no ser que sea invitado.
* Se define un banco de palabras para filtrar las tareas y así definir las funcionalidades del sistema y las opciones de menú de dicho usuario, por ejemplo: la tarea “registro” se verá reflejada como un menú superior con un pequeño formulario para creación del usuario, las tareas como “Crear artículo” o simplemente las que empiecen por “Crear” serán submenús de x usuario que crean formularios con un título, imagen y descripción que lleven esa creación a la base de datos.
* El evento final de cualquier proceso lleva al usuario al inicio del sistema.
* Cada gateway debe estar nombrado con palabras claves que van a estar almacenadas en un banco de palabras para realizar filtros y llevar un control.
