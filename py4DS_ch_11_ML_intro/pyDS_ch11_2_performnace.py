
################# 0: FULL
# copy: Analyze: analyze this text, get the topics, 
#       output in english: describe the topics on your own knowledge withot losing context, use clarification and fix any misconception (mention them)
#        
################# (10-May-25 for 11-May-25)

# Courses: PrTla PY for DS & ML >    14.4, 14.5


----------------------    Use google translate:    -----------------------------

------------------------------
00:03:55,430 --> 00:03:56,910
de prueba x.
------------------------------


==================  9.00  =====================
Confusion matrix:

Now we can also see all the "correctly classified" versus "incorrectly classified" images in the form of a confusion matrix.
So the confusion matrix looks something like this:

multi level Table:
----------------------------------------------------------------------------------------------------------
|                    |                      | **Predicted Condition**        |                                 |
| :----------------- | :------------------- | :----------------------------- | :------------------------------ |
|                    | **Total Population** | **Predicted Positive**         | **Predicted Negative**          |
| **True Condition** | **Actual Positive**  | True Positive (TP)             | False Negative (FN) *(Type II error)* |
|                    | **Actual Negative**  | False Positive (FP) *(Type I error)* | True Negative (TN)              |
----------------------------------------------------------------------------------------------------------

true condition:
We have the underlying true conditions.
That's the true correct label, and we can think of the condition as positive or negative, like
actually being a dog or not being a dog, or often used in a medical diagnosis, like having the presence of
a disease as opposed to not having it.


predicted condition
We have the predicted condition from the models.
So, positive prediction or negative prediction, and I think when it comes to confusion matrices, it's often
easier to first get an intuition if you think of this as a diagnostic test for having some type of disease present
in a person after maybe taking a blood sample and running it through your model.

---------------  GPT  ---------------


Sure — here’s a simplified, clear version without losing context:

---

### 📊 **Confusion Matrix Simplified**

* A **confusion matrix** shows how many predictions were **correct** or **incorrect** by comparing predicted and actual labels.

---

**Structure:**

|                     | **Predicted Positive**               | **Predicted Negative**                |
| :-----------------: | :----------------------------------- | :------------------------------------ |
| **Actual Positive** | True Positive (TP)                   | False Negative (FN) *(Type II error)* |
| **Actual Negative** | False Positive (FP) *(Type I error)* | True Negative (TN)                    |

---

**Key Ideas:**

* **True Condition:**
  The actual, correct label — e.g. whether the image is *actually a dog* or *not a dog*, or in medical tests, *has a disease* or *doesn't have it*.

* **Predicted Condition:**
  What the model predicts — positive or negative.

* **Use Case Example:**
  Think of this like a medical test:

  * *Positive prediction* → model says person has disease
  * *Negative prediction* → model says person doesn’t
    The confusion matrix tracks where the model was right and wrong.

---

Would you like a small diagram-style illustration version too?



|                    |                      | **Predicted Condition**        |                                 |
| :----------------- | :------------------- | :----------------------------- | :------------------------------ |
|                    | **Total Population** | **Predicted Positive**         | **Predicted Negative**          |
| **True Condition** | **Actual Positive**  | True Positive (TP)             | False Negative (FN) *(Type II error)* |
|                    | **Actual Negative**  | False Positive (FP) *(Type I error)* | True Negative (TN)              |


----  9.48  ----


So, for example, a true positive would be someone who actually has that disease and your model correctly predicts

that they have it; a true negative would be someone who doesn't have the disease and your model correctly predicts

that they don't have the disease.

So, you have true positives and true negatives, and both are correct predictions, and then we essentially have

these two types of incorrect predictions: a false positive and a false negative. A false positive would be if the person

doesn't have the disease, and you predict that it's a false positive because you're falsely saying that they're

positive for this disease or this condition. A false negative is essentially

the opposite of where this person has the disease present, and then you report using your model and your

test that they're actually negative, they actually don't have this disease, and sometimes

they're also called, and the statistics are, a type 1 error and a type 2 error, and

then from these true negative results, true positive results, false negative results, and false positive results.

There are many other metrics you can calculate, so we can see some of them here.

In the bottom left corner, we can see the actual accuracy calculation. It's the sum of true positives plus true negatives, essentially the sum of the total population guesses.

There are a bunch of others, like the positive probability rate, false positive rate, prevalence rate, and false positive rate.




















Part 2: 

Welcome back, everyone.

We just discussed how to evaluate performance for classification problems.

