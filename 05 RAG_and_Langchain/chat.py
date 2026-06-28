
import os
from dotenv import load_dotenv

from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
from langchain_qdrant import QdrantVectorStore

from openai import OpenAI

load_dotenv()

# CLIENT SETUP
client = OpenAI(
    api_key=os.environ.get("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

# Embedding model
embedding_model = NVIDIAEmbeddings(
   model="nvidia/nv-embed-v1",
)

# Vector DB
vector_db = QdrantVectorStore.from_existing_collection(
    embedding=embedding_model,
    url="http://localhost:6333",
    collection_name="learning_rag"
)

# Take user input
user_query = input("Enter your query: ")

# Relevant chunks from the vector db
search_results = vector_db.similarity_search(query=user_query)

# Build context
context = "\n\n---\n\n".join([
    f"Page {result.metadata.get('page_label', 'N/A')} | Source: {result.metadata.get('source', 'N/A')}\n"
    f"{result.page_content}"
    for result in search_results
])

SYSTEM_PROMPT = f"""You are a helpful assistant. Answer the user's question based **only** on the provided context from the PDF.

If the answer is in the context, clearly mention the page number(s) so the user can refer to it.
If the answer is not in the context, say so honestly.

Context:
{context}
"""

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": user_query }
    ]
)

print("\n🤖 Response:")
print(response.choices[0].message.content)