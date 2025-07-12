import requests
from config import YOUTUBE_API_KEY

def fetch_youtube_videos(query, max_results=6):
    search_url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        'part': 'snippet',
        'q': query,
        'key': YOUTUBE_API_KEY,
        'maxResults': max_results,
        'type': 'video'
    }
    response = requests.get(search_url, params=params)
    if response.status_code == 200:
        videos = []
        for item in response.json().get('items', []):
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            description = item['snippet']['description']
            videos.append({
                'video_id': video_id,
                'title': title,
                'description': description
            })
        return videos
    return []
