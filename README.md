# AgriTech: AI-Powered Plant Disease Diagnostic System

 **Live Demo:** (https://huggingface.co/spaces/Mohsan-Javed/agritech-diagnostic)

AgriTech is an intelligent agricultural tool that utilizes Deep Learning to identify diseases in vegetable crops instantly. By analyzing leaf images, this system helps farmers and gardeners detect pathogens early, ensuring better crop yields and reducing the unnecessary use of chemical treatments.

## Features
* **Real-time Diagnostic:** Upload a photo and get an instant disease classification.
* **Specialized Model:** Specifically tuned for high-impact vegetable crops (Tomato, Potato, Pepper).
* **High Reliability:** Uses a Convolutional Neural Network (CNN) with 90%+ accuracy.
* **Responsive UI:** Clean, modern interface built with Streamlit.

## 🛠️ Tech Stack
* **Language:** Python 3.11
* **Deep Learning Framework:** TensorFlow / Keras
* **Web Interface:** Streamlit
* **Deployment:** Hugging Face Spaces

## Supported Classes (14 Categories)
The model is trained to recognize the following 14 specific states across three major crop types:

### Bell Pepper
* Bacterial Spot
* Healthy

### Potato
* Early Blight
* Late Blight
* Healthy

### Tomato
* Bacterial Spot
* Early Blight
* Late Blight
* Leaf Mold
* Septoria Leaf Spot
* Spider Mites (Two-spotted)
* Target Spot
* Yellow Leaf Curl Virus
* Healthy

## Installation and Deployment
1. Clone the repository:
   ```bash
   git clone [https://github.com/Mohsan-Javed/agritech-diagnostic.git](https://github.com/Mohsan-Javed/agritech-diagnostic.git) ```
2. Install dependencies:
```bash
pip install -r requirements.txt 
```

3. Run the application:

```bash
streamlit run app.py 
```
