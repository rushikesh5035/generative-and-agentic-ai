# ReAct Prompting

# ReAct = Reason + Act
# The model thinks about what it needs,
# performs an action, observes the result,
# and then produces the final answer.

# This is the foundation of AI Agents.

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are an AI Engineering Assistant.

Follow the ReAct format:

Thought:
What should I do?

Action:
What action should be taken?

Observation:
What information was obtained?

Final Answer:
Provide the answer.
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
            "content": """
A Node.js API is becoming slow.

Average response time:
800ms

Database:
PostgreSQL

What should I investigate first?
"""
        }
    ]
)

print(response.choices[0].message.content)


# ----------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------------

# Thought: The user is asking for the first thing to investigate to improve the performance of a slow Node.js API. The API has an average response time of 800ms and uses PostgreSQL as its database. Performance issues in web applications often stem from either the application code itself or the database. Given the response time, it's likely a bottleneck exists. I should prioritize investigating the most common culprits.

# Action:
# Identify common performance bottlenecks in Node.js APIs and PostgreSQL databases.

# Observation:
# Common performance bottlenecks in Node.js APIs include:
# 1.  **Inefficient code:** Blocking operations, excessive computations, memory leaks.
# 2.  **External service calls:** Slow third-party APIs, network latency.
# 3.  **Database interactions:** Slow queries, N+1 query problems, unindexed tables, connection pool exhaustion.
# 4.  **Resource constraints:** CPU, memory, I/O limitations on the server.

# Common performance bottlenecks in PostgreSQL databases include:
# 1.  **Slow queries:** Missing indexes, inefficient query plans, large table scans.
# 2.  **Database configuration:** Insufficient memory allocation (e.g., `shared_buffers`, `work_mem`), incorrect settings.
# 3.  **Hardware limitations:** Slow disk I/O, insufficient RAM, CPU bottlenecks.
# 4.  **Connection management:** Too many connections, inefficient connection pooling.
# 5.  **Locking and contention:** Long-running transactions blocking other operations.

# Considering the 800ms average response time and the use of PostgreSQL, database interactions are a very strong candidate for the bottleneck. Slow database queries are a frequent cause of high API response times. Therefore, investigating the database queries should be the first step.

# Final Answer:
# The first thing to investigate is the **database queries**. Specifically, look for slow-running queries, missing indexes, and inefficient query plans in your PostgreSQL database. Tools like `EXPLAIN ANALYZE` in PostgreSQL can help identify problematic queries. Additionally, check for N+1 query problems in your Node.js application code that might be making excessive database calls.