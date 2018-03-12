from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("mnist", one_hot=True)

from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Activation

model = Sequential()
model.add(Dense(10, input_shape=(784,)))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(mnist.train.images, mnist.train.labels, epochs=20, batch_size=128)

scores = model.evaluate(mnist.test.images, mnist.test.labels, verbose=1)
print('Test accuracy:', scores[1])