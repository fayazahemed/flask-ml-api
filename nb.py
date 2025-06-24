from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Model API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array([[data['age'], data['salary']]])
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
