# AI Career RAG Agent — Personal Knowledge Base, Career Intelligence & Interview Assistant

A personal AI-powered career assistant that combines **Retrieval-Augmented Generation (RAG)** with **n8n workflow automation** to retrieve career knowledge, analyze incoming career-related emails, identify important actions and deadlines, and prepare personalized career alerts.

The project was built as a hands-on learning and portfolio project to understand how **RAG, vector search, LLMs, structured outputs, workflow automation, and messaging integrations** can work together in a practical AI application.

---

## 🚀 Overview

The AI Career RAG Agent has two connected parts:

### 1. Personal RAG Knowledge Base

A Python-based RAG system stores and retrieves information from personal career documents such as:

* Education
* Technical skills
* Work experience
* Projects
* Job applications
* Interview information
* Career goals and professional direction

The system uses **ChromaDB** for persistent vector storage and **Sentence Transformers** for semantic embeddings.

When a question is asked, the system retrieves relevant information from the knowledge base and provides that context to a **Groq LLM**, which generates a grounded response.

### 2. n8n Career Alert Automation

An n8n workflow extends the RAG system into a career-monitoring assistant.

The workflow:

* Monitors incoming Gmail messages
* Retrieves relevant career knowledge
* Processes the email and retrieved information
* Uses Groq LLM to analyze the career relevance
* Produces structured career information
* Determines action requirements and deadline status
* Generates a career alert
* Is being extended with WhatsApp Business for notifications

---

# 🏗️ System Architecture

## RAG Architecture

```text
                    ┌──────────────────────┐
                    │   Career Documents   │
                    │                      │
                    │ profile.txt          │
                    │ projects.txt         │
                    │ job_applications.txt │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Document Ingestion │
                    │      Python          │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Text Chunking     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ Sentence Transformers│
                    │  all-MiniLM-L6-v2    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      ChromaDB        │
                    │   Vector Database    │
                    └──────────┬───────────┘
                               │
                       Semantic Retrieval
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Retrieved Context │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │       Groq LLM       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Grounded Response  │
                    └──────────────────────┘
```

---

# 🔄 n8n Career Alert Workflow

The RAG knowledge base is also used as part of an **n8n-based career intelligence and notification workflow**.

## Current Workflow

```text
┌───────────────┐
│ Gmail Trigger │
└───────┬───────┘
        │
        ▼
┌──────────────────┐
│  HTTP Request    │
│ Retrieve Career  │
│ Knowledge        │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Code Node     │
│ Process Data     │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│ HTTP Request 1   │
│ Additional Data  │
│ Processing       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Groq LLM      │
│ Career Analysis  │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Code Node 1   │
│ Structured Output│
│ Processing       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│    Code Node 2   │
│ Deadline / Alert │
│ Processing       │
└────────┬─────────┘
         │
         ▼
┌──────────────────┐
│   Career Alert   │
└────────┬─────────┘
         │
         ▼
┌─────────────────────────┐
│ WhatsApp Business       │
│ Integration             │
│ In Progress             │
└─────────────────────────┘
```

---

# 🧩 n8n Workflow Components

### 1. Gmail Trigger

The workflow starts when a new email is received.

It is intended to identify career-related messages such as:

* Interview invitations
* Interview reminders
* Job application updates
* Recruiter communication
* Assessment notifications
* Application deadlines
* Other career-related messages

---

### 2. HTTP Request

The workflow sends a request to retrieve relevant information from the personal career knowledge system.

The retrieved information provides additional context about:

* Skills
* Projects
* Experience
* Previous applications
* Career direction
* Technologies used

This allows the LLM to analyze an incoming email using both the **email content** and the **personal career knowledge base**.

---

### 3. Code Node

The first Code node processes and prepares the retrieved information for downstream workflow processing.

This helps normalize the data before it is passed to the next request and analysis stages.

---

### 4. HTTP Request 1

A second HTTP Request node handles the required downstream request/data processing before the LLM analysis stage.

---

### 5. Groq LLM

The Groq LLM analyzes the incoming email together with the retrieved career context.

The structured analysis includes fields such as:

```json
{
  "category": "...",
  "summary": "...",
  "career_relevance": "...",
  "action_required": "...",
  "deadline": "...",
  "deadline_status": "..."
}
```

The LLM is used to convert unstructured email information into structured career intelligence.

---

### 6. Code Node 1

This node processes the structured LLM output and prepares it for the subsequent workflow logic.

---

### 7. Code Node 2

The final processing stage evaluates deadline information and prepares the career alert.

The workflow can distinguish situations such as:

* Upcoming deadline
* Overdue deadline
* Completed/old reminder
* No deadline detected