Now let's understand how to evaluate performance for regression testing, so we can take a moment to discuss how we evaluate a model that is performing some type of regression task.

And, in general, a regression is the task when a model tries to predict continuous values.

Unlike classification tasks, where we are trying to predict categorical values, you may have heard of some evaluation metrics, such as precision or recall, as we just discussed.

However, these types of metrics will not be useful for regression problems.

It doesn't really make sense to calculate the precision or recall of a regression task since you are actually classifying things.

Instead, you are predicting a continuous value.

Therefore, we need new metrics designed for those continuous values.

For example, imagine we are trying to predict the price of a house given its characteristics.

That would be a regression task, or trying to predict the country.

A house is inside.

Given its characteristics, it would be a classification task.

And again, we're focused now on how to evaluate that regression task where a label is continuous and not separate categories.

So, again, to look at the most common evaluation metrics for regression, which are the

mean absolute error (mean squared error) and then the root mean squared error.

Let's start with the simplest, which is the mean absolute error.

And this is the easiest one to understand. Essentially, all you're going to do is compare your predictions.

And remember, we're comparing a continuous value here since this is a regression task.

We're going to compare our predictions with the label and the true one. For example, compare the actual house price prediction with the actual house price.

And what we do is simply take the difference between the true price minus our predicted price. That's why we take the absolute value of that. The reason we take the absolute value is because technically, our predictions could be above or below the true value.

And since we want to average all of our predictions, we take the absolute value.

Okay, that's the mean absolute error. You're essentially just taking the differences between your prediction and the true label. You take the absolute value of that, and then you average that for all of your predictions.

Now, the problem with the mean absolute error is that it won't punish large errors.

So here we have what's known as an ans comes quartet, and we can see here that we have a wide variety

of different spreads of data points here.

However, the line of best fit for all of these is actually the same.

So we want to make sure we're aware of situations like this.

For example, let's take a look at this specific situation.

We have one point that's a huge outlier, so we want our air metrics to really account for them.

So what we can do is use a mean squared error.

And this is the mean of the squared errors.

So what we're doing here is taking the difference between the true value minus our predicted value and we're going to square it.

And as you can imagine, when we actually square that error, the larger errors are more noticeable than with mean absolute error, which makes squared error more popular because it's actually going to punish your model for those outliers it doesn't fit.

And we no longer need to take the absolute value because anything squared ends up being positive.

However, there's another problem we run into with a squared error that squares the actual label minus its prediction.

It actually also squares the units themselves.

So, for example, if you're predicting the price of a house, our error metric with mean absolute error would be in dollars, but with mean squared error.

We end up getting an error metric in units of dollars squared, which is hard to interpret, so the way we solve this is with the root mean squared error. Essentially, at the end, you just take the square root of your mean squared error.

So this is the most popular because it punishes those larger error values ​​and

at the end of the day, it has the same metrics or the same units as y now.

The most common question I get from students is: Hey, does this squared error mean this value?

I got it right.

And as always, context is everything.

Let's imagine you were doing some kind of machinery model and got a squared error.

























Bienvenidos a todos a esta conferencia sobre evaluación del desempeño, particularmente para problemas de clasificación en la

próxima conferencia.

Discutiremos la evaluación del rendimiento para las protestas de regresión, por lo que acabamos de enterarnos de que después de que

se complete un proceso de aprendizaje automático, utilizaremos métricas de rendimiento para evaluar cómo lo hizo realmente

nuestro modelo.

Y seguimos mencionando el hecho de que entrenamos nuestro modelo en los datos de entrenamiento y luego usaremos

algún tipo de métrica para ver realmente cómo se desempeñó en el conjunto de prueba o el conjunto de validación.

Entonces sigamos y discutamos lo que eso realmente significa.

Qué métricas de clasificación vamos a utilizar y las métricas de clasificación clave

que deberíamos comprender nuestra precisión, precisión de recuerdo y puntaje f1, pero primero debemos entender el razonamiento detrás de estas

métricas y cómo funcionarán realmente en el mundo real típicamente en cualquier tarea de clasificación su modelo en

realidad solo puede lograr dos resultados, o bien su modelo fue correcto en su

predicción o su modelo fue incorrecto en su predicción y todas las métricas de clasificación provienen de esta idea, ahora

afortunadamente incorrecta versus correcta también se expande a situaciones en las que tiene múltiples clases como

intentar para predecir categorías de más de dos.

