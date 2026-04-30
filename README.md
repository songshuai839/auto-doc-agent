
# 🚀 Auto Doc Agent

> AI-powered Code Documentation Generation System using Multi-Agent Architecture

---

## 🧠 Project Overview

Auto Doc Agent is an AI-driven system that automatically analyzes source code and generates professional documentation such as:

- 📄 README documentation  
- 📘 API documentation  
- 🏗️ System design documentation  
- 🧾 Code explanation reports  

It leverages an Agent-based pipeline to simulate human-like code understanding and documentation generation.

---

## ⚡ Key Features

- 🧠 AI Code Understanding (Agent-based)
- 📊 Automatic Code Structure Analysis
- 📄 Multi-format Document Generation (README / API / Design Docs)
- 📥 Export to Word & PDF
- 🗄️ SQLite history logging
- 🌐 Web UI built with Streamlit

---

## 🏗️ System Architecture

```
User Upload Code
        ↓
Code Analyzer Agent
        ↓
Document Generator Agent
        ↓
Export Engine (Word / PDF)
        ↓
Streamlit UI Output
```

---

## 🧩 Tech Stack

- Python 3.10+
- Streamlit
- LangChain (Agent design concept)
- python-docx
- reportlab
- SQLite

---

## 🚀 Quick Start

### 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run application

```bash
py -m streamlit run app.py
```

---

## 📂 Project Structure

```
auto_doc_agent/
│── app.py
│── agent/
│   ├── analyzer.py
│   ├── generator.py
│
│── exporter/
│   ├── word_export.py
│   ├── pdf_export.py
│
│── database/
│   ├── db.py
│
│── uploads/
│── outputs/
```

---

## 🎯 Core Innovation

✔ AI-driven documentation automation  
✔ Agent-based modular design  
✔ End-to-end code understanding pipeline  
✔ Export-ready enterprise documentation system  

---

## 📸 Demo

> Upload code → Analyze → Generate Docs → Download Word/PDF

---

## 🧠 Use Cases

- Software Engineering teams
- Codebase documentation automation
- Legacy system analysis
- Developer productivity enhancement

---

## 📌 Future Improvements

- Multi-file project analysis
- GitHub repository auto parsing
- RAG-based semantic understanding
- UML diagram generation
- Multi-Agent collaboration system

---

## 📜 License

MIT License

---

## ⭐ Author

Auto Doc Agent Project
