# EV Charging Hub Suitability Analysis Using Satellite Image Classification

## Project Overview

This project uses a Convolutional Neural Network (CNN) to classify satellite images into Industrial, Residential, and Highway categories. Based on the identified land type, the system estimates the suitability of a location for EV charging hub installation.

## Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* Streamlit
* CNN (Convolutional Neural Network)

## Dataset

* EuroSAT Satellite Image Dataset
* Classes Used:

  * Industrial
  * Residential
  * Highway

## Features

* Satellite image classification
* Image preprocessing and data augmentation
* CNN-based multiclass classification
* EV charging hub suitability estimation
* Interactive Streamlit web application

## Project Workflow

1. Collect satellite images from EuroSAT dataset.
2. Preprocess images using resizing and normalization.
3. Train CNN model for land classification.
4. Predict land type from uploaded image.
5. Generate EV charging hub suitability score.
6. Display results through Streamlit interface.

## Results

* Trained on 3,000+ satellite images.
* Achieved approximately 90% classification accuracy.
* Successfully classified Industrial, Residential, and Highway regions.

## Author

Rohit Swamy 
