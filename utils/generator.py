import google.generativeai as genai
from .prompts import SUMMARY_PROMPT_TEMPLATE, GOAL_PROMPT_TEMPLATE, MCQ_PROMPT_TEMPLATE
from langchain_core.prompts import PromptTemplate
import os
import streamlit as st

# ✅ Configure the Gemini API
genai.configure(api_key= st.secrets["api_key"])  # Replace with your actual Gemini API key


# ✅ Create the Gemini model instance
model = genai.GenerativeModel("models/gemini-1.5-flash")  # <- Correct format

def generate_summary(content):
    prompt = SUMMARY_PROMPT_TEMPLATE.format(text=content)
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_goals(content):
    prompt = GOAL_PROMPT_TEMPLATE.format(content=content)
    response = model.generate_content(prompt)
    return response.text.strip().splitlines()

def generate_mcqs(content):
    prompt = MCQ_PROMPT_TEMPLATE.format(content=content)
    response = model.generate_content(prompt)
    return response.text.strip().split("\n\n")
