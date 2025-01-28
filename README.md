# Knowledgeable-AI Medical Chatbot

**Knowledgeable-AI** is an intelligent medical chatbot application designed to provide insightful answers to user queries. It leverages powerful language models, embeddings, and document retrieval techniques to analyze data from various sources, including PDFs and URLs. This application is built with **Streamlit** for an interactive and user-friendly interface.

---

## Features
- **Multiple Data Sources**: Analyze data from uploaded PDFs, URLs, or pre-indexed default data.
- **Conversational Interface**: Ask questions interactively and get responses in real time.
- **Chat History**: View your question-answer history for context and reference.
- **Embeddings & Retrieval**: Utilizes advanced embeddings (HuggingFace) and retrieval mechanisms for precise responses.
- **Custom Prompting**: Generates context-specific, accurate answers using a custom prompt template.

---

## Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/)
- **Backend**: Python, LangChain, Ollama, Chroma, Pinecone
- **Embeddings**: HuggingFace Embeddings
- **Data Sources**: PDF files, URLs, and pre-loaded databases

---

## Installation and Setup
### Prerequisites
- Python 3.8+
- API keys for:
  - Google Generative AI
  - Pinecone

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/AITHASAIVARUN/knowledgeable-ai.git
   cd knowledgeable-ai

   pip install -r requirements.txt

   GOOGLE_API_KEY=your_google_api_key
   PINECONE_API_KEY=your_pinecone_api_key

   streamlit run app_main.py

   



