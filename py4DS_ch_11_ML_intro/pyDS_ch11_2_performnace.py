
################# 14.4: FULL
# copy: Analyze: analyze this text, get the topics, 
#       output in english: describe the topics on your own knowledge withot losing context, use clarification and fix any misconception (mention them)
#        
################# (17-May-25 for 18-May-25)

# Courses: PrTla PY for DS & ML >    14.4, 14.5


----------------------    Use google translate:    -----------------------------


----------------  2.18
mean squared error:
Now, the problem with the mean absolute error is that it won't punish large errors.


So what we can do is use a mean squared error.

And this is the mean of the squared errors.

So what we're doing here is taking the difference between the true value minus our predicted value and we're going to square it.

And as you can imagine, when we actually square that error, the larger errors are more noticeable than with mean absolute error, which makes squared error more popular because it's actually going to punish your model for those outliers it doesn't fit.

And we no longer need to take the absolute value because anything squared ends up being positive.



Sure — here’s a simplified, middle-ground version without losing context:

---

**Mean Squared Error (MSE):**

* MAE treats all errors equally, but it doesn’t strongly penalize large mistakes.
* MSE fixes this by **squaring the errors** before averaging them.
* Formula involves:

  * Taking the difference between the actual and predicted value.
  * Squaring that difference.
  * Averaging these squared errors.

**Why square it?**

* Squaring makes big errors count more than small ones.
* No need for absolute values since squaring removes negatives.

**In short:** MSE highlights large errors, making it useful when big mistakes matter.


Sure — here’s the formula for **Mean Squared Error (MSE)**:

$$
\text{MSE} = \frac{1}{m} \sum_{i=1}^{m} (y^{(i)} - \hat{y}^{(i)})^2
$$

**Where:**

* $m$ = total number of examples
* $y^{(i)}$ = true value for the $i^{th}$ example
* $\hat{y}^{(i)}$ = predicted value for the $i^{th}$ example

**Explanation:**
Take the difference between actual and predicted values, square it, then average across all examples.








root mean squared error:
However, there's another problem we run into with a squared error that squares the actual label minus its prediction.

It actually also squares the units themselves.

So, for example, if you're predicting the price of a house, our error metric with mean absolute error would be in dollars, but with mean squared error.

We end up getting an error metric in units of dollars squared, which is hard to interpret, so the way we solve this is with the root mean squared error. Essentially, at the end, you just take the square root of your mean squared error.

So this is the most popular because it does both: punishes those larger error values ​​and

at the end of the day, it has the same metrics or the same units as y now.



Sure — here’s a clean, simplified version without losing context:

---

**Root Mean Squared Error (RMSE):**

* **Problem with MSE:** It squares the errors, which also squares the units (e.g. dollars²), making it hard to interpret.
* **Solution:** Take the square root of the MSE to bring the error back to the original unit (e.g. dollars).
* **Benefit:**

  * Still punishes large errors (since it uses squared errors).
  * Final result is in the same unit as the target value.

**Commonly preferred because it balances both error punishment and interpretability.**


Sure — here’s the equation for **Root Mean Squared Error (RMSE)**:

$$
\text{RMSE} = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2}
$$

**Where:**

* $y_i$ = actual value
* $\hat{y}_i$ = predicted value
* $m$ = total number of data points





The most common question I get from students is: Hey, does this value of RMSE good?
And as always, context is everything.

---------  4.26

Let's imagine you were doing some kind of ML model and got a squared error.





And as always, context is everything.

Let's imagine I was doing some kind of machine modeling and got a root mean squared error of ten dollars, and you're like, "Is this a good enough squared error?"

Well, it really depends on the context of the situation.

It means a ten-dollar quarter would be fantastic if you're predicting the price of a house, since ten dollars is very small compared to the average price of a house.

But if your machine learning model was supposed to predict the price of a chocolate bar based on its characteristics,

and your path means the quarter was ten dollars.

Actually, that's really bad. What we need to do is compare your error metric for the regression task with the average label value.

That's the mean value in your dataset to try to get an intuition about its overall performance.

And as always, domain knowledge also plays a really important role here.

So, machine learning again isn't done in a vacuum; it's usually done with a collaborative process.

So, if you're predicting house prices and want to get a sense of whether your routine error was good or not, it's probably a good idea to start talking to someone with experience as a real estate agent.

Okay, now we understand the different metrics you can use to evaluate the performance of a regression task.

Thanks, and we'll see you at the next conference.


















Bienvenidos de nuevo a todos.

Acabamos de discutir cómo evaluar el rendimiento para los problemas de clasificación.

Ahora comprendamos cómo evaluar el rendimiento para las pruebas de regresión, de modo que podamos tomar un momento para analizar cómo

evaluamos un modelo que está realizando algún tipo de tarea de regresión.

Y, en general, una regresión es la tarea cuando un modelo intenta predecir valores continuos.

A diferencia de las tareas de clasificación en las que estamos tratando de predecir valores categóricos, es posible que haya oído hablar

de algunas métricas de evaluación, como la precisión o el recuerdo o la precisión como acabamos de discutir.

Sin embargo, este tipo de métricas no serán útiles para problemas de regresión.

Realmente no tiene sentido calcular la precisión o la recuperación de una tarea de regresión ya que en

realidad está clasificando cosas.

En cambio, estás prediciendo un valor continuo.

Por lo tanto, necesitamos nuevas métricas diseñadas para esos valores continuos.

Por ejemplo, imagine que estamos intentando predecir el precio de una casa dadas sus características.

Esa sería una tarea de regresión o intentar predecir el país.

Una casa está adentro.

Dadas sus características, sería una tarea de clasificación.

Y nuevamente estamos enfocados ahora en cómo evaluar esa tarea de regresión donde una

etiqueta es continua y no son categorías separadas.

Por lo tanto, nuevamente para analizar las métricas de evaluación más comunes para la regresión, que son el

error absoluto medio significa error al cuadrado y luego el error al cuadrado medio raíz.

Comencemos con el más simple, que es el error absoluto medio.

Y este es el más fácil de entender, esencialmente todo lo que vas a hacer es comparar tus

predicciones y recordar que estamos comparando un valor continuo aquí, ya que esta es una tarea de regresión,

vamos a comparar nuestras predicciones con las la etiqueta y verdadera, por ejemplo, compara la predicción real del precio

de la vivienda con el precio de la vivienda real y lo que hacemos es simplemente tomar la diferencia entre el precio

verdadero menos nuestro precio predicho, por eso tomamos el valor absoluto de eso y la razón por la que tomamos

el el valor absoluto se debe a que técnicamente nuestras predicciones podrían estar por encima o por

debajo del valor verdadero y dado que queremos promediar todas nuestras predicciones, tomamos el valor absoluto.

De acuerdo, ese es el error absoluto medio, esencialmente solo estás tomando las diferencias entre tu predicción

y la etiqueta verdadera, tomas el valor absoluto de eso y luego promedias

eso para todas tus predicciones.



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














