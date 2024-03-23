import tensorflow as tf
import numpy as np
from PIL import Image

IMG_SHAPE = 260
model_path = 'model/version_0p1.keras'
objects = ['earth', 'jupiter', 'mars', 'mercury', 'moon', 'neptune', 'pluto', 'saturn', 'sun', 'uranus', 'venus']
model = tf.keras.models.load_model(model_path, compile=False)

def preprocessing_image(image_path):
    img = Image.open(image_path)
    # img = tf.image.resize_with_crop_or_pad(img, IMG_SHAPE, IMG_SHAPE)
    img = img.resize((IMG_SHAPE, IMG_SHAPE))
    # img = np.array(img) / 255.0
    return img

def get_classes():
    return objects

def predict_object(img_path):
    image = preprocessing_image(img_path)
    predicted = model.predict(np.expand_dims(image, axis=0))

    predicted_object = objects[np.argmax(predicted)]
    predicted_perc = np.max(predicted).astype('float') * 100

    predicted[0][np.argmax(predicted)] = 0
    second_predicted = objects[np.argmax(predicted)]
    second_perc = np.max(predicted).astype('float') * 100

    predicted[0][np.argmax(predicted)] = 0
    third_predicted = objects[np.argmax(predicted)]
    third_perc = np.max(predicted).astype('float') * 100

    data = [
        (predicted_object, predicted_perc),
        (second_predicted, second_perc),
        (third_predicted, third_perc)
    ]
    print(data)
    return data


