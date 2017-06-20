# Keras MNIST

cnn.py training based on [keras mnist_cnn.py](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py)  
predict.py inference based on [Flask app.py](https://github.com/llSourcell/how_to_deploy_a_keras_model_to_production/blob/master/app.py)  
cnn.h5 pretrained Keras model  

TFKeras is based on simplified [MNIST For ML Beginners](https://www.tensorflow.org/get_started/mnist/beginners#the_mnist_data) and cnn.py.  
TFKeras.py, TFKeras.h5 & TFKpredict only uses Dense and so is less accurate than CNN.  
TFKeras is 92% accurate vs CNN 99.25%  

CNN can detect digit `1` better.

Code Documentation:  
* `batch_size` number of images per loop step
* `epochs` number of train loops
* `num_classes` there are 10 digits 0-9
* `x_train.astype('float32')` trains faster than int
* `x_train /= 255` from 0-255 to 0-1
* `verbose=1` 1 for progress bar logging

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