AgriTech: AI-Powered Plant Disease Diagnostic System
AgriTech is a specialized Computer Vision tool designed to identify 14 distinct health states in high-impact vegetable crops (Tomato, Potato, and Bell Pepper). By leveraging Transfer Learning and MobileNetV2, this system provides near-instant diagnostics to help farmers mitigate crop loss and reduce chemical overuse.

Key Technical Highlights
Transfer Learning Architecture: Utilized a pre-trained MobileNetV2 backbone for its optimal balance between parameter efficiency and high accuracy (90%+).

Real-Time Latency Profiling: Developed a custom profiling layer to monitor end-to-end inference. Achieved a consistent response time of 150ms–300ms on CPU-tier infrastructure.

Defensive Prediction Logic: Integrated a 60% confidence threshold. If the model's Softmax output is low, the system flags the result as "Uncertain," preventing false positives caused by poor lighting or non-leaf images.

Production-Ready Deployment: Optimized the environment using tensorflow-cpu to reduce container overhead by 40%, ensuring fast startup and stable performance on Hugging Face Spaces.

Model Performance & Dataset
The model was trained on the PlantVillage dataset, focusing on 14 specific categories:

Bell Pepper: Bacterial Spot, Healthy.

Potato: Early Blight, Late Blight, Healthy.

Tomato: Bacterial Spot, Early/Late Blight, Leaf Mold, Septoria Spot, Spider Mites, Target Spot, Yellow Leaf Curl, and Healthy.

Tech Stack
Engine: TensorFlow / Keras (MobileNetV2)

Interface: Streamlit

Environment: Python 3.11, tensorflow-cpu

Hosting: Hugging Face Spaces (Docker-based)

Engineering & Optimization (The "Deep Dive")
1. Why MobileNetV2?
Unlike heavy architectures (VGG/ResNet), MobileNetV2 uses depthwise separable convolutions. This makes the model lightweight enough to eventually run on-device (Edge AI) without losing the feature-extraction power needed for subtle fungal patterns.

2. Inference Speed vs. Resource Constraints
To simulate real-world field use, the app includes a Latency Tracker. By profiling every request, I identified that image resizing was a bottleneck and optimized the preprocessing pipeline to ensure the "Wait Time" for a farmer is virtually zero.

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
