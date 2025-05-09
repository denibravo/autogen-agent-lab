import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# The coder (writes code based on instructions)
coder = AssistantAgent(
    name="Coder",
    llm_config={
        "config_list": [
            {
                "model": "gpt-3.5-turbo",
                "api_key": api_key
            }
        ]
    }
)

# The user agent (acting as the 'researcher' giving a task)
researcher = UserProxyAgent(
    name="Researcher",
    human_input_mode="NEVER",
    code_execution_config={"use_docker": False}
)

# Start a conversation: researcher gives coder a task
researcher.initiate_chat(
    recipient=coder,
    message="We need a Python function that takes a sentence and counts how many times each word appears. Can you write that?"
)
