import time
import datetime
from langchain_ollama import OllamaLLM
from agentictools import memory, tools
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings("ignore")
from RAG.process import vectorstorecreator
load_dotenv()

def run_agent(user_input, sessionID):
    agent_memory = memory.Memory(sessionID).getMemory()
    agent_tools = tools.agentools.toolsMerged()

    groq_chat = OllamaLLM(model="gemma3:1b", temperature=0)

    agent = initialize_agent(
            agent_tools,
            groq_chat,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION, # or CHAT_OPENAI_FUNCTIONS if needed
            memory=agent_memory,
            verbose=True,
        )

    response = agent.run(input=user_input)
    return response

    # vectorstorecreator(r"./sample.pdf") # run this once to create the vector store
print(run_agent(user_input="how are you?", sessionID=89))