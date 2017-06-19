from scipy.misc import imread
import numpy as np
x = imread('test3.png',mode='L')
#compute a bit-wise inversion so black becomes white and vice versa
x = np.invert(x)
#convert to a 4D tensor to feed into our model
x = x.reshape(1,784).astype('float32') / 255

#perform the prediction
from keras.models import load_model
model = load_model('TFKeras.h5')
out = model.predict(x)
print(np.argmax(out))