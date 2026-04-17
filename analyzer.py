from prompts import build_prompt
# from openai import OpenAI  # or any LLM API

def analyze_code(problem, code):
    prompt = build_prompt(problem, code)

    # Mock response (replace with API call)
    response = f"""
    ✔ Time Complexity: O(n)
    ✔ Space Complexity: O(n)
    ✔ Suggestions:
    - Optimize using hashmap
    - Handle edge case: empty array
    ✔ Rating: 8/10
    """

    return response
