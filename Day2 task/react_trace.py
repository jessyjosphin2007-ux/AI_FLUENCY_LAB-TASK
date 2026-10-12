
"""Day 2, Part D: print the agent's real ReAct trace."""

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Day1'))
)

from agent import agent


QUESTION = (
    "A student has a budget of Rs. 30,000. "
    "CS101 costs Rs. 12,000, AI202 costs Rs. 18,000, "
    "and DS303 costs Rs. 15,000. "
    "Which two courses can the student take together within the budget?"
)


print("QUESTION:", QUESTION, "\n")

print("--- the agent's actions and observations ---")

answer = agent(QUESTION, max_steps=8)

print("\nFINAL ANSWER:", answer)