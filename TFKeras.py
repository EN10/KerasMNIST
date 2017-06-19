from tensorflow.examples.tutorials.mnist import input_data
import keras

mnist = input_data.read_data_sets("./mnist", one_hot=True)

model = keras.models.Sequential()
model.add(keras.layers.Dense(10, activation='softmax', input_shape=(784,)))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(mnist.train.images, mnist.train.labels,
          batch_size=128,
          epochs=20,
          verbose=1)
          
model.save('TFKeras.h5')