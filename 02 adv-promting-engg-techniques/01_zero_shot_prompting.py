# Zero-Shot Prompting

# Directly giving the instruction to the model without any examples. 
# Zero-shot prompting is a technique where we ask the model to perform a task without providing any examples. The model relies entirely on its pre-trained knowledge.

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "user",
            "content": "Explain Docker in simple terms."
        }
    ]
)

print(response.choices[0].message.content)

# User: What is the capital of France? -> I am sorry, I can only answer coding related questions.

# User: How do I reverse a string in Python? -> You can reverse a string in Python using slicing. Here is an example: