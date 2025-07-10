import openai
import streamlit as st

client = openai.Client(api_key=st.secrets["OPENAI_API_KEY"])

def suggest_roles(resume_text):
    prompt = f"""
    You are a career advisor AI. Given the following resume, suggest 3 job role the candidate is a strong match for.
    Use the following format in your responses:
    - Role 1: <title> - <1-line reason>
    - Role 2: ...
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        input=resume_text
    )
    return response.output_text
    