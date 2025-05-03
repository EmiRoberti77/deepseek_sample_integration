from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_BASE_URL = os.getenv("API_BASE_URL")
MODEL = "deepseek-reasoner"

client = OpenAI(api_key=API_KEY, base_url=API_BASE_URL)

#round 1
messages=[{
  "role":"user", "content":"what number is greater 8.10 or 9.2?"
}]
response = client.chat.completions.create(
  model=MODEL,
  messages=messages
)
reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content
print("= = = = = = ROUND 1 = = = = = = = = ")
print(reasoning_content)
print("= = = = = = = = = = = = = = ")
print(content)
#round 2
messages.append({"role":"assistant","content":content})
messages.append({"role":"user","content":"how many Rs in 'Strawberry'"})
response = client.chat.completions.create(
  model=MODEL,
  messages=messages
)
reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content
print("= = = = = = ROUND 2 = = = = = = = = ")
print(reasoning_content)
print("= = = = = = = = = = = = = = ")
print(content)
