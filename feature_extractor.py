import cv2
import numpy as np
from pathlib import Path
from tensorflow.keras.models import load_model

IMG_SIZE = 64

MODEL_PATH = Path(__file__).parent / "cnn_model.h5"
model = load_model(MODEL_PATH)


def predict_location(image):

    img = cv2.resize(image, (IMG_SIZE, IMG_SIZE))
    img = img.astype("float32") / 255.0
    img = img.reshape(1, IMG_SIZE, IMG_SIZE, 3)

    prediction = model.predict(img, verbose=0)[0]

    predicted_class = np.argmax(prediction)

    classes = [
        "Industrial",
        "Residential",
        "Highway"
    ]

    land_type = classes[predicted_class]

    if land_type == "Highway":

        score = 0.90
        recommendation = "Highly Suitable"

        commercial = 0.70
        traffic = 0.95
        powerline = 0.80

    elif land_type == "Industrial":

        score = 0.75
        recommendation = "Suitable"

        commercial = 0.90
        traffic = 0.65
        powerline = 0.75

    else:

        score = 0.45
        recommendation = "Moderately Suitable"

        commercial = 0.50
        traffic = 0.40
        powerline = 0.45

    return (
        land_type,
        recommendation,
        score,
        commercial,
        traffic,
        powerline
    )