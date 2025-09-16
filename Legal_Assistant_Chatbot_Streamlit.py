# Legal Assistant Chatbot - Chat Style Streamlit Version

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyMuPDFLoader
from dotenv import load_dotenv
import tempfile

load_dotenv()

st.set_page_config(page_title="Legal Assistant", page_icon="⚖️", layout="wide")
st.title("⚖️ Legal Assistant Chatbot")

# Session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "vector" not in st.session_state:
    st.session_state.vector = None
    st.session_state.retrieval_chain = None

# PDF Upload
uploaded_file = st.file_uploader("Upload a court order PDF", type="pdf")

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(uploaded_file.read())
        pdf_path = tmp_file.name

    loader = PyMuPDFLoader(pdf_path)
    pages = loader.load_and_split()
    st.success(f"{len(pages)} pages loaded.")

    # LLM setup
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # Embeddings + FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = FAISS.from_documents(pages, embeddings)
    st.session_state.vector = vector

    # Prompt template
    prompt = ChatPromptTemplate.from_template("""
    You are a lawyer assistant. Use the following court order context to answer user questions clearly and concisely.

    <context>
    {context}
    </context>

    Question: {input}
    Answer as if you are preparing a legal brief.
    """)

    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = vector.as_retriever(search_kwargs={"k": 4})
    st.session_state.retrieval_chain = create_retrieval_chain(retriever, document_chain)

# Only show chat if PDF is loaded
if st.session_state.vector:
    st.subheader("💬 Chat with the Legal Assistant")

    # Clear chat button
    if st.button("🗑️ Clear Chat"):
        st.session_state.chat_history = []

    # Show previous messages
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.write(msg)

    # Chat input at bottom
    user_query = st.chat_input("Ask a question about the case...")

    if user_query:
        with st.chat_message("user"):
            st.write(user_query)

        result = st.session_state.retrieval_chain.invoke({"input": user_query})
        answer = result["answer"]

        with st.chat_message("assistant"):
            st.write(answer)

        # Save to chat history
        st.session_state.chat_history.append(("user", user_query))
        st.session_state.chat_history.append(("assistant", answer))
