from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

# Load trained model
model = joblib.load(r"C:\Users\Sri Pranav\Downloads\traffic-dashboard\backend\model\traffic_model.pkl")

@app.route("/")
def home():
    return "Traffic Severity Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    temperature = data["temperature"]
    visibility = data["visibility"]
    wind_speed = data["wind_speed"]
    humidity = data["humidity"]
    hour = data["hour"]

    features = np.array([[temperature, visibility, wind_speed, humidity, hour]])
    
    prediction = model.predict(features)[0]

    return jsonify({"severity": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
