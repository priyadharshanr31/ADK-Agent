# pdf_agent/agent.py

from google.adk.agents import Agent
from .tools import answer_question_from_pdf, summarize_pdf, ask_about_uploaded_pdf


pdf_reader_agent = Agent(
    name="pdf_reader_agent",
    model="gemini-1.5-flash",
    description="Agent that answers questions and summarizes PDF content with memory.",
    instruction=(
        "You are a helpful assistant that answers questions or summarizes uploaded PDFs. "
        "Use previously uploaded content if no file is attached."
    ),
    tools=[answer_question_from_pdf, summarize_pdf, ask_about_uploaded_pdf],
)