Por ejemplo, tiene Categoría A B C D Puede ser correcto al predecir la categoría correcta o

incorrecto al predecir la categoría correcta.

Ahora con el fin de explicar las métricas, vamos a seguir adelante y simplificar esto a lo

que se conoce como una situación de clasificación binaria binaria que significa dos.

Por lo tanto, solo hay dos clases disponibles, ya sea clase 0 o clase 1.

Y esta idea también se expandirá a múltiples clases.

Pero para simplificar, imaginemos solo una situación de clasificación binaria, por lo que en nuestro ejemplo intentaremos predecir si una imagen

es un perro o un gato realmente realizará esta tarea más adelante durante la convolución de toda

la parte de la red neuronal de este curso.

Ahora, dado que es un problema de aprendizaje supervisado, lo que tendremos que hacer primero es ajustar o entrenar un modelo

sobre datos de entrenamiento.

Eso significa que tendremos imágenes de que alguien ya se ha adelantado y etiquetado como perro o gato.

Entonces sabemos la respuesta correcta en estas imágenes y luego vamos a probar ese modelo en los datos de prueba.

Así que vamos a mostrar nuevas imágenes que la modelo no ha visto antes.

Obtenga la predicción de los modelos y luego compare los resultados de la predicción del modelo con la

respuesta correcta que ya conocemos.

Entonces, una vez que tenemos las predicciones de los modelos de los datos de la prueba X, la comparamos con los valores verdaderos de y.

Las etiquetas correctas, así que en realidad diagramamos este proceso.

Imaginemos que ya hemos entrenado nuestro modelo en algunos datos de entrenamiento y ahora es el momento de evaluar

realmente el rendimiento del modelo.

Aquí es donde entra nuestro conjunto de datos de prueba.

Entonces tomamos una imagen de prueba de donde vamos a etiquetar x prueba X que significa característica.

Por lo tanto, la imagen en sí misma es una característica y esto es del conjunto de prueba y hay una etiqueta

correcta correspondiente de la prueba Y.

Entonces tenemos la característica o imagen X y esa es la imagen de prueba y también tenemos la etiqueta correcta de la

prueba Y.

Y en este caso podemos ver que esta imagen es una imagen de un perro.

Entonces, lo que vamos a hacer es alimentar las características.

En este caso, la imagen en nuestro modelo ya entrenado y luego el modelo hará alguna predicción.

Entonces, el modelo predice que se trata de un perro y luego lo que hacemos es comparar la predicción con la

etiqueta correcta.

Entonces este perro igual al perro en este caso era correcto, sin embargo, tal vez predijo que esta imagen era un gato.

Y en este caso, esta comparación con la etiqueta correcta sería incorrecta.

Y estas son esencialmente las dos únicas situaciones.

O tienes razón o estás equivocado, correcto o incorrecto, así que repetimos este proceso para todas las imágenes en nuestros datos



------------------------------
00:03:55,430 --> 00:03:56,910 :: DONE 9-May-2025
de prueba x.
------------------------------

de prueba x.

Y al final tendremos un recuento de coincidencias correctas y una cuenta de coincidencias incorrectas.

Y la realización clave aquí que tenemos que hacer es que en el mundo real no todas las coincidencias

incorrectas o correctas tienen el mismo valor.

Entonces, vamos a concentrarnos en lo que queremos decir con eso, de modo que en el mundo real una sola

métrica no contará la historia completa y, para comprender todo esto, recuperemos esas cuatro métricas que mencionamos y veamos cómo

se calculan realmente.

Podríamos organizar nuestros valores pronosticados en comparación con los valores reales y lo que se

conoce como una matriz de confusión, por lo que tocaremos la matriz de confusión más adelante.

Pero primero hablemos de la precisión, la precisión es una de las métricas de clasificación más comunes.

Y afortunadamente también es el más fácil de entender.

Es realmente intuitivo lo que mide la precisión de la precisión y los problemas

de clasificación es la cantidad de predicciones correctas realizadas por el modelo dividido por la cantidad o la cantidad total de predicciones.

Entonces, de nuevo, es el número de predicciones correctas dividido por el número

total de predicciones esencialmente respondiendo a las preguntas cuántas predicciones acerta como porcentaje, así que, por ejemplo, imaginemos

que el conjunto de prueba X tenía 100 imágenes y nuestro modelo predijo correctamente 80 imágenes.

Luego tenemos 80 dividido por 100 o cero punto, ocho u 80 por ciento de precisión y la precisión es realmente útil cuando

