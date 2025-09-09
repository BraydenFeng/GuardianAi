from dotenv import load_dotenv
import os
import requests
import subprocess
from datetime import datetime

load_dotenv()

discord_url = "https://discord.com/api/v10/users/@me/channels"

def get_dms(discord_token, username):
    header = {
        "Authorization": discord_token
    }
    response = requests.get(discord_url, headers=header)
    response_data = response.json()
    return response_data

def process_dms(discord_token, username):
    dms = get_dms(discord_token, username)
    dm_ids = []
    for dm in dms:
        if dm['type'] == 1:
            dm_ids.append(dm['id'])
    return dm_ids

def sort_dms(discord_token, username, amount=15):
    channel_ids = process_dms(discord_token, username)
    timestamps = {}
    header = {
        "Authorization": discord_token
    }
    for channel_id in channel_ids:
        message_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        response = requests.get(message_url, headers=header)
        data = response.json()
        if data:
            last_timestamp = data[0]['timestamp']
            timestamps[last_timestamp] = channel_id
    keys = list(timestamps.keys())
    keys.sort(key=lambda x: datetime.fromisoformat(x), reverse=True)
    sorted_ids = [timestamps[key] for key in keys]
    return sorted_ids[:amount]

def export_dms(discord_token, username):
    channel_ids = sort_dms(discord_token, username)
    messages_list = []
    header = {
        "Authorization": discord_token
    }
    for channel_id in channel_ids:
        message_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        response = requests.get(message_url, headers=header)
        messages_list.append(response.json())
    return messages_list

def clean_dms(discord_token, username):
    cleaned_messages = []
    messages_list = export_dms(discord_token, username)
    for messages in messages_list:
        for message in messages:
            cleaned_messages.append({message['author']['username']: message['content']})
    return cleaned_messages

def results(discord_token, username):
    results = clean_dms(discord_token, username)
    return results