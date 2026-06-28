# Few-Shot + Structured Output Prompting

# This combines:
# 1. Few-Shot Prompting
# 2. Structured Output Prompting

# The examples teach the model the pattern.
# The JSON structure controls the output format.

# This is one of the most common techniques used
# in production GenAI applications.

import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
Always return a valid JSON object.
Output Format:
    {
        "technology": "",
        "category": "",
        "use_case": ""
    }

Examples:
Q: Python
A:
    {
        "technology": "Python",
        "category": "Programming Language",
        "use_case": "Web Development, Data Science, Scripting, Automation"
    }

Q: PostgreSQL
A:
    {
        "technology": "PostgreSQL",
        "category": "Database",
        "use_case": "Data Storage, Data Analysis, Web Applications"
    }

Q: MongoDB
A:
    {
        "technology": "MongoDB",
        "category": "Database",
        "use_case": "Data Storage, Real-time Analytics, Content Management"
    }

Q: Redis
A:
    {
        "technology": "Redis",
        "category": "In-Memory Data Structure Store",
        "use_case": "Caching, Session Storage, Message Broker"
    }
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    response_format={"type": "json_object"},
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "Kafka"
        }
    ]
)

raw_output = response.choices[0].message.content
print("Raw model output:\n", raw_output)
 
parsed = json.loads(raw_output)
print("\nParsed dict:\n", parsed)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Response:

# Raw model output:
#  {
#     "technology": "Kafka",
#     "category": "Distributed Event Streaming Platform",
#     "use_case": "Real-time Data Pipelines, Streaming Analytics, Event-Driven Architectures"
# }

# Parsed dict:
#   {
#       'technology': 'Kafka', 
#       'category': 'Distributed Event Streaming Platform', 
#       'use_case': 'Real-time Data Pipelines, Streaming Analytics, Event-Driven Architectures'
#   }