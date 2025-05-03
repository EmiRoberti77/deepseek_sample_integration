from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL = "deepseek-reasoner"
_EMPTY = ""

client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)

#round 1
messages=[{
  "role":"user", "content":"what number is greater 8.10 or 9.2?"
}]
response = client.chat.completions.create(
  model=MODEL,
  messages=messages,
  stream=True
)
reasoning_content = _EMPTY
content = _EMPTY
for chunks in response:
  if chunks.choices[0].delta.reasoning_content:
    reasoning_content = chunks.choices[0].delta.reasoning_content
    print(reasoning_content, end="", flush=True)
  else:
    content = chunks.choices[0].delta.content
    print(content, end="", flush=True)