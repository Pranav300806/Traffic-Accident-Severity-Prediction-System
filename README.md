🚦 Traffic Accident Severity Predictor (ML Web App)

An end-to-end Machine Learning web application that predicts traffic accident severity (1–4) using weather and time-based features.

This project demonstrates the complete ML pipeline from data preprocessing → model training → API development → frontend integration.

📌 Problem Statement

Road accidents cause injuries, traffic delays and economic loss.
Predicting accident severity in advance can help authorities and drivers take preventive actions.

This project builds a machine learning model to predict accident severity based on environmental conditions.

📊 Dataset

Dataset used: US Accidents (2016–2023)
Source: Kaggle

Features used from dataset:

Start Time (converted to Hour)

Temperature (F)

Visibility (miles)

Wind Speed (mph)

Humidity (%)

Target:

Accident Severity (1 to 4)

🤖 Machine Learning Model

Model used:

Random Forest Classifier

Why Random Forest?

Works well on tabular data

Handles non-linear relationships

Good baseline for real-world prediction

⚙️ ML Pipeline

1️⃣ Load dataset
2️⃣ Clean and preprocess data
3️⃣ Convert time → hour feature
4️⃣ Train/Test split
5️⃣ Train RandomForest model
6️⃣ Save trained model (.pkl)
7️⃣ Build Flask API for predictions
8️⃣ Integrate frontend UI with API

🧠 Input Features for Prediction

The web app accepts:

Feature	Description
Temperature	Weather temperature
Visibility	Visibility in miles
Wind Speed	Wind speed
Humidity	Humidity percentage
Hour	Time of day (0–23)

Output:
👉 Predicted Accident Severity (1–4)

🌐 Web Application

The project includes:

✔️ Trained ML model
✔️ Flask REST API
✔️ Frontend UI for user input
✔️ Real-time predictions

📸 Project UI
![UI](frontend/UI.png)

🛠 Tech Stack

Backend

Python

Pandas

Scikit-learn

Flask

Joblib

Frontend

HTML

CSS

JavaScript

▶️ How to Run Locally
1️⃣ Train the model
python backend/model/train_model.py

2️⃣ Run Flask API
cd backend
python app.py


Server runs at:

http://127.0.0.1:5000

3️⃣ Open Frontend

Open frontend/index.html in browser.

🔌 API Endpoint

POST /predict

Example request:

{
  "temperature":70,
  "visibility":5,
  "wind_speed":10,
  "humidity":60,
  "hour":14
}


Example response:

{
  "severity": 3
}

🎯 Project Highlights

End-to-end ML project

Real dataset (large scale)

REST API integration

Frontend + Backend connection

Ready for deployment

👨‍💻 Author

Pranav


