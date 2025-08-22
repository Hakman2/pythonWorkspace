import os
# pip install openai
from openai import OpenAI

api_key1 = "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"
api_key2 = "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"
api_key3 = "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"

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key1,
)
# model parameters
system_prompt = "You are an expert Economics tutor. Answer all questions with clear explanations and real-world examples."
query = "Explain the law of demand with an example."
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