import time
import datetime
from langchain_groq import ChatGroq
from agentictools import memory, tools
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os
load_dotenv()


def run_agent(user_input, sessionID):
    obj = memory.memory(sessionID)
    agent_memory = obj.getMemory()
    agent_tools = tools.agentools().toolsMerged()

    groq_chat = ChatGroq(model="openai/gpt-oss-20b", temperature=0, api_key=os.getenv("GROQ"))

    agent = initialize_agent(
        agent_tools,
        groq_chat,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=agent_memory,
        verbose=True,
    )

    response = agent.run(input=user_input)
    return response


# print(run_agent("who is ryan to ray?", 89))