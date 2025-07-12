from flask import Blueprint, render_template, request
from youtube.youtube_fetcher import fetch_youtube_videos

video_bp = Blueprint('video', __name__)

@video_bp.route('/yoga', methods=['GET', 'POST'])
def yoga_page():
    videos = []
    query = ""
    if request.method == 'POST':
        query = request.form.get('search_query', '')
        if query:
            videos = fetch_youtube_videos(query)
    return render_template('yoga.html', videos=videos, query=query)
