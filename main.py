# -*- coding: utf-8 -*-
"""Main.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hn9Gk3ZkvvteZKy8QA-GQFpQp1KFfLW-
"""

import requests

# LinkedIn API credentials
CLIENT_ID = '776qzr0qhmlt23'
CLIENT_SECRET = 'bNX1V477dRwkDEfq'
ACCESS_TOKEN = 'access_token'  # Obtained after authentication


def get_new_connections():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    # request to LinkedIn's API to retrieve new connections

    api_url = 'https://api.linkedin.com/v2/network/connections'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        new_connections = response.json().get('connections', [])
        return new_connections
    else:
        print("Failed to fetch new connections")
        return []


def analyze_profiles(connections):
    for connection in connections:
        profile_id = connection.get('id')
        # Fetch profile details using LinkedIn API
        profile_data = fetch_profile_data(profile_id)
        # Extract and analyze relevant profile information (about section, job description, posts, etc.)


# Function to fetch profile data
def fetch_profile_data(profile_id):
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }

    api_url = f'https://api.linkedin.com/v2/people/{profile_id}'
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        profile_data = response.json()
        return profile_data
    else:
        print(f"Failed to fetch profile data for profile ID: {profile_id}")
        return {}


def generate_personalized_messages(profile_info):
    personalized_messages = []
    for info in profile_info:
        # Generate personalized messages based on the analyzed profile information
        message = f"Hi, I noticed your recent post about {info['recent_posts']}. Let's connect!"
        personalized_messages.append(message)
    return personalized_messages

def send_connection_requests(connections, messages):
    for connection, message in zip(connections, messages):
        profile_id = connection.get('id')
        headers = {
            'Authorization': f'Bearer {ACCESS_TOKEN}',
            'Content-Type': 'application/json'
        }

        api_url = f'https://api.linkedin.com/v2/people/{profile_id}/relation-to-viewer'
        payload = {
            'message': message
        }
        response = requests.post(api_url, headers=headers, json=payload)

        if response.status_code == 201:
            print(f"Connection request sent successfully to profile ID: {profile_id}")
        else:
            print(f"Failed to send connection request to profile ID: {profile_id}")

# Main execution
if __name__ == "__main__":

    new_connections = get_new_connections()
    analyze_profiles(new_connections)
    profile_info = []  # Placeholder for analyzed profile information
    personalized_messages = generate_personalized_messages(profile_info)
    send_connection_requests(new_connections, personalized_messages)