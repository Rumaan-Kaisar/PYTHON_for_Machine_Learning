
################# 14.4: FULL
# copy: Analyze: analyze this text, get the topics, 
#       output in english: describe the topics on your own knowledge withot losing context, use clarification and fix any misconception (mention them)
#        
################# (17-May-25 for 18-May-25)

# Courses: PrTla PY for DS & ML >    14.4, 14.5



The most common question I get from students is: Hey, does this value of RMSE good?
And as always, context is everything.

---------  4.26

Let's imagine you were doing some kind of ML model and got a squared error.





--------------------------------
00:02:18,020 --> 00:02:20,190
eso para todas tus predicciones.
--------------------------------


Ahora el problema con el error absoluto medio es que no castigará los errores grandes.

Así que aquí tenemos lo que se conoce como ans viene cuarteto y podemos ver aquí que tenemos una amplia variedad

de diferentes dispersiones de puntos de datos aquí.

Sin embargo, la línea de mejor ajuste para todos estos es en realidad la misma.

Por eso queremos asegurarnos de que estamos al tanto de situaciones como esta.

Por ejemplo, echemos un vistazo a esta situación específica.

Tenemos un punto que es un valor atípico enorme, por lo que queremos que nuestras métricas de aire realmente los tengan en cuenta.

Entonces, lo que podemos hacer es usar un error cuadrático medio.

Y esta es la media de los errores al cuadrado.

Entonces, lo que estamos haciendo aquí es tomar la diferencia entre el valor verdadero menos nuestro valor predicho y vamos a

ajustarlo al cuadrado.

Y como puede imaginar cuando realmente tomamos ese cuadrado, los errores más grandes se notan más que con el error absoluto

medio, lo que hace que el error al cuadrado sea más popular porque realmente va a

castigar a su modelo por esas situaciones atípicas a las que no corresponde.

Y ya no necesitamos tomar el valor absoluto porque cualquier cosa al cuadrado termina siendo positiva.

Sin embargo, hay otro problema con el que nos encontramos con un error al cuadrado que cuadra la etiqueta

real menos su predicción.

En realidad también cuadra las unidades mismas.

Entonces, por ejemplo, si está prediciendo el precio de una casa, nuestra métrica de error con error absoluto

medio sería en dólares pero con error medio al cuadrado.

Terminamos obteniendo una métrica de error en unidades de dólares al cuadrado que es difícil de interpretar, por lo que la forma

en que solucionamos esto es con la raíz del error cuadrático medio esencialmente al final, simplemente tomas

la raíz cuadrada de tu error cuadrático medio.

Así que este es el más popular porque castiga esos valores de error más grandes y

al final del día tiene las mismas métricas o las mismas unidades que y ahora.

La pregunta más común que recibo de los estudiantes es: hey, este valor de raíz significa error

al cuadrado que obtuve bien.

Y como siempre, el contexto lo es todo.

Imaginemos que estaba realizando algún tipo de modelo de maquinaria y obtuvo un error cuadrático

medio de diez dólares y me pregunta: ¿Es este un error cuadrático suficientemente bueno?

Bueno, realmente depende del contexto de la situación.

Significa que un cuarto de diez dólares sería fantástico si predices el precio de una casa, ya que diez

dólares son muy pequeños en comparación con el precio promedio de una casa.

Pero si se suponía que su modelo de aprendizaje automático predeciría el precio de una barra de chocolate en función de sus características

y su ruta significa que el trimestre era de diez dólares.

En realidad, eso es realmente malo, por lo que debemos hacer es que debe comparar su métrica de error para la tarea

de regresión con el valor promedio de la etiqueta.

Ese es el valor medio en su conjunto de datos para tratar de obtener una intuición de su rendimiento general.

Y como siempre, el conocimiento de dominio también juega un papel realmente importante aquí.

Entonces, el aprendizaje automático nuevamente no se hace en el vacío, generalmente se hace con un proceso colaborativo.

Entonces, si está prediciendo los precios de una casa y desea tener una idea de si su error de

rutina fue bueno o no, probablemente sea una buena idea comenzar a hablar con alguien con experiencia como

agente de bienes raíces.

Bien, ahora entendemos las diferentes métricas que puede usar para evaluar el rendimiento de una tarea

de regresión.

Gracias y nos vemos en la próxima conferencia.














