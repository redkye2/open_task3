import os
from openai import OpenAI
import datetime

client = OpenAI(api_key="open-api=key 넣어주세요")

def help(Prompt):
  response1 = client.chat.completions.create(
  temperature=0.5,
  model="gpt-3.5-turbo-1106",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": f"{Prompt} json"}
  ],
  response_format={"type": "json_object"}
)
  response= response1.choices[0]
  text = response.message.content
  print(datetime.datetime.now())
  return text


#print("test :", help("너는 gpt가 맞지?"))