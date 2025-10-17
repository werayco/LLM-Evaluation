import time
import datetime
from langchain_groq import ChatGroq
from agentictools import memory, tools
from langchain.agents import initialize_agent, AgentType


def run_agent(user_input, sessionID):
    obj = memory(sessionID)
    agent_memory = obj.getMemory()
    agent_tools = tools.agentools().toolsMerged()

    groq_chat = ChatGroq(model="openai/gpt-oss-20b", temperature=0)

    agent = initialize_agent(
        agent_tools,
        groq_chat,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=agent_memory,
        verbose=True,
    )

    response = agent.run(input=user_input)
    return response


print(run_agent("who is ray?", 89))