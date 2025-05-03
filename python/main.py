from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
import os
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

print(API_KEY)
print(API_BASE_URL)

client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)
response = client.chat.completions.create(
  model="deepseek-chat",
  messages=[
    {"role":"system", "content":"you are a helpful assistant"},
    {"role":"user", "content":"hello"}
  ],
  stream=False
)

print(response.choices[0].message.content)