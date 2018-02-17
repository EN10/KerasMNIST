# load mnist data
from tensorflow.python.keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#####################################################################################

# display an image from mnist
import matplotlib.pyplot as plt

i = 2
plt.imshow(x_train[i])
print (y_train[i])
print x_train[i].shape

#####################################################################################

# upload and save file

from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

filename = 'test1.png'
with open(filename, 'w') as f:
  f.write(uploaded[filename])

#####################################################################################

# load and display image
  
from PIL import Image
x = Image.open('test1.png')

import matplotlib.pyplot as plt
plt.imshow(x)