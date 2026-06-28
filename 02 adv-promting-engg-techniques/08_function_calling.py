# Function Calling

# Function Calling allows the model to decide when a tool/function should be used.

import json
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_database_info",
            "description": "Get information about a database technology",
            "parameters": {
                "type": "object",
                "properties": {
                    "database_name": {
                        "type": "string"
                    }
                },
                "required": ["database_name"]
            }
        }
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "user",
            "content": "Tell me about PostgreSQL."
        }
    ],
    tools=tools
)

message = response.choices[0].message

print(message)

# The model may return:
#
# {
#   "tool_calls": [
#     {
#       "function": {
#         "name": "get_database_info",
#         "arguments": {
#           "database_name": "PostgreSQL"
#         }
#       }
#     }
#   ]
# }


ChatCompletionMessage(
    content=None, 
    refusal=None, 
    role='assistant', 
    annotations=None, 
    audio=None, 
    function_call=None, 
    tool_calls=[
        ChatCompletionMessageFunctionToolCall(
            id='function-call-8344191144623080174', 
            function=Function(
                arguments='{"database_name":"PostgreSQL"}', 
                name='get_database_info'
            ), 
            type='function'
        )
    ]
)