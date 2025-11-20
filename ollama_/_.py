from ollama import chat
from ollama import ChatResponse

MODEL = "gemma3:4b"

question = input(">> ")

response: ChatResponse = chat(model=MODEL, messages=[
  {
    'role': 'user',
    'content': question,
  },
])

print(MODEL+":", response['message']['content'])
