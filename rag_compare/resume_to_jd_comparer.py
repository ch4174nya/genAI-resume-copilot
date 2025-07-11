import openai
import streamlit as st

client = openai.Client(api_key=st.secrets["OPENAI_API_KEY"])

def compare_resume_to_jd(jd, resume_chunks):
    prompt = f"""
    You are a resume expert AI.

    Compare the following resume sections to the job description provided as input:
    ---
    Resume Sections: 
    {resume_chunks}
    ---
    Give feedback on:
    1. Strengths/match
    2. Missing skills or experience
    3. Areas for improvement
    """
    response = client.responses.create(
        model="gpt-4o-mini",
        instructions=prompt,
        input=jd
    )
    return response.output_text
    