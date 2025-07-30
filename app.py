from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Simple disease prediction logic
def predict_disease(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "Flu"
    elif "high sugar" in symptoms or "fatigue" in symptoms:
        return "Diabetes"
    elif "headache" in symptoms:
        return "Migraine"
    elif "cold" in symptoms and "body pain" in symptoms:
        return "Covid-19"
    elif "bloating" in symptoms or "gas" in symptoms:
        return "Digestive Issue"
    else:
        return "Unknown"

nutrition = {
    "Diabetes": ["Avoid sugar", "Eat oats", "Use cinnamon"],
    "Flu": ["Drink warm water", "Eat khichdi", "Turmeric milk"],
    "Migraine": ["Avoid caffeine", "Eat leafy food", "Rest in dark room"],
    "Covid-19": ["Protein food", "Multivitamin", "Fruits"],
    "Digestive Issue": ["Curd", "Ajwain", "Avoid oily food"]
}

mood = {
    "Diabetes": "Fatigue and irritability are common. Stay active.",
    "Flu": "Rest well. Mood may be dull.",
    "Migraine": "Stay in calm, dark place.",
    "Covid-19": "You may feel isolated. Stay connected.",
    "Digestive Issue": "Mood affected by bloating. Eat light."
}

hydration = {
    "Diabetes": "Drink 3.5L/day to flush sugar.",
    "Flu": "Drink 3L warm fluids.",
    "Migraine": "Drink 3L. Dehydration triggers it.",
    "Covid-19": "Drink 3.5L + ORS.",
    "Digestive Issue": "Drink 3L. Coconut water helps."
}

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    user_symptoms = data.get('symptoms', '').lower()

    disease = predict_disease(user_symptoms)

    result = {
        "disease": disease,
        "nutrition": nutrition.get(disease, ["No data"]),
        "mood": mood.get(disease, "No mood data"),
        "hydration": hydration.get(disease, "No hydration advice")
    }

    return jsonify(result)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
