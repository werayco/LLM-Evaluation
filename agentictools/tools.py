from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from RAG.process import load_faiss_vector_store
from langchain.tools import Tool
from numo import Numo

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
    def translator(query):
        numo = Numo()
        return numo.calculate(query)

    @staticmethod
    def calculator(query):
        numo = Numo()
        return numo.calculate(query)

    @staticmethod
    def toolsMerged():
        toolsMerged = [
            Tool(
                name="RAG_Document_Search",
                description="Answer questions about someone named Ray",
                func=load_faiss_vector_store,
            ),
            Tool(
                name="translator tool",
                description="use this anytime you need to translate text from one language to another",
                func=agentools.translator,
            ),
            Tool(
                name="calculator tool",
                description="use this anytime you need to do a mathematical calculation",
                func=agentools.calculator,
            )
        ]
        return toolsMerged