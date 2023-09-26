import streamlit as st
from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from tensorflow.keras import preprocessing
from tensorflow.keras.models import load_model
from tensorflow.keras.activations import softmax
import os
import h5py

st.header=("Image class predictor")

def main():
    file_uploaded = st.file_uploader("Choose the file", type =['jpg', 'png', 'jpeg'])
    image= Image.open(file_uploded)
    figure= plt.figure()
    plt.imshow(image)
    plt.axis('off')
    result = predict_class(image)
    st.write(result)
    st.pyplot(figure)

def predict_class(image):
    classifier_model= tf.keras.models.load_mode(r'/content/gdrive/MyDrive/bunga/databunga/my_model.hdf5')
    shape=((128, 128, 3))
    model= tf.keras.Sequential(hub[hub.KerasLayer(classifier_model, input_shape=shape)])
    test_image= image.resize((128, 128))
    test_image= preprocessing.image.img_to_array(test_image_
    test_image= test_image/225.0
    test_image= np.expand_dims(test_image, axis=0)
    class_image= ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']
    predictions= model.predict(test_image)
    scores= tf.nn.softmax(predictions[0])
    scores= scores.numpy()
    image_class= class_names[np.argmax(scores)]
    result= "The image uploaded is: {}".format(image_class)
    return result
    
if __name__ == "__main__":
    main()
                


