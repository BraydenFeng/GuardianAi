from dotenv import load_dotenv
import os
import requests
import subprocess
from datetime import datetime

load_dotenv()
discord_token = os.getenv('discord_token')
discord_url = "https://discord.com/api/v10/users/@me/channels"
username = os.getenv('username')

def get_dms():
    header = {
        "Authorization": discord_token
    }
    response = requests.get(discord_url, headers=header)
    response_data = response.json()
    return response_data

def process_dms(length=10):
    dms = get_dms()[:length]
    dm_ids = []
    for dm in dms:
        if dm['type'] == 1:
            dm_ids.append(dm['id'])
    return dm_ids

def export_dms():
    channel_ids = process_dms()
    messages_list = []
    header = {
        "Authorization": discord_token
    }
    for channel_id in channel_ids:
        message_url = f"https://discord.com/api/v10/channels/{channel_id}/messages"
        response = requests.get(message_url, headers=header)
        messages_list.append(response.json())
    return messages_list

def clean_dms():
    cleaned_messages = []
    messages_list = export_dms()
    for messages in messages_list:
        for message in messages:
            cleaned_messages.append({message['author']['username']: message['content']})
    return cleaned_messages

print(export_dms())