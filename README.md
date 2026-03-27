# AgriTech: Deep Learning Plant Pathology Diagnostic System

## Link to live demo
[https://agritech-diagnostic.streamlit.app/](https://huggingface.co/spaces/Mohsan-Javed/agritech-diagnostic)

## Project Overview
AgriTech is an end-to-end computer vision solution designed to identify 15 unique classifications of plant diseases in Tomato, Potato, and Pepper crops. By leveraging transfer learning on the MobileNetV2 architecture, this system provides real-time diagnostic capabilities to assist in precision agriculture and crop management.

## Technical Architecture
* **Base Model**: MobileNetV2 (Pre-trained on ImageNet)
* **Optimization**: Adam Optimizer with a custom learning rate schedule.
* **Regularization**: Dropout layers and Label Smoothing (0.1) to prevent overfitting.
* **Inference Technique**: Test Time Augmentation (TTA) to increase prediction stability by averaging 5 augmented perspectives per specimen.



[Image of a convolutional neural network architecture for image classification]


## Key Features
* **High-Precision Classification**: Achieved 94% validation accuracy on the PlantVillage dataset.
* **Robust Preprocessing**: Automated image normalization and RGB channel verification.
* **Professional Interface**: Streamlit-based dashboard for seamless specimen upload and analysis.
* **Confidence Scoring**: Integrated logic to flag low-confidence results for human review.

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
