import os
import base64
import requests
from dotenv import load_dotenv

load_dotenv()

def encode_image(image_path):
    with open(image_path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

image_base64 = encode_image('/Users/seherbal/AIHashtagGenerator/pythonProject1/post151.png')

headers = {

    'Content-Type': 'application/json',
    'Authorization': f'Bearer {os.getenv("OPENAI_KEY")}'
}

payload = {
    "model": "gpt-4o-mini",
    "messages": [
        {
            'role': 'system',
            'content': [
                {
                    'type': 'text',
                    'text': 'You are a hashtag generation model. When you get an image as input, your response should always contain exactly 30 hashtags separated by commas.'
                }
            ]
        },
        {
            'role': 'user',
            'content': [
                {
                    'type': 'text',
                    'text': 'Provide the hashtags for this image:'
                },
                {
                    'type': 'image_url',
                    'image_url': {
                        'url': f'data:image/png;base64,{image_base64}'
                    }
                }
            ]
        }
    ],
    "max_tokens": 500
}

response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
print(response.json)