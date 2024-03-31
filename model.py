import numpy as np
from PIL import Image
import keras

IMG_SHAPE = 300
model_path = './model/version_0p4.keras'
objects = ['earth', 'jupiter', 'mars', 'mercury', 'moon', 'neptune', 'pluto', 'saturn', 'sun', 'uranus', 'venus']
model = keras.models.load_model(model_path)
def preprocessing_image(image_path):
    img = Image.open(image_path)
    img = img.resize((IMG_SHAPE, IMG_SHAPE))
    img = np.array(img) / 255.0
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

img_path = './to_predict/saturn2.jpeg'

predict_object(img_path)


