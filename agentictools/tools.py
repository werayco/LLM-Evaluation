from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from RAG.process import load_faiss_vector_store
from langchain.tools import Tool

class agentools:
    @staticmethod
    def ragtool(query, db_directory_path="faiss_db"):
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': "cpu"})
        vector_store = FAISS.load_local(db_directory_path, embeddings, allow_dangerous_deserialization=True)
        retriever = vector_store.as_retriever()
        response = retriever.get_relevant_documents(query)
        print(f"Relevant document chunks:\n{response}\n")
        return response
    
    @staticmethod
    def football():
        pass

    @staticmethod
    def calendar():
        pass

    @staticmethod
    def calculator():
        pass

    @staticmethod
    def toolsMerged(self):
        toolsMerged = [
            Tool(
                name="RAG_Document_Search",
                description="Answer questions about someone named Ray",
                func=load_faiss_vector_store,
            ),
            Tool(
                name="",
                description="",
                func="",
            ),
            Tool(
                name="Football_Live_Scores",
                description="",
                func="",
            ),
            Tool(
                name="",
                description="",
                func="",
            ),
        ]
        return toolsMerged