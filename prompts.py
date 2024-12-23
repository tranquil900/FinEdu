"""
Centralized prompt templates for the application
"""

from langchain.prompts import ChatPromptTemplate

FINANCIAL_ASSISTANT_PROMPT = ChatPromptTemplate.from_template(
    "You are a financial assistant. Answer the question based on the following context:\n\n"
    "{context}\n\n"
    "Question: {question}\n"
    "Answer:"
)