# REST_API

En el fichero app.py se presenta el código fuente para el proyecto en cuestión. Por el enunciado del problema, no estaba seguro en si pedíais un endpoint para requerir la información de nombre y código postal mediante un comando GET a una fuente externa como una base de datos o, por el contrario, tenía que recibir la información para registrar un nuevo usuario en una base datos. Finalmente me he decantado por la segunda opción: se trata de un endpoint de tipo POST que recibirá peticiones de ingreso de supuestos nuevos usuarios mediante su nombre y su código postal. 

Utilizando el código postal recibido, se realiza una petición GET a la API de geonames para obtener la ciudad correspondiente a dicho código postal. Normalmente, la API de geonames nos devolverá un listado con varias ciudades del mundo que pueden corresponderse al código postal. Para el problema en cuestión he decidido quedarme con la primera de todas.

Para simular la entrada de nuevos usuarios, así como para comprobar el correcto funcionamiento de las comunicaciones, se ha utilizado el software Insomnia, que nos permite enviar los comandos GET y POST en formato JSON. Posteriormente, almacenamos dicha información en una base de datos. 

Para la base de datos hemos utilizado el software XAMPP, que es un paquete de software libre, que consiste principalmente en el sistema de gestión de bases de datos MySQL e incluye el módulo phpMyAdmin. La base de datos estará formada por 2 tablas:
•	Users_master: almacena el nombre del usuario
•	Users_details: almacena el código postal y la ciudad

Finalmente, el servidor responde en formato JSON para indicar si el usuario se ha podido añadir satisfactoriamente o si, por el contrario, no ha encontrado el código postal introducido.
