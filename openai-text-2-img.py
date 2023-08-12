import requests
import json
import os
import openai
from dotenv import load_dotenv
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
openai_org_id = os.getenv("OPENAI_ORG_ID")
openai_api_base = "https://api.openai.com/v1"
azure_openai_api_key = os.getenv("AZURE_OPENAI_API_KEY")
azure_openai_api_base = os.getenv("AZURE_OPENAI_ENDPOINT")
deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
use_azure = False

def text_to_image(prompt: str):
   authorization = f"Bearer {openai_api_key}"
   headers = {'Content-type': 'application/json', 'Authorization': authorization}
   url = "https://api.openai.com/v1/images/generations"
   data = {'prompt': prompt, 'n':1, 'size': "1024x1024", 'response_format': 'url'}
   response = requests.post(url, data=json.dumps(data), headers=headers)
   return response.json()['data'][0]['url']

def create_image_from_prompt(prompt: str, imagesize: str ="256x256", num_images: int = 1):
   if use_azure:            
      openai.api_type = "azure"        
      openai.api_version = "2023-05-15" 
      openai.api_base = azure_openai_api_base 
      openai.deployment_name = deployment_name  
      openai.api_key = azure_openai_api_key
   else:
      openai.api_type = "openai"        
      openai.api_version = '2020-11-07'
      openai.api_key = openai_api_key
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
   image_url = create_image_from_prompt(prompt)
   print(image_url)

if __name__ == '__main__':
    main()