This prevents older interview or application reminders from being treated as current alerts.

---

# 📱 WhatsApp Business Integration

WhatsApp Business is the planned notification channel for the career-alert workflow.

The intended flow is:

```text
Gmail
   ↓
RAG Knowledge Retrieval
   ↓
Career Email Analysis
   ↓
Groq LLM
   ↓
Deadline / Career Alert Processing
   ↓
WhatsApp Business
   ↓
Career Notification
```

### Current Status

**WhatsApp integration: In Progress**

The Meta WhatsApp Business account has been created and the account is currently under review.

The following components will be configured after the Meta setup is ready:

* WhatsApp Business API / Cloud API connection
* Phone number
* Phone Number ID
* API credentials/access token
* n8n WhatsApp integration
* Test message
* Final career-alert notification

The WhatsApp node is therefore **not yet marked as completed** in this project.

---

# 🧠 RAG Pipeline

The RAG component follows this process:

```text
Documents
    ↓
Document Ingestion
    ↓
Text Chunking
    ↓
Embedding Generation
    ↓
ChromaDB
    ↓
Semantic Search
    ↓
Relevant Context
    ↓
Groq LLM
    ↓
Grounded Answer
```

The system retrieves relevant information instead of relying only on the LLM's general knowledge.

This helps the assistant provide answers based on the user's actual career information.

---

# 📚 Knowledge Base

The current knowledge base contains:

### `profile.txt`

Contains information such as:

* Education
* Skills
* Experience
* Professional direction
* Career information

### `projects.txt`

Contains information about:

* AI automation projects
* GTM automation projects
* Revenue intelligence projects
* RAG projects
* Technical implementations
* Project status

### `job_applications.txt`

Contains information related to:

* Job applications
* Interview information
* Application status
* Deadlines
* Career opportunities

---

# ⚙️ RAG Technical Pipeline

The Python implementation performs the following steps:

### Step 1 — Document Ingestion

Text documents are loaded from the knowledge-base directory.

### Step 2 — Chunking

Documents are divided into meaningful sections/chunks for retrieval.

### Step 3 — Embedding Generation

Sentence Transformers generates vector embeddings using:

```text
all-MiniLM-L6-v2
```

### Step 4 — Vector Storage

Embeddings are stored persistently in:

```text
ChromaDB
```

### Step 5 — Semantic Retrieval

A user query is converted into an embedding and compared against stored vectors.

Relevant chunks are retrieved based on semantic similarity.

### Step 6 — Context Construction

The retrieved chunks are combined into context for the LLM.

### Step 7 — Grounded Generation

The Groq LLM generates a response using the retrieved personal context.

---

# 🛡️ Grounding & Accuracy

The project is designed to reduce unsupported career claims by grounding responses in the personal knowledge base.

The knowledge base also distinguishes between:

* **Completed work**
* **In-progress work**
* **Planned/future work**

This is especially important for accurately representing project experience during interviews and job applications.

---

# ✨ Key Features

* Personal career knowledge base
* RAG-based semantic retrieval
* Document ingestion from `.txt` files
* Section-based document chunking
* Sentence Transformer embeddings
* Persistent ChromaDB vector storage
* Semantic search
* Groq LLM integration
* Grounded response generation
* Project-specific retrieval
* Structured LLM output
* Career relevance analysis
* Email-based career monitoring
* Deadline extraction and status evaluation
* Career alert generation
* n8n workflow automation
* Gmail integration
* HTTP API integration
* Code-based workflow processing
* WhatsApp Business notification integration in progress
* Environment-variable based API-key management

---

# 💻 Technology Stack

## AI / RAG

* Python
* RAG
* ChromaDB
* Sentence Transformers
* all-MiniLM-L6-v2
* Groq LLM
* Semantic Search
* Prompt Engineering

## Automation

* n8n
* Gmail
* HTTP Requests
* Webhooks/API-based workflow processing
* JavaScript Code nodes

## Messaging

* WhatsApp Business / WhatsApp Cloud API — integration in progress

## Development

* Python
* Git
* GitHub
* `.env`
* python-dotenv

---

# 📁 Project Structure

