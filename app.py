import streamlit as st
import numpy as np
from PIL import Image
from feature_extractor import predict_location

st.set_page_config(
    page_title="EV Charging Hub Suitability Analysis",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("⚡ EV Charging Hub Suitability Analysis")
st.caption(
    "Upload a satellite image to evaluate its suitability for an EV Charging Hub."
)

with st.sidebar:
    st.header("Project Overview")
    st.write(
        """
This application uses a trained CNN model to classify the uploaded satellite
image into one of the following land categories:

- 🏭 Industrial
- 🏘 Residential
- 🛣 Highway

Based on the predicted land type, the application applies a rule-based
suitability analysis to estimate the feasibility of establishing an EV
Charging Hub.
"""
    )

    st.divider()

    st.subheader("Workflow")

    st.markdown(
        """
1. Upload Satellite Image

2. CNN Land Classification

3. Infrastructure Assessment

4. Suitability Analysis

5. Recommendation
"""
    )

uploaded_file = st.file_uploader(
    "📷 Upload Satellite Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file).convert("RGB")
    image_np = np.array(image)

    left_col, right_col = st.columns([1, 1])

    with left_col:

        st.image(
            image,
            caption="Uploaded Satellite Image",
            use_container_width=True
        )

    with right_col:

        st.subheader("Prediction")

        if st.button(
            "⚡ Analyze Location",
            use_container_width=True
        ):

            with st.spinner("Analyzing image..."):

                (
                    land_type,
                    recommendation,
                    score,
                    commercial,
                    traffic,
                    powerline
                ) = predict_location(image_np)

            st.success("Analysis Completed")

            st.metric(
                "Predicted Land Type",
                land_type
            )

            st.metric(
                "Suitability",
                recommendation
            )

            st.metric(
                "Suitability Score",
                f"{score * 100:.0f}%"
            )

            st.progress(float(score))

            st.divider()

            st.subheader("Infrastructure Assessment")

            c1, c2, c3 = st.columns(3)

            with c1:

                st.metric(
                    "🏢 Commercial Index",
                    f"{commercial * 100:.0f}%"
                )

                st.progress(float(commercial))

            with c2:

                st.metric(
                    "🚗 Accessibility Index",
                    f"{traffic * 100:.0f}%"
                )

                st.progress(float(traffic))

            with c3:

                st.metric(
                    "⚡ Infrastructure Index",
                    f"{powerline * 100:.0f}%"
                )

                st.progress(float(powerline))

            st.divider()

            st.subheader("Location Insights")

            if land_type == "Industrial":

                st.info(
                    """
**Industrial Area**

• High commercial activity

• Better supporting infrastructure

• Good road accessibility

• Suitable for public EV charging stations
"""
                )

            elif land_type == "Highway":

                st.info(
                    """
**Highway Area**

• High traffic movement

• Suitable for fast charging stations

• Good connectivity

• Ideal for long-distance EV users
"""
                )

            else:

                st.info(
                    """
**Residential Area**

• Suitable for neighbourhood charging

• Moderate infrastructure

• Lower traffic density

• Best suited for community EV charging
"""
                )

            st.divider()

            st.subheader("Final Recommendation")

            if score >= 0.80:

                st.success(
                    """
### 🟢 Highly Suitable

This location is highly suitable for establishing an EV Charging Hub.
"""
                )

            elif score >= 0.60:

                st.warning(
                    """
### 🟡 Suitable

This location is suitable for establishing an EV Charging Hub.
"""
                )

            else:

                st.error(
                    """
### 🔴 Moderately Suitable

The location has moderate suitability. Further infrastructure
development is recommended before deployment.
"""
                )

st.divider()

st.caption(
    "Developed using CNN-based satellite image classification for EV Charging Hub Suitability Analysis."
)