# 📄 PDF QA & Summarizer Agent

This project is an AI-powered autonomous agent built using Google's Agent Development Kit (ADK). The agent allows users to upload PDF files and either ask questions about the content or receive a concise summary. It also supports memory: once a PDF is uploaded, you can ask follow-up questions without re-uploading the file.

---

## 🚀 Features

- 🤖 Built with Google ADK  
- 🔍 Answers questions based on PDF content  
- 📝 Summarizes full PDF documents  
- 🧠 Uses Gemini 1.5 Flash to interpret user intent and decide which tool to run (autonomous tool selection)  
- 📎 Supports file upload via the Google ADK Developer UI  
- 💾 In-memory support: ask follow-up questions about previously uploaded PDF files  

---

## 🧠 How It Works

The project defines a single autonomous agent:

- **Name:** `pdf_reader_agent`  
- **Model:** `Gemini 1.5 Flash`  
- **Instruction:** Designed to interpret user queries about PDF files and intelligently pick the right tool.  

### Tools:

| Tool Name                  | Description                                                                  |
|---------------------------|------------------------------------------------------------------------------|
| `answer_question_from_pdf`| Extracts text from a newly uploaded PDF and answers a specific question.      |
| `summarize_pdf`           | Summarizes the full content of a newly uploaded PDF.                          |
| `ask_about_uploaded_pdf`  | Answers follow-up questions based on the previously uploaded PDF (in-memory). |

**Google ADK** enables automatic function calling where the agent chooses the appropriate tool based on your query.

---

## 🗂️ Project Structure

29_may_qa_adk/
├── main.py # (Optional) Manual dev entry (not needed for ADK Dev UI)
├── project.yaml # Defines agent metadata and entrypoint for ADK
├── pdf_agent/
│ ├── init.py # Initializes the agent module
│ ├── agent.py # Defines the root agent using ADK
│ ├── tools.py # Tools: summarization, Q&A, and follow-up via memory
│ ├── memory.py # In-memory storage for last uploaded PDF content
│ └── utils.py # PDF text extraction utility (using PyMuPDF)



---

## ⚙️ Requirements

- Python 3.10+  
- [Google ADK](https://github.com/google/agent-development-kit)  
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) (`fitz`)  
- Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)  

---

## 🔑 Environment Setup

Create a `.env` file or export the following in your shell:

```env

GOOGLE_API_KEY=your_google_api_key_here
🧪 Running with Google ADK Dev UI

1. Install Google ADK:
pip install google-agents

2. Install other dependencies:
bash
Copy
Edit
pip install -r requirements.txt

3. Start the Developer UI:
adk web

4. In your browser:
Open: http://localhost:8080

Select your project from the dropdown

Upload a PDF file using the 📎 button

Ask a question like:

"What is the total amount mentioned in this invoice?"

"Summarize this document in 3 lines."

"What company issued this invoice?" (after upload, no need to reattach the file)

📌 Notes
If you ask a question without uploading a PDF, the agent will attempt to use the last uploaded file stored in memory.

Currently, only one PDF is stored at a time (in-memory).
