from google.adk.agents import Agent
from .tools import answer_question_from_pdf, summarize_pdf

pdf_reader_agent = Agent(
    name="pdf_reader_agent",
    model="gemini-1.5-flash",
    description="Agent that answers questions and summarizes PDF content.",
    instruction=(
        "You are a helpful assistant that answers questions or summarizes content from uploaded PDF files."
    ),
    tools=[answer_question_from_pdf, summarize_pdf],
)
