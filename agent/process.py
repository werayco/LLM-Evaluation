from agentictools import memory, tools
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
import os
import warnings
from RAG.process import vectorstorecreator
from langchain_google_genai import ChatGoogleGenerativeAI
from pymongo import MongoClient

warnings.filterwarnings("ignore")

client = MongoClient(os.getenv("MONGO"))
db = client["responses"]
collection = db["mdresponses"]

load_dotenv()

def run_agent(user_input, usersname, sessionID=89):
    agent_memory = memory.Memory(sessionID).getMemory()
    agent_tools = tools.agentools.toolsMerged()

    groq_chat = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

    agent = initialize_agent(
        agent_tools,
        groq_chat,
        agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
        memory=agent_memory,
        verbose=True,
        max_iterations=5,
        early_stopping_method="generate",
        agent_kwargs={
            "system_message": (
                "Your name is Vera,"
                "You are a helpful assistant who help users with questions "
                "For questions about people named Ray, Ayodeji, Ryan, Tony, or Tola, "
                "you MUST use the RAG_Document_Search tool first before answering. "
                "Never say you don't have information without checking the RAG tool first."
                f"The user you are speaking with is {usersname}. Occasionally, mention their name to make the conversation more personal and professional. "
                "If a user wants to book an appointment or place an order, always ask for their user_id, item_id, and quantity before proceeding. After the order is being successful, just tell the user that the order has been made. thats all"
            )
        },
    )
    response = agent.run(input=user_input)
    collection.insert_one({"user's_query":user_input, "model's_response":response}) # using the response for monitoring
    return response
