\# AI Career RAG Agent — Personal Knowledge Base \& Interview Assistant



A personal RAG-based AI assistant that retrieves relevant information from career, project, skills, and job-application documents to generate grounded responses.



\## Overview



This project was built to learn and implement the complete Retrieval-Augmented Generation (RAG) pipeline hands-on.



The system uses a personal knowledge base containing structured career and project information. When a question is asked, relevant information is retrieved from the knowledge base and provided to a Groq LLM to generate a grounded response.



\## Architecture



User Question

&#x20;     ↓

Query Processing

&#x20;     ↓

Semantic Retrieval

&#x20;     ↓

ChromaDB Vector Store

&#x20;     ↓

Retrieved Context

&#x20;     ↓

Groq LLM

&#x20;     ↓

Grounded Response



\## Tech Stack



\- Python

\- ChromaDB

\- Sentence Transformers

\- all-MiniLM-L6-v2

\- Groq API

\- python-dotenv

\- Vector Search

\- RAG



\## Key Features



\- Document ingestion from `.txt` files

\- Document section-based chunking

\- Embedding generation using Sentence Transformers

\- Persistent vector storage using ChromaDB

\- Semantic retrieval of relevant career information

\- Groq LLM integration

\- Grounded response generation

\- Project-specific retrieval logic

\- Prompt grounding to reduce unsupported claims

\- Distinction between completed, in-progress, and planned work

\- API-key management using environment variables



\## Knowledge Base



The current knowledge base contains:



\- `profile.txt` — education, skills, experience, and professional direction

\- `projects.txt` — AI automation, GTM, and revenue-intelligence projects

\- `job\_applications.txt` — interview and job-application information



\## What I Learned



Through this project, I gained hands-on experience with:



\- RAG pipeline design

\- Document ingestion

\- Text chunking

\- Embeddings

\- Vector databases

\- Semantic search

\- Context retrieval

\- LLM + retrieved context

\- Grounded response generation

\- Prompt engineering

\- Retrieval quality improvement

\- Persistent vector storage

\- Python-based AI application development



\## Example Use Cases



The assistant can answer questions such as:



\- What are my strongest hands-on technical skills?

\- What projects have I built?

\- Explain my RevIQ project.

\- What debugging challenges did I solve?

\- What is my experience with RAG and LangGraph?

\- How should I explain my career transition?

\- What technologies did I use in my GTM automation projects?



\## Project Status



This is an ongoing learning and portfolio project.



The current implementation covers document ingestion, embeddings, ChromaDB storage, semantic retrieval, Groq LLM integration, and grounded response generation.



Future improvements may include a web interface, more advanced retrieval strategies, conversation memory, and additional evaluation of retrieval quality.



\## Author



Archana Krishnan



AI Automation Engineer / GTM Engineer



GitHub: https://github.com/archanakrishnan094-max

