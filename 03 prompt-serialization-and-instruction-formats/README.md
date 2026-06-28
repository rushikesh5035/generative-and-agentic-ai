## Prompt Serialization & Instruction Formats

👉 **Prompt Serialization** is the format in which you structure your instructions and messages when communicating with LLMs.

Different models expect different formats. Using the wrong format can:

- ❌ Reduce model performance
- ❌ Cause parsing errors
- ❌ Waste tokens

---

### 🔥 Style 1: Alpaca Prompting

👉 Alpaca is a simple, text-based prompt format. It uses natural language markers to separate different parts of the prompt.

**Developed by:** Stanford University  
**Use Case:** Fine-tuned models, simple instruction-following tasks  
**Readability:** Very high (human-friendly)

#### Format Structure

```
### Instruction:
<SYSTEM_PROMPT>

### Input:
<USER_QUERY>

### Response:
<MODEL_OUTPUT>
```

#### Example 1: Simple Task

```
### Instruction:
Translate English to French.

### Input:
Hello, how are you?

### Response:
Bonjour, comment allez-vous?
```

#### Example 2: Chatbot Style

```
### Instruction:
You are a helpful programming assistant. Answer coding questions clearly.

### Input:
How do I reverse a string in Python?

### Response:
You can reverse a string in Python using slicing with [::-1]:
string = "hello"
reversed_string = string[::-1]  # "olleh"
```

#### When to Use Alpaca

- Simple instruction-following tasks
- Small fine-tuned models
- When readability is priority
- Legacy systems

---

### 🔥 Style 2: ChatML (Chat Markup Language) ⭐ MOST USED

👉 ChatML is a **standardized, structured format** for multi-turn conversations. It clearly separates different roles in a conversation.

**Developed by:** OpenAI  
**Use Case:** Modern LLMs, chat applications, multi-turn conversations  
**Readability:** Medium (requires understanding the structure)  
**Adoption:** Industry standard ⭐

#### Format Structure

**Text Format:**

```
<|im_start|>system
<SYSTEM_PROMPT>
<|im_end|>
<|im_start|>user
<USER_QUERY>
<|im_end|>
<|im_start|>assistant
<MODEL_RESPONSE>
<|im_end|>
```

**JSON Format (Most Common):**

```json
[
  {
    "role": "system",
    "content": "<SYSTEM_PROMPT>"
  },
  {
    "role": "user",
    "content": "<USER_QUERY>"
  },
  {
    "role": "assistant",
    "content": "<MODEL_RESPONSE>"
  }
]
```

### Key Concepts

- **role:** Can be "system", "user", or "assistant"
  - `system`: Sets context/instructions (appears once, usually first)
  - `user`: User's input/query
  - `assistant`: Model's response
- **content:** The actual text message

#### Example 1: Simple Conversation (JSON)

```json
[
  {
    "role": "system",
    "content": "You are a helpful programming assistant."
  },
  {
    "role": "user",
    "content": "How do I reverse a string in Python?"
  },
  {
    "role": "assistant",
    "content": "Use slicing with [::-1]:\nstring = 'hello'\nreversed_string = string[::-1]"
  }
]
```

#### Example 2: Multi-turn Conversation (JSON)

```json
[
  {
    "role": "system",
    "content": "You are a math tutor. Explain concepts clearly."
  },
  {
    "role": "user",
    "content": "What is a derivative?"
  },
  {
    "role": "assistant",
    "content": "A derivative is the rate of change of a function at a point."
  },
  {
    "role": "user",
    "content": "Can you give an example?"
  },
  {
    "role": "assistant",
    "content": "Sure! For f(x) = x², the derivative is f'(x) = 2x."
  }
]
```

### Example 3: Text Format (ChatML)

```
<|im_start|>system
You are a helpful code reviewer. Review code and suggest improvements.
<|im_end|>
<|im_start|>user
Review this Python function:

def add(a, b):
    return a + b
<|im_end|>
<|im_start|>assistant
Good function! Some suggestions:
1. Add type hints: def add(a: int, b: int) -> int:
2. Add docstring: """Add two numbers."""
3. Add error handling for invalid inputs
<|im_end|>
```

### Python Implementation with OpenAI API

