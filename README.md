# Keras MNIST

cnn.py training based on [keras mnist_cnn.py](https://github.com/fchollet/keras/blob/master/examples/mnist_cnn.py)  
predict.py inference based on [Flask app.py](https://github.com/llSourcell/how_to_deploy_a_keras_model_to_production/blob/master/app.py)  
cnn.h5 pretrained Keras model 

## Install
Keras:  

    sudo apt update 
    sudo apt install python-dev 
    sudo pip install keras

Tensorflow:
    
    sudo pip install -U pip  
    sudo pip install tensorflow 
    sudo pip install pillow 
    
disable "cpu_feature_guard":  
`export TF_CPP_MIN_LOG_LEVEL=2`