from openai import OpenAI
from dotenv import load_dotenv
import os
import requests
import json
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Weather tool
def get_weather_info(city):
    url = f'https://wttr.in/{city.lower()}?format=%c+%t'
    response = requests.get(url)
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text.strip()}"
    else:  
        return f"Could not retrieve weather information for {city}."

available_tools = {"get_weather_info": get_weather_info}

class MyOutputFormat(BaseModel):
    step: str = Field(..., description= "The ID of the step, can be START, PLAN, TOOL or OUTPUT")
    content: Optional[str] = Field(None, description= "The optional string content of the step")
    tool: Optional[str] = Field(None, description= "The ID of the tool to be called")
    input: Optional[str] = Field(None, description= "The input parameter string for the tool to be called")


# SYSTEM_PROMPT = """
#     Your're an expert AI assistant in resolving user queries using chain of thought.
#     You work on START, PLAN and OUTPUT steps.
#     You need to first PLAN what needs to be done. The PLAN can be multiple steps.
#     Once you think enough PLAN has been done, finally you can give an OUTPUT.
#     Your can also call a tool if required from the list of available tools.
#     "Once you have given the OUTPUT step, do not continue. Stop after OUTPUT."

#     Rules:
#     - Strictly follow the given JSON output format.
#     - only run one step at a time.
#     - The sequence of steps is START (where user gives an input), PLAN (That can be multiple times), TOOL (if a tool is called), and finally OUTPUT (where you give the final answer).
#     for every tool call wait for observe step which is the output from the called tool.

#     Output JSON format:
#         { "step": "START" | "PLAN" | "TOOL", "content":"string", "tool": "string", "input": "string"}
    
#     Available tools:
#     - get_weather_info(city: str): takes a city name as input and returns the current weather information for that city.

#     Example 1:
#     START: What is the weather in Pune?
#     PLAN: { "step": "PLAN", "content":"Seem like user is interested in  getting weather of Pune in India" }
#     PLAN: { "step": "PLAN", "content":"Lets see if we have any available tool from the list of available tools" }
#     PLAN: { "step": "PLAN", "content":"Great, we have get_weather_info tool available for this query" }
#     PLAN: { "step": "PLAN", "content":"I need to call get_weather_info tool for Pune as input for city" }
#     TOOL: { "step": "TOOL", "tool": "get_weather_info", "input": "Pune"}
#     PLAN: { "step": "OBSERVE", "TOOL":"get_weather_info", "output": "the current weather in Pune is: Partly cloudy, 22°C" }
#     PLAN: { "step": "PLAN", "content":"Great, I got the weather information for Pune" }
#     OUTPUT: { "step": "OUTPUT", "content":"The current weather in Pune is: Partly cloudy, 22°C" }

#     Example 2:
#     START: What is the weather in Mumbai?
#     PLAN: { "step": "PLAN", "content":"Seem like user is interested in  getting weather of Mumbai in India" }
#     PLAN: { "step": "PLAN", "content":"Lets see if we have any available tool from the list of available tools" }
#     PLAN: { "step": "PLAN", "content":"Great, we have get_weather_info tool available for this query" }
#     PLAN: { "step": "PLAN", "content":"I need to call get_weather_info tool for Mumbai as input for city" }
#     TOOL: { "step": "TOOL", "tool": "get_weather_info", "input": "Mumbai"}
#     PLAN: { "step": "OBSERVE", "TOOL":"get_weather_info", "output": "the current weather in Mumbai is: Sunny, 28°C" }
#     PLAN: { "step": "PLAN", "content":"Great, I got the weather information for Mumbai" }
#     OUTPUT: { "step": "OUTPUT", "content":"The current weather in Mumbai is: Sunny, 28°C" }
# """

# ================== Improved Prompt ==================
SYSTEM_PROMPT = """
You are an expert AI assistant using chain-of-thought.
Follow this sequence strictly: START → PLAN(s) → TOOL → OBSERVE → PLAN → OUTPUT.

Rules:
- Respond with **only** valid JSON matching the schema.
- One step per response.
- After OUTPUT, stop completely.
- Do not add extra text outside the JSON.

Available tools:
- get_weather_info(city: str)
"""

message_history = [{"role": "system", "content": SYSTEM_PROMPT}]

user_query = input(f"👉 Please enter your weather query: ")

message_history.append({"role": "user", "content": user_query})

while True:
    response = client.chat.completions.parse(
        model="openai/gpt-oss-120b",
        response_format=MyOutputFormat,
        messages=message_history,
        temperature=0.1,
    )

    # raw_results = response.choices[0].message.parsed

    parsed_result = response.choices[0].message.parsed   # Pydantic object
    
    # Convert to JSON string before adding to history
    assistant_message = parsed_result.model_dump_json()
    message_history.append({"role": "assistant", "content": assistant_message})
    
    # step = parsed_result.get("step")
    step = parsed_result.step

    if step in ["START", "PLAN"]:
        print(f"🧠: {parsed_result.content}")
        continue

    elif step == "TOOL":
        tool_name = parsed_result.tool
        tool_input = parsed_result.input
        
        print(f"⛏️: {tool_name}({tool_input})")
        
        if tool_name in available_tools:
            tool_response = available_tools[tool_name](tool_input)
            print(f"⛏️: {tool_name} = {tool_response}")
            
            message_history.append({
                "role": "developer",
                "content": json.dumps({
                    "step": "OBSERVE",
                    "tool": tool_name,
                    "input": tool_input,
                    "output": tool_response
                })
            })
        continue

    elif step == "OUTPUT":
        print(f"🤖: {parsed_result.content}")
        break

        
