import requests
from PIL import Image
from random import randrange
import json
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_org_id = os.getenv("OPENAI_ORG_ID")
openai_api_base = "https://api.openai.com/v1"
openai_api_image_generation = "https://api.openai.com/v1/images/generations"

azure_openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
use_azure = False

def text_to_image(api_key: str, api_url: str, prompt: str):
   authorization = f"Bearer {api_key}"
   headers = {'Content-type': 'application/json', 'Authorization': authorization}
   data = {'prompt': prompt, 'n':1, 'size': "1024x1024", 'response_format': 'url'}
   response = requests.post(api_url, data=json.dumps(data), headers=headers)
   return response.json()['data'][0]['url']

def create_image_from_prompt(prompt: str, imagesize: str ="256x256", num_images: int = 1):
   if use_azure:            
      openai.api_type = "azure"        
      openai.api_version = "2023-05-15" 
      openai.api_key = azure_openai_api_key
      openai.api_base = azure_openai_api_base
   else:
      openai.api_type = "openai"        
      openai.api_version = '2020-11-07'
      openai.api_key = openai_api_key
      openai.api_base = openai_api_base
      if openai_org_id: 
         openai.organization = openai_org_id
   
   response = openai.Image.create(
                    prompt=prompt,
                    n=num_images,
                    size=imagesize)
   image_urls = [data['url'] for data in response['data']]
   return image_urls

def main():
   prompt = 'While traveling through a dense forest, you stumble upon an ancient, overgrown path veering off from the main trail. Do you dare to explore its mysteries?'
   output = text_to_image(openai_api_key,openai_api_image_generation, prompt)
   
   image_paths = write_image([output])
   for image_path in image_paths:
      image = Image.open(image_path)
      image.show()
   image_urls = create_image_from_prompt(prompt, num_images=2)
   image_paths = write_image(image_urls)
   for image_path in image_paths:
      image = Image.open(image_path)
      image.show()



def write_image(image_urls):
   image_dir = os.path.join(os.curdir, 'images')
   if not os.path.isdir(image_dir):
      os.mkdir(image_dir)
   for image_url in image_urls:
      generated_image = requests.get(image_url).content
      random_num = randrange(10000)
      generated_image_file = f'generated_image_{random_num}.png'
      image_path = os.path.join(image_dir, generated_image_file)
      with open(image_path, "wb") as image_file:
         image_file.write(generated_image)
         yield image_path


if __name__ == '__main__':
    main()
