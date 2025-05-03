from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIError
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")

print(API_KEY)
print(API_BASE_URL)

try:
  client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)
  stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
      {"role":"system", "content":"you are a helpful assistant"},
      {"role":"user", "content":"explain quantum computing in simple terms"}
    ],
    temperature=0.7,
    max_tokens=1000,
    stream=True
  )

  for chunk in stream:
    if chunk.choices[0].delta.content:
      print(chunk.choices[0].delta.content, end="", flush=True)

except AuthenticationError as auth_e:
  print(auth_e)
except APIError as api_e:
  print(api_e)
except Exception as e:
  print(e)