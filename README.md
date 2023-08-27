# RedNeuronal

## Proyecto Final Calculo Empresarial

### Cristian Vargas

### Gabriel Corrales

## Descenso de gradiente aplicado a una neuronal con retro propagación.

### ¿Qué es una red neuronal?
Una red neuronal es un modelo matemático y computacional inspirado en la estructura y el funcionamiento del sistema nervioso biológico, diseñado para procesar información y aprender patrones a partir de datos, está compuesta por una serie de unidades interconectadas llamadas neuronas artificiales que a través de una organización en capas y conexiones ponderadas, pueden realizar tareas de procesamiento de información, como clasificación, regresión, reconocimiento de patrones y toma de decisiones, mediante el ajuste de sus conexiones durante el entrenamiento.

Una red neuronal es una herramienta fundamental en el campo del aprendizaje automático y la inteligencia artificial que permite a las máquinas aprender y realizar tareas complejas de manera autónoma al procesar datos de entrada y generar salidas basadas en patrones aprendidos.

### Descenso de gradiente.
El descenso de gradiente es un método de optimización utilizado en matemáticas y aprendizaje automático para encontrar el mínimo de una función, en el contexto del aprendizaje automático, esta función generalmente se conoce como función de costo o pérdida, y el objetivo es ajustar los parámetros de un modelo para minimizar esta función y, por lo tanto, mejorar el rendimiento del modelo.
El proceso del descenso de gradiente implica calcular el gradiente (una medida de la pendiente) de la función de costo con respecto a los parámetros del modelo en cada iteración, luego, se ajustan los parámetros en la dirección opuesta al gradiente, escalado por una tasa de aprendizaje, con el fin de acercarse al mínimo de la función de costo.

### Retro propagación.
La retropropagación es un algoritmo fundamental para entrenar redes neuronales en el aprendizaje profundo (deep learning), su objetivo principal es ajustar los pesos de las conexiones en una red neuronal de manera que la función de costo se minimice, lo que implica mejorar el rendimiento del modelo en la tarea específica para la que se está entrenando.

### Cómo funciona la retropropagación?

1. Propagación hacia adelante: En la fase de propagación hacia adelante, los datos de entrada se introducen en la red neuronal y se propagan a través de las capas ocultas hasta llegar a la capa de salida. Cada neurona realiza una serie de cálculos ponderados y pasa su resultado a través de una función de activación.
2. Cálculo de la función de costo: Luego, se calcula una función de costo que mide la diferencia entre la salida estimada y la salida desead para cada muestra de entrenamiento.
3. Retropropagación del error: En esta etapa, se calcula el gradiente de la función de costo con respecto a los pesos de la red. Este gradiente se calcula utilizando la regla de la cadena y el cálculo de derivadas parciales, la retropropagación implica calcular cómo un pequeño cambio en cada peso afecta el cambio en la función de costo.
4. Actualización de pesos: Después de calcular el gradiente, se utiliza el descenso de gradiente para ajustar los pesos de la red en la dirección opuesta al gradiente, multiplicado por una tasa de aprendizaje (learning rate). 
5. Iteración: Los pasos 1 a 4 se repiten iterativamente para todas las muestras de entrenamiento, el proceso se repite durante varias épocas hasta que la función de costo converja o hasta que se alcance un criterio de detención.
6. Convergencia y evaluación: Finalmente una vez que la función de costo ha convergido o se ha cumplido un criterio de detención se evalúa el rendimiento del modelo en un conjunto de datos de prueba independiente para verificar su capacidad de generalización.
La retropropagación es esencial para el entrenamiento eficiente de redes neuronales profundas ya que permite ajustar los pesos de manera que el modelo pueda aprender a representar y generalizar a partir de los datos de entrenamiento, puede ser utilizada en combinación con diversas técnicas de optimización y regularización para mejorar el rendimiento y la estabilidad del modelo.


### Aplicándolo a una Red Neuronal
El descenso de gradiente es una técnica crucial para entrenar redes neuronales en el aprendizaje profundo (deep learning). Aquí te explico cómo se aplica el descenso de gradiente a las redes neuronales:
1. Inicialización de pesos: Al comenzar el entrenamiento de una red neuronal, los pesos de las conexiones entre las neuronas se inicializan generalmente de manera aleatoria o con valores pequeños cercanos a cero.
2. Propagación hacia adelante: Durante la fase de entrenamiento, los datos de entrada se propagan a través de la red neuronal, capa por capa, para calcular una salida estimada. Cada neurona realiza una serie de cálculos ponderados y pasa su resultado a través de una función de activación. Esto se hace para todas las muestras de entrenamiento.
3. Cálculo de la función de costo: Se calcula una función de costo que mide la diferencia entre la salida estimada y la salida deseada (etiqueta real) para cada muestra de entrenamiento. La función de costo cuantifica qué tan bien está funcionando la red en términos de predicción.
4. Cálculo del gradiente: El siguiente paso es calcular el gradiente de la función de costo con respecto a los pesos de la red. Esto se hace utilizando la regla de la cadena y el cálculo de derivadas parciales. El gradiente indica la dirección y la magnitud del cambio necesario en cada peso para reducir la pérdida o costo.
5. Actualización de pesos: Los pesos de la red se actualizan utilizando el gradiente calculado. Aquí es donde entra en juego el descenso de gradiente. Los pesos se ajustan en la dirección opuesta al gradiente multiplicado por una tasa de aprendizaje (learning rate). La tasa de aprendizaje controla cuánto se ajustan los pesos en cada iteración.
6. Iteración: Los pasos 2 a 5 se repiten iterativamente para todas las muestras de entrenamiento (en el caso de descenso de gradiente estocástico) o para mini-lotes de muestras (en el caso del descenso de gradiente mini-batch). Esto se repite durante varias épocas hasta que la función de costo converja o hasta que se alcance un criterio de detención.
7. Convergencia y evaluación: La red neuronal se sigue entrenando hasta que la función de costo converja a un mínimo o hasta que se cumplan ciertos criterios de detención. Luego, se evalúa el rendimiento del modelo en un conjunto de datos de prueba independiente.
8. Ajuste hiperparámetros: Durante el proceso de entrenamiento, es importante ajustar hiperparámetros como la tasa de aprendizaje y la arquitectura de la red para obtener un rendimiento óptimo.

Este proceso se repite hasta que el modelo alcance un rendimiento satisfactorio en la tarea que se le asigna. En resumen, el descenso de gradiente se utiliza para ajustar automáticamente los pesos de las conexiones en una red neuronal, lo que permite que la red aprenda y se adapte a los patrones en los datos de entrenamiento
