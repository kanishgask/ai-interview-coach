def build_prompt(problem, code):
    return f"""
    You are a FAANG interviewer.

    Problem:
    {problem}

    Candidate Code:
    {code}

    Evaluate:
    - Time & Space Complexity
    - Bugs / Edge Cases
    - Optimization
    - Final rating out of 10
    """
