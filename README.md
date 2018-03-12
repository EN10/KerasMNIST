# Keras MNIST

cnn.py training based on [keras mnist_cnn.py](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py)  
cnnPredict.py inference based on [Flask app.py](https://github.com/llSourcell/how_to_deploy_a_keras_model_to_production/blob/master/app.py)  
cnn.h5 pretrained Keras model  

TFKeras is based on simplified [MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners#the_mnist_data) and cnn.py.  
TFKeras.py, TFKeras.h5 & TFKpredict only uses Dense and so is less accurate than CNN.  
TFKpredict is a slimmed version of cnnPredict.  

TFKeras is 92% accurate vs CNN 99.25%  
CNN can detect digit `1` better.

[Keras.js MNIST CNN Demo](https://transcranial.github.io/keras-js/#/mnist-cnn)

Code Documentation:  
* `batch_size` number of images per loop step
* `epochs` number of train loops
* `num_classes` there are 10 digits 0-9
* `x_train.astype('float32')` trains faster than int
* `x_train /= 255` from 0-255 to 0-1
* `verbose=1` 1 for progress bar logging
* `imread('test3.png',mode='L')` [‘L’ (8-bit pixels, black and white)](http://scipy.github.io/devdocs/generated/scipy.misc.imread.html#scipy.misc.imread)

[kerasDataset.py](https://github.com/EN10/KerasMNIST/blob/master/kerasDataset.py) equivalent to TFKeras.py using the keras dataset rather than the tensorflow dataset.  
[KerasTFDataset.py](https://github.com/EN10/KerasMNIST/blob/master/KerasTFDataset.py) simplified example of [TFKeras.py](https://github.com/EN10/KerasMNIST/blob/master/TFKeras.py)    
[jupyter.py](https://github.com/EN10/KerasMNIST/blob/master/jupyter.py) has matplotlib and colab examples.    

Keras Documentation:  
* [to_categorical](https://keras.io/utils/#to_categorical) aka one_hot
* [Dense](https://keras.io/layers/core/#dense)
* [Flatten](https://keras.io/layers/core/#flatten)

## Install
Tensorflow:
    
    sudo pip install -U pip  
    sudo pip install tensorflow 

Keras:  

    sudo apt update 
    sudo apt install python-dev 
    sudo pip install keras

Save Model:

    sudo pip install h5py

imread:

    sudo pip install pillow 

disable "cpu_feature_guard":  
`export TF_CPP_MIN_LOG_LEVEL=2`