# RAG Prompting

# Retrieval Augmented Generation
# The model receives retrieved context
# and must answer using ONLY that context.

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

RETRIEVED_CONTEXT = """
PostgreSQL Features:
    - ACID Compliance
    - Supports Transactions
    - Supports Indexing
    - Supports JSONB
    - Open Source
"""

SYSTEM_PROMPT = """
    You are a RAG assistant.
    Rules:
        1. Answer ONLY using the provided context.
        2. Do not use outside knowledge.
        3. If the answer is not found in the context,
    reply with:
        "I don't know based on the provided context."
"""

response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    temperature=0,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""
                Context: {RETRIEVED_CONTEXT}
                Question: Does PostgreSQL support transactions?
            """
        }
    ]
)

print(response.choices[0].message.content)


#-----------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------
# Response:
# Yes, PostgreSQL supports transactions.