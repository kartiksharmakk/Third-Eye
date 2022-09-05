from PIL import Image
#import matplotlib.pyplot as plt
import tensorflow as tf
from prediction import predict_caption
from extract_features import extract_features
import os
import pickle
import keras
import pyttsx3

max_length=35
WORKING_DIR = 'working/'
BASE_DIR='input/'

#loading RNN-LSTM model
model = keras.models.load_model(os.path.join(WORKING_DIR, 'image_caption_RNN_LSTM_model.h5'))

# loading
with open(os.path.join(WORKING_DIR, 'tokenizer.pickle'), 'rb') as handle:
    tokenizer = pickle.load(handle)

# load features from pickle
with open(os.path.join(WORKING_DIR, 'features.pkl'), 'rb') as f:
    features = pickle.load(f)

def generate_caption(image_name,image_path):
    try:
        image_id = image_name.split('.')[0]
        y_pred = predict_caption(model,features[image_id], tokenizer, max_length)
        return y_pred
        
    except KeyError:
        # load the image    
        y_pred = predict_caption(model,extract_features(image_name,image_path), tokenizer, max_length)
        print("_________________________________________________________")
        print(y_pred)
        tf.keras.backend.clear_session()
        return y_pred

