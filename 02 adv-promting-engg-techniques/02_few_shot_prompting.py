# Few-Shot Prompting

# Few-Shot Prompting is a technique where we provide the model with a few examples (input-output pairs) before asking it to perform a similar task.
# The model learns the pattern from the examples and applies it to the new input.

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are a conventional-commit classifier. Given a git commit message,
reply with exactly one label: feat, fix, docs, refactor, chore, or test.
Reply with only the label, nothing else.
"""

# Few-shot examples are passed as prior turns in the conversation
messages = [
    {"role": "system", "content": SYSTEM_PROMPT},
    {"role": "user", "content": "Added dark mode toggle to settings page"},
    {"role": "assistant", "content": "feat"},
    {"role": "user", "content": "Fixed null pointer exception in payment handler"},
    {"role": "assistant", "content": "fix"},
    {"role": "user", "content": "Updated README with installation instructions"},
    {"role": "assistant", "content": "docs"},
    {"role": "user", "content": "Added missing test cases for the auth middleware"},
    {"role": "assistant", "content": "test"},
    # Actual question
    # {"role": "user", "content": "Renamed getUserData to fetchUserProfile for clarity, no behavior change"},
    {"role": "user", "content": "Added unit tests for the new payment gateway integration"},
]


response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages= messages
)

print(response.choices[0].message.content)

# User: Renamed getUserData to fetchUserProfile for clarity, no behavior change
# Assistant: refactor

# User: Added unit tests for the new payment gateway integration
# Assistant: test