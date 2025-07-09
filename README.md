# Udaan Translate API

A lightweight, modular translation microservice built for **Project Udaan (IIT Bombay)**.  
This RESTful API supports bulk translations using an LLM (like LLaMA 3 via Groq) and is structured for scalability and clean integration.

---

## 🚀 Features

- 🌐 Translate text into multiple languages (e.g., `hi`, `bn`, `ta`, etc.)
- 📦 Bulk translation support
- 🧠 LLM-based translation (LLaMA 3 via Groq API)
- 🛠️ Input validation and error handling
- 🩺 `/health` endpoint for service monitoring
- 📑 Logs all translation requests to SQLite

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework  
- **LangChain + Groq** – LLM integration (LLaMA 3.3)  
- **Pydantic** – Request validation  
- **SQLite** – Lightweight logging database  
- **dotenv** – Secret/API key management  

---

## 🧪 Running Locally

1. **Clone the repo**:
   ```bash
   git clone https://github.com/Tapas000/Translation-Microservice-IIT-Bombay.git
   cd udaan-translate-api

2.python -m venv .venv
  source .venv/bin/activate  # or .venv\Scripts\activate on Windows

3.pip install -r requirements.txt
4.API=your_groq_api_key
5.uvicorn main:app --reload

