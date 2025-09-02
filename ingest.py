# ingest.py (Updated for multiple folders)

import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import DirectoryLoader, TextLoader

# Load environment variables from .env file
load_dotenv()

# --- Main Ingestion Process ---

# 1. Load all documents from the main 'Corpus' folder and its subdirectories
print("Loading documents from all subfolders...")
# This path should be the main folder containing all your different texts (Gita, Ramayana, etc.)
# For example, if your structure is Corpus/bhagavadgita, Corpus/ramayana, point this to './Corpus'
loader = DirectoryLoader(
    './Corpus',  # <-- IMPORTANT: Change this to your main data folder
    glob="**/*.txt",
    loader_cls=TextLoader,
    loader_kwargs={'encoding': 'utf-8'}
)
documents = loader.load()

if not documents:
    print("🛑 Error: No documents were loaded. Please ensure the path is correct and it contains subfolders with .txt files.")
    exit()

print(f"Loaded {len(documents)} document(s) from all sources.")

# 2. Split the documents into smaller chunks
print("Splitting documents into chunks...")
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
docs = text_splitter.split_documents(documents)
print(f"Split documents into {len(docs)} chunks.")

# 3. Initialize the embedding model
print("Initializing embedding model...")
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("Google API key not found. Please check your .env file.")
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

# 4. Create and save the new, combined FAISS vector store
print("Creating and saving the combined FAISS index...")
vectorstore = FAISS.from_documents(docs, embeddings)
vectorstore.save_local("faiss_index")

print("\n✅ Success! Your combined knowledge base has been created in the 'faiss_index' folder.")
