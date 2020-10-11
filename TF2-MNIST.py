"""MNIST
Code based on :
https://www.tensorflow.org/tutorials/quickstart/beginner
"""

import keras
(train_images, train_labels), (test_images, test_labels) = keras.datasets.mnist.load_data()

# improves accuracy ~89% to ~93%
train_images, test_images = train_images / 255.0, test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5)
model.evaluate(test_images, test_labels)
