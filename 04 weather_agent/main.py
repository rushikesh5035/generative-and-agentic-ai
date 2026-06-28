from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY"),
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# function to get weather info
def get_weather_info(city):
    url = f'https://wttr.in/{city.lower()}?format=%c+%t'

    response = requests.get(url)
    
    if response.status_code == 200:
        return f"The current weather in {city} is: {response.text}"
    else:  
        return f"Could not retrieve weather information for {city}. Please try again."



def main():
    user_query = input(f"👉 Please enter your weather query: ")

    response = client.responses.create(
        input=user_query,
        model="openai/gpt-oss-20b",
    )

    print(f"🤖: {response.output_text}")

# main()

print(get_weather_info("Pune"))