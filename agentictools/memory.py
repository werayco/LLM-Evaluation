from langchain_community.chat_message_histories import MongoDBChatMessageHistory
from langchain.memory import ConversationBufferMemory
import os

class memory:
    def __init__(self, sessionID):
        self.sessionID = sessionID
        self.conString: str = os.getenv("MONGO")
        self.databaseName: str = "memory"
        self.collection_name: str = "agentmemory"
    
    def getMemory(self):
        history = MongoDBChatMessageHistory(
            connection_string=self.conString,
            session_id=self.sessionID,
            database_name=self.databaseName,
            collection_name=self.collection_name,
        )
        memory = ConversationBufferMemory(
            chat_memory=history,
            return_messages=True,
            memory_key="chat_history",
            input_key="input",
        )
        return memory

 