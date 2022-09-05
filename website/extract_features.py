import os
import pickle
import numpy as np
from tensorflow.keras.models import Model
import keras
import tensorflow as tf

from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

WORKING_DIR = 'working/'
BASE_DIR='static/img/'

def extract_features(image_name,image_path):
    #load vgg16model
    #model = VGG16()
    #restructure the model
    #model = Model(inputs=model.inputs, outputs=model.layers[-2].output)

    #load pretrained and restructred VGG16 model
    model=keras.models.load_model(os.path.join(WORKING_DIR, 'vgg16_feature_extractor.h5'))
    # extract features from image
    features = {}
    # load the image from file
    #img_path = os.path.join(BASE_DIR, image_name)
    image = load_img(image_path, target_size=(224, 224))
    # convert image pixels to numpy array
    image = img_to_array(image)
    # reshape data for model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
    # preprocess image for vgg
    image = preprocess_input(image)
    # extract features
    feature = model.predict(image, verbose=0)
    # get image ID
    image_id = image_name.split('.')[0]
    # store feature
    features[image_id] = feature
    tf.keras.backend.clear_session()

    return features[image_id]