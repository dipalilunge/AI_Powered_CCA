SUMMARY_PROMPT_TEMPLATE = """
You are an assistant that summarizes work journals. 
Read the following content and return a brief 10 lines summary:

{text}
"""

GOAL_PROMPT_TEMPLATE = """
You are an AI productivity coach. Given this work journal:
\"\"\"
{content}
\"\"\"
Generate 3 SMART goals for tomorrow based on today’s progress.
"""

MCQ_PROMPT_TEMPLATE = """
You are an AI tutor. Based on this journal:
\"\"\"
{content}
\"\"\"
Generate 2–3 MCQs to help recall key points.

Format:
Q1. <question> /n
A. Option 1 /n
B. Option 2 /n
C. Option 3 /n
D. Option 4 /n
Answer: <correct option>
"""
