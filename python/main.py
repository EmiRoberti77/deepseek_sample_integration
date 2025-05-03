from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError
load_dotenv()
import os
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

print(API_KEY)
print(API_BASE_URL)

try:
  client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)
  response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
      {"role":"system", "content":"you are a helpful assistant"},
      {"role":"user", "content":"hello"}
    ],
    stream=False
  )
except AuthenticationError as auth_e:
  print(auth_e)
except APIError as api_e:
  print(api_e)
except Exception as e:
  print(e)


print(response.choices[0].message.content)