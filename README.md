changelog      
Actualizacion de Reestructuracion de PIA 1.1:                                     
-Se cambiaron nombre de archivos y funciones, con la eliminacion de la funcion "Menu" para integrarla dentro del main                 
-ahora el archivo Opciones ahora se llama menu, ahi se pondra todas las funciones del menu               


Actualizacion de Personajes de PIA 1.2:  
-se agregaron modulos funPersonajes.py y funNavesPeliculas.py   
-se agrego la funcion instaladores unica y exclusivamente para agregar librerias locales   
-se agrego la funcion obtener_informacion_por_id en el modulo de sub-menu para ingregar el ID de los personajes y asegurar que se meta una ID valida 	   
-se agregaron 4 funciones al modulo funPersonajes.py:    
---obtener_informacion_personaje: funciona para obtener el personaje a partir de la ID y regresa los datos obtenidos de la api en una variable llamada datosPersonaje    
---mostrar_caracteristicas_fisicas: funciona solo para mostrar las caracteristicas fisicas apartir de la variable datosPersonaje    
---mostrar_datos_generales: funciona solo para mostrar los datos que no necestariamente son fisicos, la variable que usa tambien es datosPersonaje   
---obtener_nombres: es una funcion que se utiliza para obtener unicamente los nombres de cualquier cosa que necesite un link concreto como las naves, recibe las URL's para dar los nombres     
-se agregaron 2 funciones al modulo funPersonajes.py:     
---obtener_informacion_naves: funciona para obtener el personaje a partir de la ID y regresa los datos obtenidos de la api en una variable llamada datosNaves      
---obtener_informacion_peliculas: funciona para obtener el personaje a partir de la ID y regresa los datos obtenidos de la api en una variable llamada pelis