```python
from openai import OpenAI

client = OpenAI()

messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant."
    },
    {
        "role": "user",
        "content": "What is machine learning?"
    }
]

response = client.chat.completions.create(
    model="gpt-4",
    messages=messages
)

print(response.choices[0].message.content)
```

#### When to Use ChatML

- ⭐ **ChatGPT, GPT-4, Claude, etc.**
- Multi-turn conversations
- Production applications
- Any modern LLM API

### Real-world Usage

```python
# This is how most APIs work today
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

# All major APIs use this format:
# - OpenAI (ChatGPT, GPT-4)
# - Anthropic (Claude)
# - Google (PaLM, Gemini)
# - Meta (Llama models with ChatML)
# - Mistral
```

---

### 🔥 Style 3: INST Prompting (Instruction Format)

👉 INST is a **simple token-based format** used primarily by Meta's Llama 2 models. It wraps instructions in special markers.

**Developed by:** Meta  
**Use Case:** Llama models, open-source LLMs  
**Readability:** Medium  
**Adoption:** Popular in open-source community

#### Format Structure

**Basic Format:**

```
[INST] <INSTRUCTION> [/INST]
```

**With System Prompt:**

```
[INST] <<SYS>>
<SYSTEM_PROMPT>
<</SYS>>

<INSTRUCTION>
[/INST]
```

**Full Conversation:**

```
<s>[INST] <<SYS>>
<SYSTEM_PROMPT>
<</SYS>>

<FIRST_USER_MESSAGE>
[/INST] <FIRST_ASSISTANT_RESPONSE> </s>
<s>[INST] <SECOND_USER_MESSAGE> [/INST] <SECOND_ASSISTANT_RESPONSE> </s>
```

### Key Components

- `[INST]` and `[/INST]`: Wrap the user instruction
- `<<SYS>>` and `<</SYS>>`: Wrap system prompt (optional)
- `<s>` and `</s>`: Special tokens marking start/end of sequence
- Everything between markers is the instruction

### Example 1: Simple Instruction

```
[INST] What is Python? [/INST]
```

Output:

```
Python is a high-level programming language known for its simplicity and readability.
```

### Example 2: With System Prompt

```
[INST] <<SYS>>
You are a helpful programming tutor.
<</SYS>>

Explain what a loop is.
[/INST]
```

Output:

```
A loop is a control structure that repeats a block of code. For example:
for i in range(5):
    print(i)  # Prints 0 to 4
```

### Example 3: Multi-turn Conversation

```
<s>[INST] <<SYS>>
You are a helpful assistant.
<</SYS>>

What is JavaScript?
[/INST] JavaScript is a programming language primarily used for web development. </s>
<s>[INST] Can you give me an example? [/INST] Sure!
console.log("Hello, World!");
</s>
```

#### When to Use INST

- Llama 2 models
- Open-source LLMs
- Local deployments
- Token-constrained scenarios
- Mistral and similar models

---

## 📊 Comparison Table

| Format              | Structure           | Common Model                     |
| ------------------- | ------------------- | -------------------------------- |
| **Alpaca**          | Plain Text Template | Alpaca, Instruction-Tuned Models |
| **ChatML**          | Role-Based Messages | OpenAI, Gemini, Modern APIs      |
| **Standardization** | Special Tags        | Llama 2                          |

---

# Interview Notes

### What is Prompt Serialization?

Prompt Serialization is the process of converting instructions, user inputs, and conversation history into a format that a language model can understand.

### Which Prompt Format Is Most Common Today?

ChatML is the most widely used format because it supports multi-turn conversations and clearly separates system, user, and assistant messages.

### Why Should We Learn Different Prompt Formats?

Because different LLMs expect different prompt structures. Understanding these formats helps when working with:

- OpenAI APIs
- Gemini APIs
- Llama Models
- Ollama
- HuggingFace
- Fine-Tuning Pipelines

---

# Quick Summary

## Alpaca

```text
Instruction
Input
Response
```

Simple instruction-following format.

## ChatML

```json
[{ "role": "system" }, { "role": "user" }, { "role": "assistant" }]
```

Most common format today.

## INST

```text
[INST]
Prompt
[/INST]
```

Used by Llama 2 models
