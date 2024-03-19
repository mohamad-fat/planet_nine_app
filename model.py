import tensorflow as tf
import numpy as np
from PIL import Image

IMG_SHAPE = 150
model_path = 'model/version_0p1.keras'
objects = ['sun', 'Mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto', 'moon']
model = tf.keras.models.load_model(model_path, compile=False)

def preprocessing_image(image_path):
    img = Image.open(image_path)
    img = img.resize((IMG_SHAPE, IMG_SHAPE))
    img = np.array(img) / 255.0
    return img

def predict_object(img_path):
    image = preprocessing_image(img_path)
    predicted = model.predict(np.expand_dims(image, axis=0))

    predicted_object = objects[np.argmax(predicted)]
    predicted_proba = np.max(predicted)

    predicted[0][np.argmax(predicted)] = 0
    second_predicted = objects[np.argmax(predicted)]
    second_proba = np.max(predicted)

    predicted[0][np.argmax(predicted)] = 0
    third_predicted = objects[np.argmax(predicted)]
    third_proba = np.max(predicted)

    data = [
        (predicted_object, predicted_proba),
        (second_predicted, second_proba),
        (third_predicted, third_proba)
    ]
    return data


