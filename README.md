# 🧘‍♂️ Ayurveda Paramarsh

**Ayurveda Paramarsh** is a web-based Ayurvedic health consultation system powered by machine learning. It helps users identify their Dosha imbalances (Vata, Pitta, Kapha), get natural remedies, view daily routines, and explore curated yoga and meditation videos based on their symptoms.

---

## 🌿 Features

- 🔍 **Dosha Consultation**  
  Input your symptoms and receive Ayurvedic analysis using NLP and ML.

- 💊 **Personalized Remedies**  
  Get herbal, lifestyle, and dietary suggestions based on ancient Ayurvedic texts.

- 🧘 **Yoga & Meditation Recommendations**  
  Fetches YouTube videos dynamically based on user needs (stress, pain, digestion, etc.).

- 🕉️ **Daily Ayurvedic Routine Generator**  
  Suggests ideal daily habits based on your Dosha type.

- 📚 **Scriptural References**  
  Remedies are linked to traditional sources like *Charaka Samhita*, *Ashtanga Hridayam*, etc.

---

## ⚙️ Technologies Used

- **Frontend**: HTML5, CSS3, JavaScript  
- **Backend**: Python, Flask  
- **ML/NLP**: Fuzzy Matching, Cosine Similarity, Symptom Synonyms  
- **Database**: JSON / CSV-based knowledge system  
- **API**: YouTube Data API (for yoga videos)  
- **Hosting**: Render / GitHub Pages

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ayurveda-paramarsh.git
cd ayurveda-paramarsh

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python app.py