las clases objetivo están bien equilibradas.

Entonces que significa eso.

Bien equilibrado bien en nuestro ejemplo.

Eso significaría que tenemos aproximadamente la misma cantidad de imágenes de gatos que imágenes de perros en todos nuestros datos.

Por lo tanto, significa que las etiquetas en sí mismas están más o menos igualmente representadas en el conjunto de datos, pero imaginemos que tenemos

lo que se conoce como una situación de clase desequilibrada.

En este caso, la precisión no es una buena métrica para usar.

Así que hagamos un pequeño experimento mental.

Imaginemos que en este conjunto de pruebas teníamos noventa y nueve imágenes de perros y solo una imagen de un gato.

Ahora, si nuestro modelo fuera simplemente una línea que siempre predijo el perro, sin importar la imagen que viera, obtendríamos una precisión del

noventa y nueve por ciento en este conjunto de prueba en particular porque simplemente diciendo que el

perro noventa y nueve imágenes son perros y una imagen de un gato entonces solo nos perdimos uno.

Es por eso que debes ser consciente de la desventaja de la precisión y la desventaja realmente viene

cuando tienes una situación de clase desequilibrada.

Si sus clases están más o menos equilibradas, la precisión es un método intuitivo muy agradable o una métrica para comprender.

Sin embargo, si tiene una clase desequilibrada, puede ver en esta situación particular

donde comienza a representar un problema y ahí es donde entran en juego las otras métricas.

Entonces, nuevamente en esta situación, querremos comprender el recuerdo y la precisión que nos ayudan a comprender qué tan

bien se está desempeñando en el retiro de clases desequilibradas es la capacidad de un modelo para encontrar todos los casos relevantes dentro de

un conjunto de datos y la definición precisa del recuerdo es la cantidad conocidos como verdaderos positivos y lo vamos a

afinar más adelante cuando veamos la matriz de confusión.

Pero es el número de verdaderos positivos dividido por el número de verdaderos positivos

más el número de falsos negativos y la precisión es la capacidad de un modelo de clasificación para identificar solo los puntos

de datos relevantes donde la precisión se define como el número de verdaderos positivos divididos por el

número de positivos verdaderos más un número de falsos positivos ahora.

A menudo, usted tiene una compensación entre el recuerdo y la precisión, mientras que el recuerdo expresa la capacidad de

encontrar todas las instancias relevantes en un conjunto de datos. La precisión expresa la proporción de los puntos

de datos que nuestro modelo dice que eran relevantes y que realmente eran relevantes, y luego el puntaje F1 es esencialmente una combinación de

estos dos.


-----------------------------
00:07:42,670 --> 00:07:43,570 :: DONE 9-May-2025
estos dos.
-----------------------------

En los casos en que queremos encontrar una combinación óptima de precisión y recuperación, podemos combinar

las dos métricas utilizando lo que se conoce como la puntuación F1 y la puntuación F1 es la media armónica de precisión y recuperación teniendo

en cuenta ambas métricas en la siguiente ecuación.

Entonces, esto no es solo tomar el promedio de precisión de registro, sino tomar la media armónica de ellos.

Y aquí tenemos la fórmula para el puntaje F1 o los puntajes F1 iguales a dos veces.

Los tiempos de precisión se recuerdan en el numerador y luego se dividen por la precisión más el recuerdo en el denominador, por lo

que la razón por la que usamos la media armónica en lugar de solo una media simple o un promedio

simple es porque va a castigar valores extremos.

Por ejemplo, si creó un clasificador que tenía una posición de 1 que significaba una precisión esencialmente perfecta

y una recuperación de cero era esencialmente el peor registro posible.

Si solo tomaras el promedio simple de esto, entonces sería cero punto cinco.

Pero el puntaje F1 porque se ha tomado un armónico significa que tenemos tiempos de precisión recuperados allí en la parte superior, lo

que significa que obtienes cero veces uno de los mejores y obtienes un puntaje F1 de cero.

Esto es realmente bueno porque te permite castigar las diferencias extremas entre la precisión y la recuperación, por lo

que te da una especie de evaluación justa de esa compensación entre precisión y recuperación.

Ahora también podemos ver todas las imágenes clasificadas correctas versus clasificadas incorrectamente en forma de una

matriz de confusión.

Entonces, la matriz confusa se parece a esto.

Tenemos las verdaderas condiciones subyacentes.

Esa es la verdadera etiqueta correcta y podemos pensar que la condición es positiva o negativa, como

