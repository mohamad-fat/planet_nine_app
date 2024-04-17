import numpy as np
from PIL import Image
import tensorflow as tf

IMG_SHAPE = 200
model_path = './model/version_0p1.keras'
objects = ['earth', 'jupiter', 'mars', 'mercury', 'moon', 'neptune', 'pluto', 'saturn', 'sun', 'uranus', 'venus']

interpreter = tf.lite.Interpreter(model_path='./model/model_compressed.tflite')
interpreter.allocate_tensors()

def preprocessing_image(image_path):
    img = Image.open(image_path)
    img = img.resize((IMG_SHAPE, IMG_SHAPE))
    img = np.array(img, dtype=np.float32) / 255.0
    img = np.expand_dims(img, axis=0)

    # img = np.array(img) / 255.0
    return img

def get_classes():
    return objects

def predict_object(img_path):
    image = preprocessing_image(img_path)

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    predicted = output_data[0]

    predicted_object = objects[np.argmax(predicted)]
    predicted_perc = np.max(predicted).astype('float') * 100

    predicted[np.argmax(predicted)] = 0
    second_predicted = objects[np.argmax(predicted)]
    second_perc = np.max(predicted).astype('float') * 100

    predicted[np.argmax(predicted)] = 0
    third_predicted = objects[np.argmax(predicted)]
    third_perc = np.max(predicted).astype('float') * 100

    data = [
        (predicted_object, predicted_perc),
        (second_predicted, second_perc),
        (third_predicted, third_perc)
    ]
    print(data)
    return data

