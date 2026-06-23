# Prompt Chaining

# Prompt chaining breaks a complex task into smaller sub-tasks, where the output of one LLM call becomes the input to the next. This is more reliable than asking the model to do everything in a single giant prompt.


from openai import OpenAI

client = OpenAI(
    api_key= "YOUR_GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

FEATURE_REQUEST = """
Build a function that takes a list of user objects (each with `username`
and `login_count` fields) and returns the top 3 most active users based on
login_count, breaking ties alphabetically by username.
"""

# Step 1: Turn the feature request into an implementation plan (no code yet)
plan_response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "system",
            "content": "You are a software architect. Given a feature request, "
                        "write a clear, numbered, step-by-step implementation plan. "
                        "Do not write any code, just the plan."
        },
        {"role": "user", "content": FEATURE_REQUEST}
    ]
)
plan = plan_response.choices[0].message.content
print("Step 1 - Implementation plan:\n", plan)

# Step 2: Use the plan (not the original request) to generate the actual code
code_response = client.chat.completions.create(
    model="gemini-2.5-flash-lite",
    messages=[
        {
            "role": "system",
            "content": "You are a software engineer. Given an implementation plan, "
                        "write the actual Python function implementing it. "
                        "Only output the code in a single code block, no explanation."
        },
        {"role": "user", "content": plan}
    ]
)
code = code_response.choices[0].message.content
print("\nStep 2 - Generated code:\n", code)


# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------

# Step 1 - Implementation plan:
#   Here is a step-by-step implementation plan for the function to find the top 3 most active users:
#   1.  **Define the function signature:** Create a function, let's call it `get_top_3_active_users`, that accepts one     argument: `user_list`. This argument will be a list of user objects.
#   2.  **Handle empty or insufficient input:** Check if the input `user_list` is empty or contains fewer than 3 users. If it's empty, return an empty list. If it has fewer than 3 users, proceed to sort and return all available users.
#   3.  **Sort the user list:** Sort the `user_list` based on two criteria:
#     *   **Primary sorting key:** Descending order of `login_count`.
#     *   **Secondary sorting key:** Ascending alphabetical order of `username` (to break ties).
#   4.  **Select the top 3 users:** After sorting, take the first 3 elements from the sorted `user_list`.
#   5.  **Return the result:** Return the list containing the top 3 users.

# Step 2 - Generated code:
#  ```python
# def get_top_3_active_users(user_list):
#     """
#     Finds the top 3 most active users from a list of user objects.

#     Args:
#         user_list: A list of user objects. Each user object is expected to have
#                    'username' (str) and 'login_count' (int) attributes.

#     Returns:
#         A list containing the top 3 most active users, sorted by login_count
#         descending, then username ascending. Returns an empty list if user_list
#         is empty. Returns fewer than 3 users if the input list has fewer than 3.
#     """
#     if not user_list:
#         return []

#     # Sort by login_count descending, then username ascending
#     sorted_users = sorted(user_list, key=lambda user: (-user.login_count, user.username))

#     # Select the top 3 users
#     top_3_users = sorted_users[:3]

#     return top_3_users
# ```