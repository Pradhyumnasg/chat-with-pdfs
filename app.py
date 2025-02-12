import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS   # VectorStoreDB
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings  ## Vector Embedding
from dotenv import load_dotenv
import time

load_dotenv()

## Load the GROQ and Google API's
groq_api_key = os.getenv("GROQ_API_KEY")
os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")

st.title("Chat with PDF's")

llm = ChatGroq(groq_api_key=groq_api_key, model_name="gemma2-9b-it")

prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based on the provided content only.
    Please provide the most accurate response based on the question
    <context>
    {context}
    <context>
    Questions:{input}
    """
)

uploaded_files = st.file_uploader("Upload PDF(s)", type=["pdf"], accept_multiple_files=True)

def process_pdfs(uploaded_files):
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        docs = []
        for uploaded_file in uploaded_files:
            with open(f"./temp_{uploaded_file.name}", "wb") as f:
                f.write(uploaded_file.getbuffer())
            loader = PyPDFLoader(f"./temp_{uploaded_file.name}")
            docs.extend(loader.load())
        
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        final_documents = text_splitter.split_documents(docs)
        st.session_state.vectors = FAISS.from_documents(final_documents, st.session_state.embeddings)
        st.write("Vector Store DB is Ready")

if uploaded_files and st.button("Process Documents"):
    process_pdfs(uploaded_files)
    
prompt1 = st.text_input("Enter your questions from the documents")

if prompt1 and "vectors" in st.session_state:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    start = time.process_time()
    response = retrieval_chain.invoke({'input': prompt1})
    st.write("Response time:", time.process_time() - start)
    st.write(response['answer'])

    with st.expander("Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("-------------------")
