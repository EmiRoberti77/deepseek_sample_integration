from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL = "deepseek-chat"

client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)
messages=[{"role":"user","content":"what is the highest mountain in the world?"}]
response = client.chat.completions.create(
  model=MODEL,
  messages=messages
)
message = response.choices[0].message
content = response.choices[0].message.content
print(content)
messages.append(message)
messages.append({"role":"user", "content":"what is the second"})
response = client.chat.completions.create(
  model=MODEL,
  messages=messages
)
message = response.choices[0].message
content = response.choices[0].message.content
print(content)
messages.append(message)
