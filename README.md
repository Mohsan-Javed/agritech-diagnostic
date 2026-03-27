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

  ## ⚙️ Technical Optimizations & Performance

To move beyond a baseline implementation, I focused on **Systems Engineering** principles to ensure the app is viable for real-world field use.

### Real-Time Latency Profiling
In agricultural settings, connectivity and hardware constraints are common. I implemented a **latency profiling layer** that measures the end-to-end inference time for every diagnostic request. 
* **The Goal:** Monitor model efficiency and ensure response times remain under the 500ms threshold for a seamless user experience.
* **The Result:** Average inference speed on Hugging Face CPU-tier is consistently profiled between 150ms–300ms.

### Defensive Programming & Reliability
* **Confidence Thresholding:** Implemented logic to flag "Uncertain" results if the model's confidence falls below 60%, preventing false positives in non-ideal lighting conditions.
* **Resource Management:** Optimized the TensorFlow environment to use `tensorflow-cpu` to reduce container size and improve startup time by ~40%.

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
