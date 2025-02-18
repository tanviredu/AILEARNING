import streamlit as st
from langchain.vectorstores import FAISS
from langchain.embeddings import LlamaCppEmbeddings
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import TextLoader
import os

# Load and process medical documents
def load_documents():
    loader = DirectoryLoader("./medical_docs", glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    return docs

# Create FAISS vector store
def create_vector_store():
    docs = load_documents()
    embeddings = LlamaCppEmbeddings()
    db = FAISS.from_documents(docs, embeddings)
    db.save_local("medical_faiss_db")
    return db

# Load existing FAISS store or create a new one
if os.path.exists("medical_faiss_db"):
    db = FAISS.load_local("medical_faiss_db", LlamaCppEmbeddings())
else:
    db = create_vector_store()

# Initialize the QA system
retriever = db.as_retriever()
qa_chain = RetrievalQA.from_chain_type(
    llm=LlamaCpp(model_path="path/to/your/llama/model.bin"),
    chain_type="stuff",
    retriever=retriever
)

# Streamlit UI
st.title("Medical Document Chatbot 🏥")
st.write("Ask me anything about the medical documents!")

query = st.text_input("Enter your question:")
if query:
    response = qa_chain.run(query)
    st.write("### Response:")
    st.write(response)
