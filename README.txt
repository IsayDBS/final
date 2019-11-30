Proyecto de Terminal de Autobuses
Este proyecto esta hecho para imitar una base de datos de autobuses, en la cual hay un Administrador y un vendedor.
El Administrador puede agregar y quitar rutas, igual con las paradas, exceptuado casos en que haya boletos en las rutas
o boletos que sean entrada o salida de los boletos.
El programa no diferencea entre mayusculas y minusculas, por lo tanto, cuando metes rutas o nombre de paradas, es lo kismo meterlo con mayusculas que minisculas.
Cuando el administrador borra una ruta, esta borrara todas las terminales, exceptuando cuando son compartidas, en ese caso
solo borra la terminal que le correspondia a esa estacion, manteniendo intacta la estacion de la otra ruta.
No se permite nombre de rutas repetidos
Si en una ruta hay una sola parada y se borra la parada, la ruta se borra igual, es lo mismo que decir que no existen rutas "vacias"
Si se quiere hacer una interseccion, solo basta con agregar el nombre de la misma parada a la ruta.
El vendedor puede vender boletos en cualquier ruta.
El vendedor cancela los boletos con el identificador de los boletos
Este proyecto fue pensado para que el administrador tenga en mente que las rutas son en una direccion y sin repertir estaciones, es decir, si se crea una parada
o cuando se crea una ruta, no puede haber dos terminales con el mismo nombre. (Como las rutas del transporte publico)
La forma de correr el programa es el siguiente
Hacer un .env con la informacion de tu mysql, correr el archivo final.sql
El programa recibe un valor desde afuera, sea 1 para el administrador o
2 para el vendedor, y dentro de cada uno el programa corre el menu correspondiente.
Ejemplo:
Para administrador
python Main.py 1
Para vendedor
python Main.py 2
Cualquier otra cosa, no genera nada
El programa funciona con python 3
Patron de disenios
En los patrones de disenios que yo utilice para este proyecto se encuentra
Facade
Lo utilice para que fuera mas sencillo leer el codigo, ya que administrador y vendedor tienen metodos demasiado complejos
y queria que fuera mas sencillo para que yo como programador no batallara tanto el problema
MVC
Este fue el que desde el principio supe que iba a utilizar, ya que necesitaba que la informacion
fuera leida por el usuario, interpretado, y habria un manejo de base de datos
Memento
Este patron no lo termine utilizando en mi proyecto, al principio se me ocurrio que cada vez que
se creara una ruta, se guardaran todos los boletos en la tabla con un columna de verdadero si
ya se habia vendido o falso si no se habia vendido, cada que cancelaras un boleto, utilizaria
el memento para volver al estado anterior del boleto, es decir, sin informacion, pero
me di dando cuenta en la elaboracion del proyecto que no era tan necesario, ademas de hacer
el codigo mas dificil
