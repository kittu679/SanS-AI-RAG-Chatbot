# test_backend.py

import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
import asyncio

# --- Configuration and Setup ---

# This is a workaround for a known issue with asyncio on some systems
try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.set_event_loop(asyncio.new_event_loop())

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Check for API key and configure AI models
if not api_key:
    st.error("Google API key not found. Please create a .env file and set your key.")
    st.stop()

# --- Main Application Logic ---

st.set_page_config(page_title="Backend RAG Test")
st.header("Backend RAG Logic Test 🧪")
st.write("This app tests the core RAG functionality in isolation.")

try:
    # Initialize AI models
    genai_chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

    # Load the FAISS index
    FAISS_INDEX_PATH = "faiss_index"
    db = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)

    # Define the prompt and chain
    prompt_template = """
      Answer the question as detailed as possible from the provided context.
      If the answer is not in the provided context, just say, "The answer is not available in the context."\n\n
      Context:\n {context}?\n
      Question: \n{question}\n
      Answer:
    """
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(genai_chat_model, chain_type="stuff", prompt=prompt)

    # --- Streamlit User Interface ---
    st.success("Backend components loaded successfully!")

    user_question = st.text_input("Ask a question to test the RAG system:")

    if user_question:
        with st.spinner("Performing similarity search and getting response..."):
            # Perform similarity search
            docs = db.similarity_search(user_question)
            
            # Get the response from the LLM
            response = chain.invoke({"input_documents": docs, "question": user_question}, return_only_outputs=True)
            
            st.subheader("Response:")
            st.write(response["output_text"])

            st.subheader("Source Documents Used:")
            for doc in docs:
                st.info(f"Source: {os.path.basename(doc.metadata.get('source', 'Unknown'))}")
                st.text(doc.page_content[:300] + "...")


except Exception as e:
    st.error(f"An error occurred: {e}")

