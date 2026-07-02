# ⚡ EV Charging Hub Suitability Analysis

## 🚀 Live Demo

https://ev-charging-app-suitability-analysis.streamlit.app/

## Overview

The **EV Charging Hub Suitability Analysis** project is a Deep Learning-based web application that analyzes satellite images and predicts whether a location is suitable for establishing an EV charging station.

The application uses a **Convolutional Neural Network (CNN)** trained on satellite imagery to classify the uploaded image into one of three land categories:

* 🏭 Industrial
* 🏘 Residential
* 🛣 Highway

Based on the predicted land type, a rule-based decision system estimates the suitability of the location for EV charging infrastructure.

---

## Features

* Upload satellite images through a user-friendly Streamlit interface.
* Classify land into Industrial, Residential, or Highway.
* Display an overall suitability score.
* Show infrastructure assessment using:

  * Commercial Index
  * Accessibility Index
  * Infrastructure Index
* Provide a recommendation for EV charging hub deployment.
* Clean and responsive dashboard.

---

## Project Structure

```text
EV-Charging-Hub-Suitability-Analysis/
│
├── app.py
├── feature_extractor.py
├── cnn_model.h5
├── requirements.txt
├── README.md
└── sample_images/
```

---

## Technologies Used

* Python
* Streamlit
* TensorFlow / Keras
* OpenCV
* NumPy
* Pillow

---

## Model Workflow

1. Upload a satellite image.
2. Resize the image to **64 × 64** pixels.
3. Normalize the image.
4. Pass the image to the trained CNN model.
5. Predict the land category.
6. Apply rule-based suitability analysis.
7. Display the prediction and recommendation.

---

## Land Categories

### 🏭 Industrial

* High commercial activity
* Strong supporting infrastructure
* Good accessibility
* Suitable for public EV charging stations

### 🏘 Residential

* Moderate infrastructure
* Suitable for community charging
* Lower traffic density
* Best suited for residential EV users

### 🛣 Highway

* High traffic movement
* Good road connectivity
* Suitable for fast-charging stations
* Ideal for long-distance travel

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Rohit-swamy/EV-Charging-Hub-Suitability-Analysis.git
```

Move into the project directory:

```bash
cd EV-project
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Sample Usage

1. Launch the application.
2. Upload a satellite image.
3. Click **Analyze Location**.
4. View:

   * Predicted Land Type
   * Suitability
   * Suitability Score
   * Infrastructure Assessment
   * Final Recommendation

---

## Current Limitations

* The suitability score is generated using a rule-based mapping after land classification.
* Infrastructure indices are predefined based on the predicted land category.
* The model currently supports only three land classes.

---

## Future Enhancements

* Dynamic suitability scoring using prediction confidence.
* Additional land categories.
* GIS and map integration.
* Real-time location analysis.
* Automatic report generation.
* Cloud deployment.

---

## Author

**Rohit Swamy**

Bachelor of Engineering (Computer Science)

Project: **EV Charging Hub Suitability Analysis**

---

## License

This project is developed for educational and learning purposes.