ser realmente un perro o no ser un perro o, a menudo, se usa en un diagnóstico médico, como tener presencia de

una enfermedad en lugar de no tenerla. Tenemos la condición predicha de los modelos.

Entonces, predicción positiva o predicción negativa y creo que cuando se trata de matrices de confusión, a menudo es

más fácil primero tener una intuición si piensas en esto como una prueba de diagnóstico para tener algún tipo de enfermedad presente

en una persona después de que tal vez tomes una muestra de sangre y ejecútalo a través de tu modelo.

Entonces, por ejemplo, un verdadero positivo sería alguien que realmente tiene esa enfermedad y su modelo que predice correctamente

que lo tiene, un verdadero negativo sería alguien que no tiene la enfermedad y su modelo

que predice correctamente que no tiene la enfermedad.

Entonces, tenga verdaderos positivos y verdaderos negativos, y ambas son predicciones correctas y luego tenemos esencialmente

estos dos tipos de predicciones incorrectas: un falso positivo y un falso negativo un falso positivo serían si la persona

no tiene la enfermedad y usted predice que es falso positivo porque estás diciendo falsamente que son

positivos para esta enfermedad o esta condición, un falso negativo es esencialmente

lo contrario de donde esta persona tiene la enfermedad presente y luego informas usando tu modelo y tu

prueba que en realidad es negativo, en realidad no tienen esta enfermedad y a veces

también se les llama y las estadísticas son un error de tipo 1 y un error de tipo 2 y

luego de estos resultados negativos verdaderos positivos verdaderos falsos negativos y resultados falsos positivos.

Hay muchas otras métricas que puede calcular, por lo que podemos ver algunas de ellas aquí,

como en la esquina inferior izquierda, podemos ver el cálculo real de la precisión, es la

suma de los verdaderos positivos más los verdaderos negativos, esencialmente la suma de lo que acertó la población

total y hay un montón de otros como tasa de probabilidad positiva tasa de falsos positivos tasa de prevalencia de

falsos positivos tasa de



-----------------------------
00:11:08,300 --> 00:11:09,660
falsos positivos tasa de
-----------------------------


falsos descubrimientos, etc. Ahora el punto principal a recordar aquí es que la matriz de

confusión y las diversas métricas calculadas son esencialmente todas formas fundamentales de comparar el valor predicho frente a los

valores verdaderos y lo que constituye una buena métrica en realidad depende de la situación específica.

Una pregunta muy común que recibo de los estudiantes es, oye, es una precisión lo suficientemente buena.

Bueno, eso realmente depende de su situación y el contexto de la situación.

Ahora, si todavía estás confundiendo la matriz de confusión, no hay problema.

Echa un vistazo a la página de wikipedia para ello.

Tiene un diagrama realmente bueno con todo lo más importante para todas las métricas y, a lo largo

de la capacitación, este curso generalmente solo iba a imprimir métricas, como imprimir la precisión básica.

Ahora, antes de terminar esta conferencia, quiero volver a la pregunta inicial que mencioné que los

estudiantes me preguntan todo el tiempo cuál es esta idea de cuál es una precisión suficientemente buena.

Y como siempre, esto realmente depende del contexto de la situación en la que está ejecutando su modelo.

No hay un número único que pueda dar.

Decir algo así como una precisión del 90 por ciento es lo suficientemente bueno para cada situación.

Ya vimos el problema con las clases desequilibradas, pero tampoco hay un comentario realmente bueno que pueda

dar sobre lo que es una precisión o recuerdo lo suficientemente bueno y tenemos que pensar en el contexto de la situación.

Entonces, pensemos de nuevo en ese modelo que es diagnóstico para predecir la presencia de una enfermedad.

Entonces, si creamos un modelo para predecir la presencia de una enfermedad, lo primero en lo que queremos

pensar es si vamos a tener clases de equilibrio o clases desequilibradas.

Entonces, la presencia de la enfermedad está bien equilibrada en la población general y, en la mayoría de los casos, probablemente

no lo sea.

Probablemente no haya una enfermedad que vaya a suceder donde aproximadamente la mitad de la población se ve afectada y

la mitad de la población no se ve afectada.

Por lo tanto, ya podemos decir que tendremos una situación de clase desequilibrada,

lo que significa que tendremos una compensación de recuperación de precisión, por lo que también debemos tener en cuenta que a menudo estos modelos se usan como

pruebas de diagnóstico rápido antes de tener una prueba más invasiva .

