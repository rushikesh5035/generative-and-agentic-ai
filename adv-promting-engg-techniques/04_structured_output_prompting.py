# Structured Output Prompting

# Structured Output Prompting is used when we want
# the model to return data in a predictable format.

# Common Formats:
# - JSON
# - XML
# - YAML
# - CSV

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


SYSTEM_PROMPT = """
You are a classification assistant.

Always return a valid JSON object.

Output Format:
    {
        "technology": "string",
        "category": "string"
    }
"""


response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    response_format={"type": "json_object"},
    temperature=0, # this is important to make sure the model is deterministic and always returns the same output for the same input
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "React"
        }
    ]
)
 
print(response.choices[0].message.content)

# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Response:
# {
#     "technology": "React",
#     "category": "JavaScript Library"
# }
