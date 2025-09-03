# SanS RAG: Sanskrit Text Intelligence System

> **A Retrieval-Augmented Generation (RAG) system for ancient Sanskrit texts, built with modern AI technologies**

## 🎯 What This System Does

SanS RAG transforms ancient Sanskrit scriptures into an intelligent, searchable knowledge base. It allows users to ask questions in English and receive accurate, context-aware answers directly from the original texts, complete with source citations.

### Core Capabilities
- **Multi-source Knowledge Retrieval**: Access Bhagavad Gita, Ramayana, and Yoga Sutras simultaneously
- **Intelligent Text Understanding**: Uses Google Gemini Pro for advanced language comprehension
- **Source Attribution**: Every response includes the exact source document reference
- **Real-time Query Processing**: Instant answers with semantic search across the entire corpus

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Knowledge     │
│   (HTML/JS)     │◄──►│   (FastAPI)     │◄──►│   Base (FAISS)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
   User Interface         RAG Pipeline           Vector Database
   - Mode Selection      - Embeddings          - Document Chunks
   - Chat Interface      - Similarity Search   - Metadata Storage
   - Response Display    - LLM Generation      - Source Tracking
```

## 📚 Knowledge Corpus Structure

```
Corpus/
├── bhagavadgita/
│   └── gita/
│       ├── chapter_1_sanskrit.txt
│       ├── chapter_2_sanskrit.txt
│       └── ... (18 chapters)
├── ramayana/
│   └── kandas/
│       ├── balakanda_sanskrit.txt
│       ├── ayodhyakanda_sanskrit.txt
│       └── ... (5 kandas)
└── yogasutra/
    ├── chapter_1/
    │   ├── sutra.txt
    │   ├── bhashya.txt
    │   └── bhojavruthi.txt
    └── ... (4 chapters)
```

## 🛠️ Technology Stack

| Component | Technology | Version | Purpose |
|-----------|------------|---------|---------|
| **Backend Framework** | FastAPI | 0.110.0 | RESTful API server |
| **AI/ML Framework** | LangChain | 0.1.16 | RAG pipeline orchestration |
| **Language Model** | Google Gemini Pro | 1.5-flash | Text generation & understanding |
| **Embeddings** | Google Generative AI | embedding-001 | Text vectorization |
| **Vector Database** | FAISS | 1.8.0 | Similarity search & storage |
| **Frontend** | HTML5 + Tailwind CSS | - | User interface |
| **Development Server** | Uvicorn | 0.29.0 | ASGI server |

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.11 or higher
- Google Gemini API key
- 2GB+ available RAM for FAISS operations

### Installation Steps

1. **Environment Setup**
   ```bash
   # Clone and navigate
   git clone <repository-url>
   cd SanS_RAG
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # or
   .\venv\Scripts\activate   # Windows
   ```

2. **Dependencies Installation**
   ```bash
   pip install -r requirements.txt
   ```

3. **API Configuration**
   ```bash
   # Create .env file
   echo "GOOGLE_API_KEY=your_api_key_here" > .env
   ```

4. **Knowledge Base Initialization**
   ```bash
   python ingest.py
   ```
   > ⚠️ **Note**: This step processes all text files and creates FAISS indices. Run only once after setup.

5. **Launch Application**
   ```bash
   # Start backend server
   uvicorn backend:app --reload --host 0.0.0.0 --port 8000
   
   # Open frontend
   # Navigate to index.html in your browser
   ```

## 🔧 System Components

### Backend (`backend.py`)
- **FastAPI Application**: RESTful API with CORS support
- **RAG Pipeline**: Document retrieval → LLM generation → Response formatting
- **FAISS Integration**: Efficient similarity search across document chunks
- **Prompt Engineering**: Optimized templates for Sanskrit text comprehension

### Ingestion Engine (`ingest.py`)
- **Document Processing**: Recursive text loading from corpus directories
- **Text Chunking**: 1000-character chunks with 200-character overlap
- **Vector Generation**: Google embeddings for semantic representation
- **Index Creation**: FAISS vector store with metadata preservation

### Frontend (`index.html`)
- **Responsive Design**: Tailwind CSS for modern, mobile-friendly interface
- **Mode Selection**: Switch between different Sanskrit text sources
- **Chat Interface**: Real-time conversation with the AI system
- **Source Display**: Automatic citation of referenced documents

### Testing (`test_backend.py`)
- **Streamlit Interface**: Isolated testing of RAG functionality
- **Component Validation**: Verify embeddings, search, and generation
- **Debug Information**: Source document inspection and response analysis

## 📊 Performance Characteristics

- **Response Time**: < 3 seconds for typical queries
- **Memory Usage**: ~500MB for loaded FAISS index
- **Concurrent Users**: Supports multiple simultaneous queries
- **Accuracy**: Context-aware responses with source verification

## 🔍 Usage Examples

### Basic Query
```
Question: "What does Krishna say about karma in the Bhagavad Gita?"
Mode: Bhagavad Gita
Response: [AI-generated answer with relevant verses + source citation]
```

### Cross-Text Query
```
Question: "How do the Yoga Sutras and Bhagavad Gita approach meditation?"
Mode: [Any mode - system searches across all texts]
Response: [Comprehensive answer drawing from multiple sources]
```

## 🚨 Troubleshooting

### Common Issues

1. **FAISS Index Not Found**
   ```bash
   # Rebuild the knowledge base
   python ingest.py
   ```

2. **API Key Errors**
   ```bash
   # Verify .env file exists and contains valid key
   cat .env
   ```

3. **Memory Issues**
   ```bash
   # Reduce chunk size in ingest.py
   chunk_size=500  # instead of 1000
   ```

4. **CORS Errors**
   - Ensure backend is running on correct port
   - Check browser console for specific error messages

## 🔮 Future Enhancements

- [ ] **Multi-language Support**: Hindi, English translations
- [ ] **Advanced Search**: Filters by chapter, verse, or topic
- [ ] **User Authentication**: Personalized learning paths
- [ ] **Mobile Application**: Native iOS/Android apps
- [ ] **Offline Mode**: Local LLM integration
- [ ] **Analytics Dashboard**: Learning progress tracking

## 📄 License & Attribution

**Developer**: K. Kiran, IIT Kanpur  
**Project Type**: Academic/Research  
**License**: [Specify your license here]

## 🤝 Contributing

This is a research project showcasing RAG implementation for Sanskrit texts. For collaboration or questions:

1. Review the codebase structure
2. Test with different query types
3. Suggest improvements to the RAG pipeline
4. Contribute additional Sanskrit text sources

---

**Built with ❤️ for preserving and making accessible the wisdom of ancient Sanskrit literature through modern AI technology.**
