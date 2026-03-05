rol: Experto en django consulta: Haz una documentación para una persona principiante con una explicación en forma de comentario al inicio y tras la explicación emplea un ejemplo sencillo para que quede más claro los siguientes conceptos:

- Explicación introductoria al uso de formularios
- Explicación y uso de formularios con una petición de tipo get que nos pasa información al request, con dicha información usamos una query en view usando models
  para obtener la información de la BD y mostrarla por medio del template(Aqui no usaremos clases sino que empleamos directamente request, es para ver como funciona por dentro, indica por que se trata de una mala práctica).
- Explicación del uso de if y for para manejar la información que pasamos en el context al template.
- Explicación y uso de clases que heredan de form para peticiones get, en la vista instanciamos la clase y le pasamos el request get, despues obtenemos el valor de campo con instancia.data['key'] lo cual pasamos a las queries y pasamos la instancia y el resultado de las queries a context,
  establece las ventajas de este método con respecto al anterior.
- Explicación del metodo as_p a la instancia del formulario.
- Explicación y uso de csrf token para peticiones tipo POST.
- Explicación y uso de clases que heredan de form para peticiones POST, en la vista instanciamos la clase y le pasamos el request.get, después lo validamos con isValid() a partir de una serie de funciones que le pasamos en el propio modelo y si pasa limpiamos los datos con cleanedData y creamos un context que contendrá la instancia del formulario y un booleano que no servirá para indicar que el envio del formulario ha tenido exito

  Especificaciones:-La documentación debe contener la explicación detallada de todo lo necesario para el uso de los conceptos a nivel profesional-Los ejemplos deben estar explicados con comentarios sobre lo que hacen en cada paso -El formato de entrega será markdown. Verificación:Revisa el contenido de la consulta para obtener el resultado deseado, recuerda que lo más importante es que los ejemplos estén bien explicados , tomate el tiempo necesario para obtener el mejor resultado.

genera el markdown de la documentación para descargar pero no te dejes nada de lo que has desarrollado en el primer prompt.

genera un serie de ejercicios para practicar todos estos conceptos, estos ejercicios deben diferir de los que has puesto de ejemplo y aumentar progresivamente de dificultad hasta el punto de alcanzar un uso profesional y fluido. Genera el número de ejercicios que consideres necesario para alcanzar un buen nivel de dominio

Documenta el contenido del video realizando un explicación a detalle cada uno de los ejemplos en forma de comentario tipo py y
luego poniendo el ejemplo en formato ejecutable. Las explicaciones deben ir dirigidas a un público principiante y todo debe ir
en formato py
