# routes/main.py

from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

# Home Page Route
@main_bp.route('/')
def index():
    return render_template('index.html')
@main_bp.route('/remedy/<topic>')
def remedy_page(topic):
    content = {
        'digestion': {
            'title': 'Boost Digestion',
            'description': 'Learn Ayurvedic ways to enhance your digestion using herbs like Triphala, Ginger, and Jeera.',
            'tips': [
                'Drink warm water with lemon in the morning.',
                'Use Hing, Jeera, and Ajwain in your meals.',
                'Chew fennel seeds after eating.',
                'Avoid overeating and eat mindfully.'
            ]
        },
        'antibiotic': {
            'title': 'Natural Antibiotic',
            'description': 'Discover powerful Ayurvedic herbs that act as natural antibiotics like Neem, Tulsi, and Turmeric.',
            'tips': [
                'Boil Neem leaves and drink its water weekly.',
                'Make Tulsi tea for throat infections.',
                'Use Haldi milk (turmeric latte) before bed.',
                'Inhale steam with tulsi drops during flu.'
            ]
        },
        'detox': {
            'title': 'Detox Herb',
            'description': 'Flush toxins from your system using herbs like Triphala, Aloe Vera, and Giloy.',
            'tips': [
                'Take Triphala at night with warm water.',
                'Drink Aloe Vera juice in the morning.',
                'Use Giloy kadha weekly.',
                'Eat light khichdi on detox days.'
            ]
        },
        'antioxidant': {
            'title': 'Rich in Antioxidants',
            'description': 'Protect your cells and slow aging with antioxidants from Amla, Pomegranate, and Cloves.',
            'tips': [
                'Have Amla juice or raw Amla daily.',
                'Add pomegranate to your breakfast.',
                'Use cardamom or cloves in tea.',
                'Avoid processed sugars and deep fried food.'
            ]
        },
        'immunity': {
            'title': 'Boost Immunity',
            'description': 'Strengthen your immunity with Ayurvedic herbs like Chyawanprash, Ashwagandha, and Turmeric.',
            'tips': [
                'Take 1 tsp of Chyawanprash every morning.',
                'Use turmeric and black pepper in meals.',
                'Sleep on time to restore ojas (vital energy).',
                'Practice yoga and pranayama daily.'
            ]
        }
    }

    if topic not in content:
        return "Remedy not found", 404

    return render_template('remedy.html', data=content[topic])

# Yoga / Meditation Videos Page
@main_bp.route('/videos')
def videos():
    return render_template('videos.html')

# Daily Routine Page based on Dosha
@main_bp.route('/routine/<dosha>')
def routine(dosha):
    routine_data = {
        'Vata': {
            'wake': '6:00 AM',
            'sleep': '9:30 PM',
            'food': 'Warm, moist, nourishing food. Avoid raw/cold items.',
            'avoid': 'Dry snacks, cold drinks, skipping meals',
            'tips': 'Do oil massage, light yoga, and stay warm.'
        },
        'Pitta': {
            'wake': '5:30 AM',
            'sleep': '10:00 PM',
            'food': 'Cool, mild food like cucumbers, melons, dairy.',
            'avoid': 'Spicy, oily, fried, and fermented food',
            'tips': 'Practice cooling yoga, moon gazing, meditation.'
        },
        'Kapha': {
            'wake': '5:00 AM',
            'sleep': '9:00 PM',
            'food': 'Light, warm, spicy food. Lots of veggies.',
            'avoid': 'Dairy, sweets, oily food, daytime naps',
            'tips': 'Do brisk walking, pranayama, and dry massage.'
        }
    }

    # Use get to avoid NoneType error if dosha key is invalid
    return render_template("routine.html", dosha=dosha, routine=routine_data.get(dosha))
    