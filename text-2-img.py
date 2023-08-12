import requests
import os
from dotenv import load_dotenv
load_dotenv()

deepai_api_key = os.getenv("DEEPAI_API_KEY")

response = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'While traveling through a dense forest, you stumble upon an ancient, overgrown path veering off from the main trail. Do you dare to explore its mysteries?',
    },
    headers={'api-key': deepai_api_key}
)
print(response.json())
