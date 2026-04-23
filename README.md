🧠 RAG Learning Journey
A personal repository documenting my journey learning Retrieval-Augmented Generation (RAG) from scratch — from core concepts to production-ready projects.

📚 What's Inside
FolderDescription01-notes/Concepts, theory, and learning notes02-experiments/Code experiments and scratch scripts03-projects/End-to-end RAG projects04-papers/Research paper summaries05-docs/Personal documentation and patternsassets/Diagrams, sample data, images

🗺️ Learning Roadmap

 Understand what RAG is and why it exists
 Learn about embeddings and vector similarity
 Understand chunking strategies
 Build a basic RAG pipeline from scratch
 Explore vector databases (FAISS, ChromaDB)
 Build a PDF Q&A bot
 Learn reranking and advanced retrieval
 Explore agentic RAG patterns

🛠️ Tech Stack

Language: Python (from scratch, no frameworks)
Embeddings: OpenAI text-embedding-3-small
LLM: OpenAI GPT-4o-mini / Anthropic Claude
Vector DB: FAISS (local) → ChromaDB
Tools: python-dotenv, pypdf, numpy

🚀 Getting Started
bash# 1. Clone the repo
git clone https://github.com/gkris/rag-learning.git
cd rag-learning

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up your API keys
cp .env.example .env
# Edit .env and add your real API keys
📖 Progress Log
DateMilestone2025-04🌱 Repo created, started learning
📝 Notes
This repo is a learning journal — code may be messy, experiments may fail, and that's the point. Each folder has its own README explaining what's in it.