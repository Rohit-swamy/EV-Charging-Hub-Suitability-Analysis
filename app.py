import streamlit as st
import cv2
import numpy as np
from PIL import Image
from feature_extractor import predict_location

st.set_page_config(page_title="EV Charging Hub Predictor")

st.title("⚡ EV Charging Hub Location Predictor")

uploaded_file = st.file_uploader(
    "Upload Satellite Image",
    type=["jpg","png","jpeg"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(image, use_container_width=True)

    image_np = np.array(image)

    if st.button("Analyze Location"):

        label, score, commercial, traffic, powerline = predict_location(image_np)

        st.subheader("Prediction")

        st.write("Suitability Score:", round(float(score), 2))

        st.success(label)

        st.subheader("Extracted Infrastructure Parameters")

        st.write("Commercial Activity:", round(float(commercial), 2))
        st.progress(min(int(commercial * 100), 100))

        st.write("Traffic Density:", round(float(traffic), 2))
        st.progress(min(int(traffic * 100), 100))

        st.write("Powerline Proximity:", round(float(powerline), 2))
        st.progress(min(int(powerline * 100), 100))