# Advanced Prompting Engineering Techniques

## 1. Zero-Shot Prompting

Zero-shot prompting asks the model to complete a task without providing any examples. The model relies solely on its pre-trained knowledge and the instruction you give.

#### When to use it?

- When the task is straightforward and self-explanatory
- When you expect the model has sufficient knowledge to solve it
- For quick, one-off requests

#### Simple Example

```
User: "Explain Docker in simple terms."
Expected: The model explains Docker using basic concepts.
```

## 2. Few-Shot Prompting

Few-shot prompting provides the model with 2-5 examples of input-output pairs before asking the actual question. This helps the model understand the pattern and style you want.

#### When to use it?

- When you need the model to follow a specific format or pattern
- For classification or labeling tasks
- When style matters (formal, casual, technical, etc.)

#### Simple Example

```
Example 1:
  Input: "Added dark mode to settings"
  Output: "feat"

Example 2:
  Input: "Fixed login bug"
  Output: "fix"

Now classify: "Updated README with API docs"
Expected: "docs"
```

## 3. Persona Prompting

Persona prompting tells the model to adopt a specific role or character. The model then responds from that perspective with expertise and tone appropriate to that role.

#### When to use it?

- When you want answers from a specific expertise level
- For different tones (professional, casual, expert, beginner)
- When domain knowledge matters

#### Simple Example

```
System: "You are a senior backend engineer with 15 years of experience."
User: "Should we use Redis or PostgreSQL for session storage?"
Expected: Expert technical recommendation with trade-offs.
```

## 4. Structured Output Prompting

Structured output prompting tells the model to return data in a specific format (JSON, XML, CSV) instead of free-form text.

#### When to use it?

- When your code needs to parse the response
- For APIs and automation
- When consistency is critical

#### Simple Example

```
System: "Always return valid JSON with fields: technology, category"
User: "React"
Expected Output:
{
  "technology": "React",
  "category": "JavaScript Library"
}
```

## 5. Few-Shot + Structured Output Prompting

This combines techniques #2 and #4: you provide examples in your desired output format, and the model learns both the pattern AND the structure.

#### When to use it?

- For production applications needing both learning and parsing
- When you need consistent structured responses
- For complex classification or extraction tasks

#### Simple Example

```
Examples:
  Q: "Python"
  A: {"technology": "Python", "category": "Language", "use_case": "Web, Data Science"}

  Q: "PostgreSQL"
  A: {"technology": "PostgreSQL", "category": "Database", "use_case": "Web Apps, Analytics"}

Now answer for: "Kafka"
Expected: Properly formatted JSON following the pattern.
```

## 6. Chain of Thought Prompting

Chain of thought prompting asks the model to "think out loud" by breaking down its reasoning into steps before giving the final answer.

#### When to use it?

- For complex problem-solving
- For decisions involving trade-offs
- For architecture or design questions
- When explaining reasoning matters

#### Simple Example

```
User: "Should I use PostgreSQL or MongoDB for a SaaS app with 100k users?"

Expected:
1. Analyze the requirements
2. List possible options
3. Discuss trade-offs
4. Give final recommendation
```

## 7. Prompt Chaining

Prompt chaining breaks one complex task into multiple smaller tasks. The output of one prompt becomes the input to the next prompt.

#### When to use it?

- For multi-step tasks
- When a single prompt is too complex
- For tasks requiring intermediate reviews

#### Simple Example

```
Step 1: Create a plan
  Input: "Build a function to find top 3 active users"
  Output: Implementation plan (step-by-step)

Step 2: Generate code
  Input: The plan from Step 1
  Output: Actual working code
```

## 8. ReAct Prompting

ReAct = Reason + Act + Observe. The model thinks about what it needs, takes an action, observes the result, and then decides what to do next. This is the foundation of AI agents.

#### When to use it?

- For agent-based workflows
- When the model needs to make decisions
- For debugging and investigation tasks

#### Simple Example

```
Thought: "The API is slow. What could be the cause?"
Action: "Check the database query patterns"
Observation: "Found N+1 query problem"
Final Answer: "Optimize the queries to batch load related data"
```

## 9. Function Calling

Function calling allows the model to request that a specific function or tool be executed. The model decides when and how to use external tools to get information.

#### When to use it?

- When the answer requires external data (APIs, databases)
- For tool-augmented workflows
- When the model needs real-time information

#### Simple Example

```
User: "Tell me about PostgreSQL"
Model decides: "I should call get_database_info('PostgreSQL')"
Model returns: {
  "tool_calls": [
    {
      "function": "get_database_info",
      "arguments": {"database_name": "PostgreSQL"}
    }
  ]
}
```

## 10. RAG Prompting (Retrieval-Augmented Generation)

RAG provides the model with relevant context retrieved from your knowledge base, and asks it to answer using ONLY that context. The model should not use outside knowledge.

#### When to use it?

- For company-specific information
- To ground answers in specific documents
- To prevent hallucinations with external sources

#### Simple Example

```
Context: "PostgreSQL supports ACID transactions, JSONB, and indexing."
User: "Does PostgreSQL support transactions?"
Expected: "Yes, PostgreSQL supports transactions. It is ACID compliant."
```

## Quick Comparison Table

| Technique             | Input                      | Output            | Best For               |
| --------------------- | -------------------------- | ----------------- | ---------------------- |
| Zero-Shot             | Task only                  | Free text         | Simple, clear requests |
| Few-Shot              | Task + examples            | Free text         | Pattern learning       |
| Persona               | Task + role                | Free text         | Domain expertise       |
| Structured            | Task + format              | JSON/XML/CSV      | Automation             |
| Few-Shot + Structured | Task + examples + format   | JSON/XML/CSV      | Production apps        |
| Chain of Thought      | Task + reasoning steps     | Free text         | Complex decisions      |
| Prompt Chaining       | Task → Task → Task         | Varies            | Multi-step workflows   |
| ReAct                 | Task + reasoning framework | Step-by-step      | Agent workflows        |
| Function Calling      | Task + available functions | Function requests | Tool usage             |
| RAG                   | Task + retrieved context   | Grounded answers  | Knowledge bases        |

---

## When To Use Each Technique

- **Zero-Shot**: General questions, quick answers
- **Few-Shot**: Classification, formatting, patterns
- **Persona**: Specialized advice, different perspectives
- **Structured Output**: APIs, automation, data pipelines
- **Few-Shot + Structured**: Production extraction tasks
- **Chain of Thought**: Analysis, decisions, explanations
- **Prompt Chaining**: Complex workflows, multi-step tasks
- **ReAct**: Agent systems, investigation tasks
- **Function Calling**: Real-time data, external APIs
- **RAG**: Company knowledge, document Q&A
