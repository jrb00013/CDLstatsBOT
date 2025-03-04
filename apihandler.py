import requests
import json

def get_ranked_stats(player_name):
    # Example URL for fetching stats (replace with actual CoD API endpoint)
    url = f"https://api.callofduty.com/stats/{player_name}/ranked"
    
    # You may need to include headers with your API key
    headers = {"Authorization": f"Bearer {api_key}"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        # Format the stats data to return as a string
        return f"Rank: {data['rank']}, Wins: {data['wins']}, Losses: {data['losses']}"
    else:
        return "Error fetching stats or player not found."

# You can store your API key here for testing or load it from config
api_key = "your-api-key-here"
