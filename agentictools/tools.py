from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
import asyncio
from langchain.text_splitter import RecursiveCharacterTextSplitter
from RAG.process import load_faiss_vector_store
from langchain.tools import Tool
from numo import Numo
from typing import List, Any
from langchain.tools import StructuredTool
import requests
from pydantic import BaseModel


class MakeOrderInput(BaseModel):
    user_id: int
    item_id: int
    quantity: int


class agentools:
    @staticmethod
    def ragtool(query, db_directory_path=r"RAG/faiss_db"):
        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )
        vector_store = FAISS.load_local(
            db_directory_path, embeddings, allow_dangerous_deserialization=True
        )
        retriever = vector_store.as_retriever()
        response = retriever.get_relevant_documents(query)
        print(f"Relevant document chunks:\n{response}\n")
        return response

    @staticmethod
    def translator(query):
        numo = Numo()
        return asyncio.run(numo.calculate(query))

    @staticmethod
    def calculator(query):
        numo = Numo()
        return asyncio.run(numo.calculate(query))

    @staticmethod
    def makeOrder(data: list):
        user_id, order_id, quantity = data[0], data[1], data[2]
        url = "http://orderservice:8000/api/v1/book"
        response = requests.post(
            url=url,
            json={"user_id": user_id, "order_id": order_id, "quantity": quantity},
        )
        if response.status_code == 200:
            return response.json()

    @staticmethod
    def toolsMerged() -> List[Tool]:
        """
        Return a merged list of LangChain tools for agent use.
        """
        toolsMerged = [
            Tool(
                name="RAG_Document_Search",
                description=(
                    "ALWAYS use this tool FIRST for ANY questions about: "
                    "Ray, Ayodeji, Ryan, Tony, Tola, or their family, relationships, occupation, or personal information. "
                    "This tool contains a document with detailed information about these people. "
                    "Input: A specific question about these individuals."
                ),
                func=load_faiss_vector_store,
            ),
            Tool(
                name="translator tool",
                description="Use this anytime you need to translate text from one language to another",
                func=agentools.translator,
            ),
            Tool(
                name="calculator tool",
                description="Use this anytime you need to do a mathematical calculation",
                func=agentools.calculator,
            ),
            Tool(
                name="makeOrder",
                description=(
                    "Use this to book an appointment or place an order. Requires user_id, item_id, and quantity. "
                    "The input to this tool should be a comma-separated list of numbers of length three, "
                    "representing user_id, order_id, quantity, e.g., [xx, yy, zz]."
                ),
                func=agentools.makeOrder,
            ),
        ]
        return toolsMerged