```text
AI-Career-RAG-Agent/
│
├── app/
│   ├── config.py
│   ├── ingest.py
│   ├── retrieve.py
│   └── main.py
│
├── data/
│   └── documents/
│       ├── profile.txt
│       ├── projects.txt
│       └── job_applications.txt
│
├── privacy-policy.html
├── data-deletion.html
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🔐 Environment Configuration

API keys and secrets should not be stored directly in source code.

Environment variables are used for sensitive configuration.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

Do not commit real API keys, access tokens, WhatsApp credentials, or other secrets to GitHub.

---

# ▶️ Running the RAG Application

## 1. Clone the repository

```bash
git clone https://github.com/archanakrishnan094-max/AI-Career-RAG-Agent.git
```

```bash
cd AI-Career-RAG-Agent
```

## 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file and add the required API credentials.

## 5. Ingest the knowledge base

```bash
python -m app.ingest
```

## 6. Run the application

```bash
python -m app.main
```

---

# 🔄 End-to-End Career Assistant Flow

The overall system can be viewed as:

```text
                     PERSONAL CAREER DATA
                              │
                              ▼
                    ┌─────────────────┐
                    │  RAG Knowledge  │
                    │      Base       │
                    └────────┬────────┘
                             │
                     Semantic Retrieval
                             │
                             ▼
                    ┌─────────────────┐
                    │     ChromaDB    │
                    └────────┬────────┘
                             │
                             ▼
                       Retrieved Context
                             │
                             │
Gmail Email ────────────────┐│
                            ▼▼
                    ┌─────────────────┐
                    │    Groq LLM     │
                    │ Career Analysis  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Structured Data │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Deadline / Alert│
                    │    Processing   │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Career Alert    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ WhatsApp        │
                    │ Business        │
                    │   (In Progress) │
                    └─────────────────┘
```

---

# 🎯 Example Use Cases

The RAG assistant can answer questions such as:

* What are my strongest hands-on technical skills?
* What projects have I built?
* Explain my RevIQ project.
* What technologies did I use in my GTM automation projects?
* What is my experience with RAG?
* What is my experience with LangGraph?
* How should I explain my career transition?
* What debugging challenges did I solve?
* Which projects are completed, in progress, or planned?

The n8n automation can process incoming career emails and identify:

* Interview reminders
* Interview deadlines
* Job opportunities
* Application updates
* Required actions
* Deadline status
* Career relevance

---

# 🧪 Example Structured Career Alert

An analyzed email can be transformed into structured information such as:

```json
{
  "category": "Interview Reminder",
  "summary": "Interview reminder for an applied role",
  "career_relevance": "High",
  "action_required": "Attend the scheduled interview",
  "deadline": "2026-09-22T03:17:00Z",
  "deadline_status": "overdue"
}
```

The actual values depend on the incoming email and the information retrieved from the career knowledge base.

---

# 📈 What I Learned

Through this project, I gained hands-on experience with:

* RAG pipeline design
* Document ingestion
* Text chunking
* Embeddings
* Vector databases
* ChromaDB
* Semantic search
* Context retrieval
* LLM + retrieved context
* Grounded response generation
* Prompt engineering
* Structured LLM output
* Python-based AI application development
* n8n workflow automation
* Gmail integration
* HTTP API integration
* JavaScript-based workflow processing
* Deadline and alert logic
* AI-assisted career automation

---

# 🚧 Current Project Status

**Status: IN PROGRESS**

### Implemented

* Personal career knowledge base
* Document ingestion
* Text chunking
* Sentence Transformer embeddings
* ChromaDB vector storage
* Semantic retrieval
* Groq LLM integration
* Grounded response generation
* Project-specific retrieval logic
* Status-aware prompt grounding
* GitHub Pages privacy policy
* GitHub Pages data deletion instructions

### In Progress

* n8n Gmail-based career alert workflow
* Career email analysis and structured output workflow
* Deadline/status processing
* Career alert generation
* WhatsApp Business integration
* WhatsApp notification node
* API credentials configuration
* End-to-end WhatsApp notification testing

### Future Improvements

* Additional retrieval evaluation
* Improved conversation handling
* More advanced retrieval strategies
* Web interface
* Additional notification channels
* Expanded career intelligence features

---

# 🔒 Privacy & Data

This project includes publicly accessible privacy and data-deletion information for the messaging integration.

**Privacy Policy:**
https://archanakrishnan094-max.github.io/AI-Career-RAG-Agent/privacy-policy.html

**User Data Deletion:**
https://archanakrishnan094-max.github.io/AI-Career-RAG-Agent/data-deletion.html

Sensitive credentials and API keys should never be committed to the repository.

---

# 👩‍💻 Author

**Archana Krishnan**

AI Automation Engineer / GTM Engineer

GitHub:
https://github.com/archanakrishnan094-max

---

# 📌 Project Purpose

This project demonstrates a practical combination of:

**Personal Knowledge → RAG → Semantic Retrieval → LLM → Workflow Automation → Career Intelligence → Notifications**

It is primarily a hands-on learning and portfolio project focused on building practical AI automation systems while maintaining accurate, grounded career information.
