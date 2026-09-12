# ❤️ Heart Disease Prediction

An end-to-end Machine Learning web application that predicts the likelihood of heart disease based on patient health and clinical parameters.

The project uses a **K-Nearest Neighbors (KNN)** classification model and provides an interactive interface built with **Streamlit**.

## 🚀 Live Demo

🔗 **Live App:** https://heart-disease-prediction-chetna.streamlit.app/

> If the URL changes after deployment, replace the link above with your final Streamlit URL.

---

## 📌 Project Overview

Heart disease is one of the major health concerns worldwide. Early identification of potential risk can help in taking appropriate medical advice and preventive measures.

This project demonstrates how Machine Learning can be used to analyze health-related features and predict whether a person is likely to have heart disease.

The application allows users to enter patient information through a simple web interface and receive an ML-based prediction instantly.

> ⚠️ **Disclaimer:** This application is created for educational and demonstration purposes only. It is not a medical diagnostic tool and should not replace professional medical advice.

---

## 🎯 Objectives

* Build a Machine Learning model for heart disease prediction.
* Perform data preprocessing and feature transformation.
* Train a KNN classification model.
* Scale input features using `StandardScaler`.
* Save and reuse the trained model using `joblib`.
* Develop an interactive Streamlit web application.
* Deploy the application online using Streamlit Community Cloud.

---

## 🧠 Machine Learning Model

### K-Nearest Neighbors (KNN)

The project uses the **K-Nearest Neighbors (KNN)** classification algorithm.

KNN predicts the class of a new data point by comparing it with nearby data points from the training dataset.

The model predicts two possible outcomes:

* `0` → Lower likelihood of heart disease
* `1` → Higher likelihood of heart disease

---

## 📊 Input Features

The application takes the following inputs:

| Feature             | Description                                    |
| ------------------- | ---------------------------------------------- |
| Age                 | Age of the patient                             |
| Sex                 | Gender                                         |
| Chest Pain Type     | Type of chest pain                             |
| Resting BP          | Resting blood pressure                         |
| Cholesterol         | Serum cholesterol level                        |
| Fasting Blood Sugar | Whether fasting blood sugar is above 120 mg/dl |
| Resting ECG         | Resting electrocardiogram result               |
| Max Heart Rate      | Maximum heart rate achieved                    |
| Exercise Angina     | Exercise-induced angina                        |
| Oldpeak             | ST depression caused by exercise               |
| ST Slope            | Slope of the peak exercise ST segment          |

---

## 🔄 Machine Learning Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Feature Encoding
   ↓
Train-Test Split
   ↓
Feature Scaling
   ↓
KNN Model Training
   ↓
Model Evaluation
   ↓
Save Model & Scaler
   ↓
Streamlit Application
   ↓
Live Deployment
```

---

## 🖥️ Application

The Streamlit application provides an easy-to-use interface where users can enter patient information.

After clicking the **Predict** button, the application:

1. Collects user input.
2. Converts categorical values into the required format.
3. Aligns the input with the model's expected features.
4. Applies the saved scaler.
5. Sends the processed data to the KNN model.
6. Displays the prediction.

---

## 📁 Project Structure

```text
Heart-Disease-Prediction/
│
├── app.py
├── KNNheart.pkl
├── scaler.pkl
├── expected_columns.pkl
├── requirements.txt
└── README.md
```

### File Description

* **`app.py`** → Streamlit application.
* **`KNNheart.pkl`** → Trained KNN model.
* **`scaler.pkl`** → Saved feature scaler.
* **`expected_columns.pkl`** → Saved feature-column structure used during preprocessing.
* **`requirements.txt`** → Required Python dependencies.
* **`README.md`** → Project documentation.

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* GitHub
* Streamlit Community Cloud

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/chetna123-ch/heart-disease-prediction.git
```

### 2. Navigate to the project directory

```bash
cd heart-disease-prediction
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📦 Requirements

The main dependencies are:

```text
streamlit
pandas
numpy
scikit-learn
joblib
```

---

## ☁️ Deployment

This application is deployed using **Streamlit Community Cloud**.

Deployment process:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
requirements.txt
       ↓
app.py
       ↓
Live Web Application
```

---

## 🔮 Future Improvements

* Add more advanced Machine Learning models.
* Compare KNN with Logistic Regression, Random Forest and SVM.
* Add model performance metrics.
* Add probability/confidence visualization.
* Improve UI/UX with charts and better visual design.
* Add comprehensive input validation.
* Perform hyperparameter tuning for KNN.
* Add model explainability features.

---

## 👩‍💻 Author

### Chetna Gehlot

**B.Tech Student | Aspiring AI/ML Engineer**

Interested in Machine Learning, Data Science, Python, and building practical AI/ML projects.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

### ⚠️ Medical Disclaimer

This project is intended strictly for **educational and demonstration purposes**. The predictions generated by this application should not be considered medical advice, diagnosis, or treatment recommendations. Always consult a qualified healthcare professional for medical evaluation.
