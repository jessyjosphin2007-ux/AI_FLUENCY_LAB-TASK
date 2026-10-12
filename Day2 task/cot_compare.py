
"""Day 2, Part B: the same questions asked WITHOUT and WITH Chain-of-Thought."""

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day1'))
)

from config import client, MODEL, banner


QUESTIONS = [
    # 1. Multi-step calculation
    "A student wants to take CS101 and AI202. "
    "CS101 costs Rs. 12,000 and AI202 costs Rs. 18,000. "
    "The student receives a 10% scholarship on the total fee. "
    "How much does the student have to pay?",

    # 2. Budget reasoning
    "A student has a budget of Rs. 30,000. "
    "CS101 costs Rs. 12,000, AI202 costs Rs. 18,000, and DS303 costs Rs. 15,000. "
    "Which two courses can the student take together without exceeding the budget?",

    # 3. Comparison reasoning
    "CS101 costs Rs. 12,000 and DS303 costs Rs. 15,000. "
    "Which course is more expensive and by how much?",
]


DIRECT_PROMPT = (
    "You are a helpful college course assistant. "
    "Give only the final answer. Do not explain."
)


COT_PROMPT = (
    "You are a helpful college course assistant. "
    "Solve the problem step by step. "
    "Number each step and show the calculation or reasoning in that step. "
    "After the steps, write the last line exactly as: Final Answer: <answer>"
)


def ask(system_prompt, question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question},
        ],
        temperature=0,
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    banner("CHAIN-OF-THOUGHT COMPARISON")

    for number, question in enumerate(QUESTIONS, start=1):
        print("=" * 72)
        print(f"QUESTION {number}: {question}\n")

        print("--- WITHOUT CoT ---")
        print(ask(DIRECT_PROMPT, question), "\n")

        print("--- WITH CoT ---")
        print(ask(COT_PROMPT, question), "\n")