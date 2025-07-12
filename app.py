# app.py

from flask import Flask
from routes.ml import ml_bp  # Your ML (quiz/predict) blueprint
from routes.main import main_bp
from routes.chatbot import chatbot_bp
from routes.video_routes import video_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(video_bp)

    # Set a secret key for session management (you can generate a more secure one later)
    app.secret_key = "supersecretkey"
    app.register_blueprint(main_bp)
    # Register Blueprints
    app.register_blueprint(ml_bp)
    app.register_blueprint(chatbot_bp)

    # Add more blueprints here (auth, chatbot, routine) when ready
    # from routes.auth import auth_bp
    # app.register_blueprint(auth_bp)

    # Root route (home)
    @app.route('/')
    def home():
        return '<h1>🧘 Welcome to Ayurvedaparamarsh</h1><p><a href="/quiz">Start Dosha Consultation</a></p>'

    return app

# Run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
