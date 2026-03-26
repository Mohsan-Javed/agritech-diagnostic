import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="AgriTech | Diagnostic System", layout="wide")

# --- 2. PROFESSIONAL THEMING (CSS) ---
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #2e7d32;
        color: white;
    }
    h1 {
        color: #1b5e20;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .reportview-container .main .block-container{
        padding-top: 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. LOAD MODEL ---
@st.cache_resource
def load_my_model():
    return tf.keras.models.load_model('agritech_plant_disease_90.keras')

model = load_my_model()

class_indices = {
    0: 'Pepper Bell: Bacterial Spot', 1: 'Pepper Bell: Healthy', 
    2: 'Potato: Early Blight', 3: 'Potato: Late Blight', 4: 'Potato: Healthy', 
    5: 'Tomato: Bacterial Spot', 6: 'Tomato: Early Blight', 7: 'Tomato: Late Blight', 
    8: 'Tomato: Leaf Mold', 9: 'Tomato: Septoria Leaf Spot', 
    10: 'Tomato: Spider Mites', 11: 'Tomato: Target Spot', 
    12: 'Tomato: Yellow Leaf Curl Virus', 13: 'Tomato: Mosaic Virus', 14: 'Tomato: Healthy'
}

# --- 4. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("AgriTech Control")
    st.info("System Status: Operational")
    st.write("This diagnostic tool utilizes a Deep Learning MobileNetV2 architecture to identify plant pathology from leaf imagery.")
    st.divider()
    st.caption("Developed for AgriTech Solutions")

# --- 5. MAIN INTERFACE ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("Upload Specimen")
    uploaded_file = st.file_uploader("Select an image file (JPG, PNG)", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Original Input', use_container_width=True)

with col2:
    st.header("Analysis Output")
    if uploaded_file is not None:
        with st.spinner('Running Neural Diagnostics...'):
            # Preprocessing
            img = image.resize((224, 224))
            img_array = np.array(img)
            if img_array.shape[-1] == 4:
                img_array = img_array[:, :, :3]
            img_array = img_array / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Prediction
            predictions = model.predict(img_array)
            result_index = np.argmax(predictions)
            confidence = np.max(predictions) * 100

            # Results
            st.metric(label="Primary Classification", value=class_indices[result_index])
            st.write(f"**Confidence Rating:** {confidence:.2f}%")
            st.progress(int(confidence))
            
            # Contextual Advice
            st.divider()
            if confidence > 80:
                st.success("High-Confidence Diagnosis: Proceed with standard treatment protocols for the identified pathology.")
            else:
                st.warning("Low-Confidence Diagnosis: The system recommends a secondary inspection or a clearer sample for verification.")
    else:
        st.write("Please upload a specimen image to begin analysis.")