from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import warnings
import os

vectordbpath = os.path.join(os.getcwd(),"RAG", "faiss_db")
warnings.filterwarnings("ignore")

def vectorstorecreator(filepath, db_path="faiss_db"):
    docs = PyPDFLoader(filepath).load()
    textsplitter = RecursiveCharacterTextSplitter(chunk_size=200, separators=["\n\n", "\n", " ", ""])
    document_chunks = textsplitter.split_documents(docs)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': "cpu"})
    faiss_vector_database = FAISS.from_documents(document_chunks, embeddings)
    faiss_vector_database.save_local(db_path)

def load_faiss_vector_store(query, db_directory_path=vectordbpath):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': "cpu"})
    vector_store = FAISS.load_local(db_directory_path, embeddings, allow_dangerous_deserialization=True)
    retriever = vector_store.as_retriever()
    response = retriever.get_relevant_documents(query)
    print(f"RAG Observation (Documents Found): {response}") # <--- ADD THIS LINE
    context = "\n\n".join([doc.page_content for doc in response])
    return context

# vectorstorecreator(r"./sample.pdf") # un this once to create the vector store

# print(load_faiss_vector_store("ray and ryan?"))
