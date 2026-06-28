# Chain of Thought Prompting

# Chain of Thought (CoT) Prompting encourages the model to reason through a problem step-by-step before arriving at a final answer.

# Common Use Cases:
# - Problem Solving
# - Architecture Decisions
# - Debugging
# - Root Cause Analysis

from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = """
You are a Senior Software Architect.

When solving a problem:

1. Analyze the requirements.
2. Evaluate possible solutions.
3. Discuss trade-offs.
4. Provide the final recommendation.

Structure your answer as:

Analysis:
...

Options:
...

Trade-offs:
...

Final Recommendation:
...
"""

USER_PROMPT = """
I am building a SaaS application.
Should I choose PostgreSQL or MongoDB?
Expected:
- 100k users
- Complex reporting
- Transaction support
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
            "content": USER_PROMPT
        }
    ]
)

print(response.choices[0].message.content)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Response:

# Analysis:
    # The core requirements for your SaaS application are:
    # *   **100k users:** This implies a need for scalability, both in terms of handling concurrent connections and data volume.
    # *   **Complex reporting:** This suggests that you'll need to perform sophisticated queries, aggregations, and potentially join data from multiple sources. The ability to efficiently query and analyze data is paramount.
    # *   **Transaction support:** This is a critical requirement for many SaaS applications, ensuring data integrity and consistency, especially when dealing with financial transactions, user accounts, or any operation that involves multiple steps that must succeed or fail together.

# Options:
    # 1.  **PostgreSQL:** A powerful, open-source, object-relational database system with a strong reputation for reliability, feature robustness, and extensibility. It supports ACID transactions, complex SQL queries, and has a mature ecosystem.
    # 2.  **MongoDB:** A popular open-source, NoSQL document database. It stores data in flexible, JSON-like documents. It's known for its scalability, ease of development for certain use cases, and flexible schema.

# Trade-offs:
    #**Data Modeling & Schema:**
    #   **PostgreSQL:** Relational model. Requires a predefined schema. Excellent for structured data and enforcing relationships. Can become complex to manage with highly dynamic or nested data.
    #   **MongoDB:** Document model. Flexible schema. Ideal for rapidly evolving data structures, nested data, and semi-structured information. Can lead to data inconsistency if not managed carefully, and complex relationships can be harder to query efficiently.
    #**Transaction Support:**
    #   **PostgreSQL:** Full ACID compliance is a core strength. Guarantees atomicity, consistency, isolation, and durability for transactions. This is crucial for data integrity in complex operations.
    #   **MongoDB:** Supports multi-document ACID transactions since version 4.0. However, it's a relatively newer feature compared to PostgreSQL's long-standing transactional capabilities, and there can be performance implications or limitations in certain scenarios compared to single-document operations.
    # **Complex Reporting & Querying:**
    #   **PostgreSQL:** SQL is a powerful and standardized query language. Excellent for complex joins, aggregations, window functions, and analytical queries. Mature indexing strategies and query optimization tools.
    #   **MongoDB:** Query language is designed for documents. Aggregation framework is powerful but can be more complex to write and optimize for relational-style queries. Joins (using `$lookup`) are possible but can be less performant than native SQL joins for highly relational data.
    #**Scalability:**
    #   **PostgreSQL:** Scales well vertically (more powerful hardware). Horizontal scaling (sharding) is possible but often requires more complex setup and management (e.g., using extensions like Citus or third-party solutions). Read replicas are straightforward for scaling read operations.
    #   **MongoDB:** Designed for horizontal scalability from the ground up with sharding. Can distribute data and load across multiple servers more easily. Can also scale vertically.
    #**Development Speed & Flexibility:**
    #   **PostgreSQL:** Schema-first development can sometimes slow down initial iteration if the data model is not well-defined. However, it enforces data quality early on.
    #   **MongoDB:** Schema-less nature can accelerate initial development, especially for prototypes or applications with rapidly changing data requirements. However, it shifts the burden of schema enforcement to the application layer.
    #**Maturity & Ecosystem:**
    #   **PostgreSQL:** Extremely mature, vast community support, extensive tooling, and a wide range of extensions.
    #   **MongoDB:** Also mature and has a large community, but its ecosystem for advanced analytics and reporting tools might be less extensive than PostgreSQL's in certain areas.

# Final Recommendation:
# Given your requirements for **transaction support** and **complex reporting**, **PostgreSQL** is the more suitable choice.
# Here's why:
    # 1.**Transaction Support:** PostgreSQL's ACID compliance is a fundamental strength and has been a cornerstone of its design for decades. This is critical for ensuring data integrity in your SaaS application, especially if you handle financial transactions or any operations where data consistency is paramount. While MongoDB now offers multi-document transactions, PostgreSQL's implementation is more mature and deeply integrated.

    # 2.**Complex Reporting:** SQL, the language of PostgreSQL, is exceptionally well-suited for complex analytical queries, joins, aggregations, and reporting. The relational model naturally lends itself to structured data analysis, and PostgreSQL's query optimizer is highly sophisticated. Building complex reports that involve joining data from different entities will be more straightforward and performant in PostgreSQL.

    # 3.**Scalability for 100k Users:** While MongoDB is often lauded for its horizontal scalability, PostgreSQL can effectively handle 100k users. You can achieve this through:
    #     *   **Vertical Scaling:** Upgrading your server resources.
    #     *   **Read Replicas:** Distributing read traffic.
    #     *   **Sharding:** For very large datasets or extremely high write loads, you can implement sharding. Solutions like Citus Data (now part of Microsoft) integrate seamlessly with PostgreSQL to provide distributed capabilities.

# While MongoDB excels in scenarios with highly flexible schemas, rapid iteration on data models, and where the primary access patterns are document-centric, your stated need for robust transaction support and complex reporting strongly points towards the strengths of a relational database like PostgreSQL. You can always leverage JSONB data types within PostgreSQL if you have specific needs for semi-structured data within your relational model.