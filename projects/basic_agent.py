import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

# Load your OpenAI API key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create the assistant agent
assistant = AssistantAgent(
    name="CodeHelper",
    llm_config={
        "config_list": [
            {
                "model": "gpt-3.5-turbo",
                "api_key": api_key
            }
        ]
    }
)

# Create the user proxy agent (acts as the initiator)
user = UserProxyAgent(
    name="User",
    human_input_mode="NEVER"
)

# Start the conversation
user.initiate_chat(
    recipient=assistant,
    message="Write a Python function to check if a number is prime."
)
