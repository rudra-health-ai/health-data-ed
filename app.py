from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to Disease + Nutrition Predictor API'

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Check if 'symptoms' key exists
    if not data or 'symptoms' not in data:
        return jsonify({'error': 'No symptoms provided'}), 400

    symptoms = data['symptoms'].lower()

    # Simple rule-based logic
    if "fever" in symptoms and "cough" in symptoms:
        disease = "Flu"
        nutrition = ["Vitamin C", "Warm fluids", "Protein"]
    elif "headache" in symptoms:
        disease = "Migraine"
        nutrition = ["Magnesium-rich foods", "Hydration"]
    else:
        disease = "Unknown"
        nutrition = ["Balanced diet", "Sleep"]

    return jsonify({
        "disease": disease,
        "nutrition": nutrition,
        "mood": "Take care 💙",
        "hydration": "2–3L per day"
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
