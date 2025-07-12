from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# 🌿 Load NLP model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 🌿 Synonym map
synonym_map = {
    'head pain': 'headache',
    'head is paining': 'headache',
    'stomach upset': 'loose stools',
    'tiredness': 'lethargy',
    'gas': 'acidity',
    'cold': 'congestion',
    'vomit': 'vomiting',
    'anger': 'irritability',
    'skin itch': 'eczema',
    'mood off': 'dull mood'
}

# 🌿 Preprocess input
def preprocess_input(user_input):
    user_input = user_input.lower()
    for phrase, replacement in synonym_map.items():
        user_input = user_input.replace(phrase, replacement)
    return user_input

# 🌿 Remedies dataset
remedies_dict = {
    'dry skin': 'Apply sesame or almond oil before bath. Drink warm water.',
    'constipation': 'Use Triphala at bedtime. Eat fiber-rich warm foods.',
    'insomnia': 'Apply Brahmi oil on scalp. Drink warm milk with nutmeg.',
    'tremors': 'Ashwagandha and yoga help calm the nervous system.',
    'anxiety': 'Practice deep breathing and Brahmi/Ashwagandha therapy.',
    'cold hands': 'Use warm clothing. Drink ginger tea.',
    'joint pain': 'Apply Mahanarayan oil and do light massage.',
    'dizziness': 'Consume dates and almonds. Avoid fasting.',
    'muscle spasms': 'Massage with castor oil. Use Dashmool decoction.',
    'memory loss': 'Brahmi, Shankhpushpi syrup and mental exercises.',
    'panic attacks': 'Pranayama, Tulsi tea and calming herbs like Jatamansi.',
    'restless mind': 'Meditation, Vata-pacifying herbs, regular routine.',
    'back pain': 'Abhyanga with medicated oils. Light stretching.',
    'bone loss': 'Take calcium-rich food, sesame seeds, and Ashwagandha.',
    'incontinence': 'Pelvic yoga, herbal blends like Gokshura.',
    'tinnitus': 'Nasya therapy and avoid cold exposure.',
    'irregular appetite': 'Ginger tea before meals. Eat small frequent meals.',
    'weight loss': 'Milk, ghee, rice, and Shatavari for nourishment.',
    'dry cough': 'Licorice tea, warm water, and honey.',
    'earache': 'Use warm sesame oil drops. Avoid wind exposure.',
    'palpitations': 'Ashwagandha, grounding foods, meditation.',
    'headache': 'Shirodhara with Brahmi oil, avoid loud sounds and spicy foods.',
    'heartburn': 'Drink cold milk, avoid spicy/oily food.',
    'acidity': 'Amla juice, fennel tea, and cooling foods.',
    'skin rashes': 'Use neem paste, apply sandalwood or aloe vera.',
    'acne': 'Avoid fried food, apply turmeric + honey mask.',
    'boils': 'Use neem or turmeric paste externally.',
    'ulcers': 'Licorice root decoction, soft bland diet.',
    'irritability': 'Use Brahmi and meditation. Avoid heat and caffeine.',
    'fever': 'Tulsi + coriander tea, coconut water.',
    'hot flashes': 'Aloe vera juice, Shatavari, cooling herbs.',
    'night sweats': 'Sandalwood oil, stay cool, avoid stimulants.',
    'loose stools': 'Buttermilk with nutmeg. Pomegranate juice.',
    'migraine': 'Shirodhara therapy, avoid light/sun, use Brahmi oil.',
    'inflammation': 'Turmeric milk, giloy, cold compress.',
    'jaundice': 'Bhumiamalaki, sugarcane juice, avoid fatty food.',
    'burning eyes': 'Rose water eye wash, cucumber slices.',
    'hyperacidity': 'Cold milk, Amla, avoid late-night eating.',
    'eczema': 'Apply coconut oil + neem. Avoid sour/spicy foods.',
    'photosensitivity': 'Wear sunglasses, apply aloe vera, use turmeric internally.',
    'peptic ulcers': 'Licorice, ghee, avoid caffeine.',
    'bleeding disorders': 'Pomegranate juice, Durva grass juice.',
    'psoriasis': 'Avoid stress, apply medicated oils like Mahamarichyadi.',
    'IBS': 'Eat soft, light food. Use Bilva, Kutajarishta.',
    'hepatitis': 'Bhumiamalaki, Liv52, light diet.',
    'skin cancer': 'Use turmeric, neem, and consult Ayurvedic oncologist.',
    'lethargy': 'Start day with honey + lemon. Use ginger tea.',
    'weight gain': 'Warm water, Triphala, regular walking.',
    'fluid retention': 'Barley water, coriander seed tea.',
    'high cholesterol': 'Garlic, guggul, avoid fried food.',
    'thyroid issues': 'Trikatu, yoga (sarvangasana), balanced iodine intake.',
    'depression': 'Light therapy, Ashwagandha, and energizing routine.',
    'excess mucus': 'Avoid dairy. Drink tulsi-ginger tea.',
    'congestion': 'Steam inhalation with eucalyptus. Use Sitopaladi churna.',
    'allergies': 'Turmeric, Chyawanprash, Nasya therapy.',
    'sinusitis': 'Steam with carom seeds. Avoid cold food.',
    'sleepiness': 'Wake before 6 AM. Avoid sugar and excess grains.',
    'edema': 'Punarnava, barley water, elevate legs.',
    'obesity': 'Triphala at night. Kapalbhati. Avoid sweets and rice.',
    'joint swelling': 'Use Dashmool oil, avoid heavy food.',
    'hypothyroidism': 'Guggul, yoga, avoid goitrogenic foods.',
    'dull mood': 'Brahmi, sun exposure, active schedule.',
    'deep sleep': 'Avoid naps. Early dinner. Stimulant herbs like Vacha.',
    'low appetite': 'Ginger with salt, lemon juice before meals.',
    'diabetes': 'Methi seeds, Jamun, avoid sugar/wheat.',
    'hypoglycemia': 'Small frequent meals. Dates, jaggery if needed.',
    'oligospermia': 'Shilajit, Ashwagandha, healthy lifestyle.',
    'blood pressure': 'Ashwagandha, Arjuna bark, low salt diet.',
    'gout': 'Avoid beans, tomato, uric acid foods. Guduchi helps.',
    'vatarakta': 'Dashamool kwath, Triphala, avoid fried foods.',
    'rhinitis': 'Nasya therapy, ginger tea, avoid curd.',
    'vomiting': 'Ginger juice + honey. Avoid oily food.',
    'fainting': 'Smell camphor, apply cold water, rest well.',
    'autoimmune fever': 'Giloy, turmeric, proper rest.',
    'inflam skin': 'Neem, Triphala internally. Aloe + turmeric paste externally.',
    'cough': 'Tulsi tea, honey, avoid cold drinks.',
    'nausea': 'Ginger tea, avoid strong smells, light diet.',
    'bloating': 'Ajwain water, avoid carbonated drinks.',
    'gastric issues': 'Triphala, warm water, avoid spicy food.',
    'constipation': 'Warm water, Triphala, fiber-rich foods.',
    'diarrhea': 'Rice water, pomegranate juice, avoid cold foods.',
    'fatigue': 'Ashwagandha, regular sleep, avoid excess sugar.',
    'stress': 'Meditation, Brahmi, avoid stimulants.',
    'irritability': 'Brahmi, meditation, avoid heat and caffeine.',
    'dull skin': 'Use coconut oil, drink warm water, eat fresh fruits.',
    'dry hair': 'Use coconut oil, avoid heat styling, eat healthy fats.',
    'hair fall': 'Brahmi oil massage,Use natural shampoo of reetha,amla,shikakai.',
    'dark circles': 'Apply almond oil, use cucumber slices, get enough sleep.',
    'puffy eyes': 'Use cold tea bags, apply aloe vera gel, get enough rest.',
    'sore throat': 'Gargle with warm salt water, drink ginger tea.',
}

# 🌿 Prepare embeddings
symptom_list = list(remedies_dict.keys())
symptom_embeddings = model.encode(symptom_list)

# 🌿 Remedy match function
def get_multiple_remedies(user_input, threshold=0.70, top_n=2):
    user_input = preprocess_input(user_input)
    user_embedding = model.encode([user_input])
    scores = cosine_similarity(user_embedding, symptom_embeddings)[0]

    matched = []
    for idx, score in enumerate(scores):
        if score >= threshold:
            matched.append((symptom_list[idx], score))

    matched.sort(key=lambda x: x[1], reverse=True)
    matched = matched[:top_n]

    result = []
    for symptom, score in matched:
        result.append({
            "symptom": symptom,
            "remedy": remedies_dict[symptom],
            "confidence": round(score * 100, 1)
        })

    # Fallback if no result meets threshold
    if not result:
        top_idx = int(np.argmax(scores))
        result.append({
            "symptom": symptom_list[top_idx],
            "remedy": remedies_dict[symptom_list[top_idx]],
            "confidence": round(scores[top_idx] * 100, 1),
            "note": "Closest match found. Please rephrase if this isn't accurate."
        })

    return result
