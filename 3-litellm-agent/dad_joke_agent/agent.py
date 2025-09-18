import os
import random

from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm

model = Litellm(
    model = "gemini-2.0-flash",
    api_key = os.getenv("GOOGLE_API_KEY"),
)

def get_dad_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
        "Why don't skeletons fight each other? They don't have the guts!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
    ]
    return random.choice(jokes)

root_agent = Agent(
    name = "dad_joke_agent",
    model = model,
    description = "Dad joke agent",
    instruction = """You are a dad joke agent. You tell dad jokes when asked.
    Only use the tool 'get_dad_joke' to get a dad joke.""",
    tools = [get_dad_joke],
)