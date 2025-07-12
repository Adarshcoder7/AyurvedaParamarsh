from flask import Blueprint, render_template, request
from ml.remedies import remedies_dict
from ml.predict import predict_dosha

ml_bp = Blueprint('ml', __name__)

def get_dosha_tip(dosha):
    if dosha == "Vata":
        return "Stay warm, eat grounding foods, and follow a regular routine."
    elif dosha == "Pitta":
        return "Stay cool, avoid spicy food, and use calming herbs."
    elif dosha == "Kapha":
        return "Stay active, avoid heavy food, and use warming herbs."
    else:
        return "Please enter more detailed symptoms for better results."

@ml_bp.route('/quiz')
def quiz():
    return render_template("quiz.html")

@ml_bp.route('/remedies', methods=['POST'])
def remedies():
    user_text = request.form.get("symptoms", "").lower()
    matched = {
        symptom: remedy
        for symptom, remedy in remedies_dict.items()
        if symptom in user_text
    }

    # Expand matches if too few
    if len(matched) < 3:
        keywords = user_text.split()
        for keyword in keywords:
            for symptom in remedies_dict:
                if keyword in symptom and symptom not in matched:
                    matched[symptom] = remedies_dict[symptom]

    dosha = predict_dosha(list(matched.keys()))
    tips = get_dosha_tip(dosha)

    return render_template("remedies.html", dosha=dosha, tips=tips, remedies=matched, user_text=user_text)
from ml.remedies import get_multiple_remedies

@ml_bp.route('/predict', methods=['POST'])
def predict():
    query = request.form.get("symptom")
    results = get_multiple_remedies(query)
    return render_template("remedies.html", results=results)

