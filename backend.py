# backend.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("Google API key not found. Please check your .env file.")

# Initialize AI models
genai_chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

# Load the FAISS index
FAISS_INDEX_PATH = "faiss_index"
print("Loading FAISS Index...")
db = FAISS.load_local(FAISS_INDEX_PATH, embeddings, allow_dangerous_deserialization=True)
print("FAISS Index loaded successfully.")


# Define the prompt and chain
prompt_template = """
  Answer the question as detailed as possible. read and find relevant content from each and evry text file not only specific to any one.
  If the answer is not in the provided context, just say, "The answer is not available in the context."\n\n
  Context:\n {context}?\n
  Question: \n{question}\n
  Answer:
"""
prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
chain = load_qa_chain(genai_chat_model, chain_type="stuff", prompt=prompt)

# --- API Definition ---
app = FastAPI()

# Allow requests from your HTML file (CORS Middleware)
# This is crucial for allowing your frontend to communicate with this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for simplicity in a hackathon
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Define the data model for the request body
class Query(BaseModel):
    question: str
    mode: str  # e.g., "Bhagavad Gita", "Ramayana"

@app.post("/ask")
def ask_question(query: Query):
    """
    Receives a question from the frontend, gets an answer from the RAG chain,
    and returns the answer along with a source citation.
    """
    print(f"Received question in '{query.mode}' mode: {query.question}")
    
    # Perform similarity search on the loaded FAISS index
    docs = db.similarity_search(query.question)
    
    # Get the response from the LLM
    response = chain({"input_documents": docs, "question": query.question}, return_only_outputs=True)
    
    # Extract source from metadata if available, otherwise use a placeholder
    # This is a key feature for "citation-backed responses"
    source_citation = "Unknown Source"
    if docs and docs[0].metadata and 'source' in docs[0].metadata:
        # Cleans up the source path for better display
        source_citation = os.path.basename(docs[0].metadata['source'])

    print(f"Sending response: {response['output_text']}")
    return {"answer": response["output_text"], "source": source_citation}

# To run this file, use the command in your terminal:
# uvicorn backend:app --reload