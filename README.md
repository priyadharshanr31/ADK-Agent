📄 PDF QA & Summarizer Agent
This project is an AI-powered autonomous agent built using Google's Agent Development Kit (ADK). The agent allows users to upload PDF files and either ask questions about the content or receive a concise summary.

🚀 Features
🤖 Built with Google ADK

🔍 Answers questions based on PDF content

📝 Summarizes full PDF documents

🧠 Uses Gemini 1.5 Flash/Pro to interpret user intent and decide which tool to run (autonomous tool selection)

📎 Supports file upload via the Google ADK Developer UI

🧠 How It Works
The project defines a single autonomous agent:

Name: pdf_reader_agent

Model: Gemini 1.5 Flash

Instruction: Designed to interpret user queries about PDF files

Tools:

answer_question_from_pdf: Extracts text from PDF and answers a specific question.

summarize_pdf: Summarizes the full content of the uploaded PDF.

Google ADK enables automatic function calling where the agent chooses the appropriate tool based on your query.

🗂️ Project Structure
graphql
Copy
Edit
29_may_qa_adk/
├── main.py                        # (Optional) Manual dev entry (not needed for ADK Dev UI)
├── project.yaml                   # Defines agent metadata and entrypoint for ADK
├── pdf_agent/
│   ├── __init__.py                # Initializes the agent module
│   ├── agent.py                   # Defines the root agent using ADK
│   ├── tools.py                   # Tools: summarization and Q&A over PDF
│   └── utils.py                   # PDF text extraction utility (using PyMuPDF)
⚙️ Requirements
Python 3.10+

Google ADK

Gemini API key from Google AI Studio

🔑 Environment Setup
Create a .env file or set the following environment variable in your shell:

env
Copy
Edit
GOOGLE_API_KEY=your_google_api_key_here
You can get your API key from: https://makersuite.google.com/app/apikey

🧪 Running with Google ADK Dev UI
Install Google ADK:

bash
Copy
Edit
pip install google-agents
Start the Developer UI:

bash
Copy
Edit
adk web
In your browser:

Open: http://localhost:8080

Choose the (YOUR FILE) from the dropdown.

Upload a PDF file using the 📎 attachment button.

Ask a question like:

"What is the total amount mentioned in this invoice?"

"Summarize this document in 3 lines."