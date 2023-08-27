import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD

# Generar datos aleatorios
np.random.seed(0)
num_samples = 100
X = np.random.rand(num_samples, 2)  # Puntos en un plano
y = (X[:, 0] + X[:, 1] > 1).astype(int)  # Clasificar puntos por encima de la línea x + y = 1

# Construir el modelo
model = Sequential([
    Dense(1, activation='sigmoid', input_shape=(2,))
])

# Compilacion del modelo, utilizando optimiador SGD (Descenso de Gradiente Estocástico)
# Ajustando de forma automatica los pesos de las neuronas
model.compile(optimizer=SGD(learning_rate=0.1), loss='binary_crossentropy', metrics=['accuracy'])

# Entrenar el modelo donde se utiliza model.fit, que durante cada iteración (época) del entrenamiento,
# el modelo hace predicciones para las entradas de entrenamiento, calcula función de pérdida y luego ajusta los pesos
# hacia atrás en la red neuronal utilizando el algoritmo de retropropagación para minimizar la función de pérdida.
model.fit(X, y, epochs=50, batch_size=8, verbose=2)

# Evaluación
test_loss, test_acc = model.evaluate(X, y, verbose=2)
print("\nTest accuracy:", test_acc)

predictions = model.predict(X)

# Convertir las probabilidades en clases predichas (0 o 1) usando un umbral
threshold = 0.5
predicted_classes = (predictions > threshold).astype(int)

# Matriz de confusión
confusion_matrix = tf.math.confusion_matrix(y, predicted_classes, num_classes=2)
print("Matriz de Confusión:")
print(confusion_matrix)

import matplotlib.pyplot as plt

# Lista de puntos de colores
colors = ['blue' if label == 0 else 'green' for label in y]

# Diferenciación de colores
plt.scatter(X[:, 0], X[:, 1], c=colors)
plt.xlabel('X1')
plt.ylabel('X2')

# Pesos aprendidos por el modelo
weights = model.layers[0].get_weights()[0]
bias = model.layers[0].get_weights()[1]

# Línea que separa las clases
x_range = np.array([0, 1.2])
y_range = -(weights[0] * x_range + bias) / weights[1]
plt.plot(x_range, y_range, color='black')

plt.show()
