import numpy as np
import cv2
from tensorflow.keras.models import load_model

IMG_SIZE = 64

# Load trained model
model = load_model("cnn_model.h5")
def predict_location(image):

    img = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    img = img / 255.0
    img = img.reshape(1, 64, 64, 3)

    prediction = model.predict(img, verbose=0)[0]

    predicted_class = np.argmax(prediction)

    classes = ["Industrial", "Residential", "Highway"]

    land_type = classes[predicted_class]

    # Rule-based scoring
    if land_type == "Highway":

        score = 0.90
        label = "Highly Suitable"

        commercial = 0.70
        traffic = 0.95
        powerline = 0.80

    elif land_type == "Industrial":

        score = 0.75
        label = "Suitable"

        commercial = 0.90
        traffic = 0.65
        powerline = 0.75

    else:

        score = 0.45
        label = "Moderately Suitable"

        commercial = 0.50
        traffic = 0.40
        powerline = 0.45

    return (
        label,
        score,
        commercial,
        traffic,
        powerline
    )