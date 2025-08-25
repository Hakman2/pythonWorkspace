import os
# pip install openai
from openai import OpenAI

api_key1 = ""
  
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key1,
)
# model parameters
system_prompt = "You are an expert Economics tutor. Answer all questions with clear explanations and real-world examples."
query = "How are you?"
temperature = 0.4
model = "google/gemini-2.5-flash"
stream = True

completion = client.chat.completions.create(
    extra_body={},
    model=model,
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": query
                }
            ]
        }
    ],
    temperature=temperature,
    # top_p=1,
    stream=stream,
)

if stream:
    llm_response = ''
    for chunk in completion:
        llm_response += chunk.choices[0].delta.content
        print(chunk.choices[0].delta.content, end="", flush=True)
else:
    print(completion.choices[0].message.content)