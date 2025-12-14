"""
    To be... idk something :)
    Main file that would be executed 
    or idk how I will orchestrate this tbh
"""

from openai import OpenAI

print("Hello, World!")
print("Things")

try:
    client = OpenAI()
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")

