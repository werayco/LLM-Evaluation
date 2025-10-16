from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    def loadtools():
        pass