Por ejemplo, para los modelos de cáncer de próstata es muy común hacer una simple prueba de orina antes de hacerse

una biopsia porque es mucho más fácil hacerse la prueba de orina que someterse a una biopsia completa

de la próstata.

Entonces, también debemos considerar qué está en juego si se trata de cáncer de próstata.

Las apuestas son en realidad bastante altas.



------------------------------------
00:13:23,510 --> 00:13:25,500
Las apuestas son en realidad bastante altas.
------------------------------------



Entonces, como mencionamos, a menudo tenemos esa compensación de precisión, lo que significa que esencialmente necesitamos decidir si el

modelo debe enfocarse en la fijación de falsos positivos versus falsos negativos.

Entonces, a costa de disminuir los falsos negativos.

Lo más probable es que aumentemos los falsos positivos y viceversa.

Y en el diagnóstico de la enfermedad, probablemente sea mejor tratar de minimizar la cantidad de falsos negativos

a costa de aumentar la cantidad de falsos positivos.

Entonces va en la dirección de estos falsos positivos.

¿Y por qué realmente queremos hacer eso?

Bueno, queremos asegurarnos de clasificar correctamente la mayor cantidad posible de casos de la enfermedad.

Entonces, a costa de aumentar los falsos positivos, hacemos todo lo posible para disminuir los falsos negativos.

En este contexto de diagnóstico de enfermedad y por qué realmente queremos hacer eso.

Bueno, queremos asegurarnos de que cualquier persona que realmente tenga algún tipo de presencia de esta enfermedad o en este caso

de este ejemplo, el cáncer de próstata.

Si estamos haciendo esa prueba de orina, queremos asegurarnos de que todas esas personas que tengan

la presencia de la enfermedad realmente pasen al siguiente paso.

Esa es quizás una prueba más invasiva como una biopsia.

Y recuerde que este tipo generalmente tiene un costo de aumentar esos falsos positivos.

Entonces, nuestros modelos no serán perfectos y eventualmente sucederá como alguien que

no tiene la enfermedad cuando hacemos nuestra simple prueba de orina o cualquiera que sea nuestro modelo

de aprendizaje automático va a predecir que hey, lo siento, pero tiene la presencia positiva de esta enfermedad y será

un error porque será un falso positivo.

Sin embargo, cuando reciban pruebas más invasivas, se darán cuenta de que lo siento, fue un falso positivo.

En realidad estas bien.

No tienes esta enfermedad y eso viene porque estamos tratando de minimizar los falsos negativos.

Lo que realmente no queremos cuando se trata de algo tan importante como tener cáncer o una enfermedad,

realmente no queremos rechazar a alguien que realmente tiene una enfermedad y decirles que no tienen la

enfermedad.

Por lo tanto, sea un falso negativo cuando se trata del diagnóstico de la enfermedad.

Eso es algo que realmente queremos minimizar.

Queremos minimizar esos falsos negativos para que no extrañemos accidentalmente a alguien de inmediato con nuestra

herramienta de diagnóstico y les digamos que no tienen la enfermedad o que no tienen cáncer cuando realmente

la tienen.

Por lo tanto, podemos ver algo tan importante como que el diagnóstico de la enfermedad realmente minimiza esos

falsos negativos se vuelve realmente importante y casi todo esto es para decir que el aprendizaje automático no se realizará en

el vacío.

Y estas métricas de rendimiento no tienen algún tipo de verdad universal que sea cierta en todos los problemas,

pero el aprendizaje automático es que es un proceso realmente colaborativo en el que siempre debemos consultar

a expertos en el dominio.

Por ejemplo, en el caso del diagnóstico de la enfermedad, probablemente deberíamos hablar con los médicos de

metal cola sobre cuáles son nuestros estándares aceptables para falsos negativos versus falsos positivos.

Pero como una presencia general de esta enfermedad en la población general, etc., esto va a cambiar dependiendo del

contexto de su situación, así que siempre tenga eso en cuenta.

No habrá una respuesta fácil para mí decir que es una precisión o una precisión

lo suficientemente buena porque todo depende del contexto y el dominio de la situación.

Bien, acabamos de hablar sobre cómo podemos evaluar los modelos de clasificación.

Avancemos y pasemos a la próxima conferencia donde discutimos la evaluación de las tareas de regresión.

Te veré allá.


-----------------------------
00:16:35,990 --> 00:16:36,470
Te veré allá.
-----------------------------










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














