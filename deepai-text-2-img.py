import requests
import os
from dotenv import load_dotenv
load_dotenv()

deepai_api_key = os.getenv("DEEPAI_API_KEY")

def text_to_image(prompt: str):
    response = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': prompt,
        },
        headers={'api-key': deepai_api_key})
    print(response.json())


def main():
    prompt = 'While traveling through a dense forest, you stumble upon an ancient, overgrown path veering off from the main trail. Do you dare to explore its mysteries?'
    image_url = text_to_image(prompt)


if __name__ == '__main__':
    main()
