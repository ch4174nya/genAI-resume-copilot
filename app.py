import streamlit as st
from resume_parser import extract_text_from_pdf
from role_matcher import suggest_roles
from feedback_engine import rewrite_resume_line, suggest_resume_improvements

st.title("GenAI Resume Copilot (Prototype)")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)
    if st.toggle("Extracted Resume Text"):
        st.text_area("Resume Content", resume_text, height=400)

    if resume_text:
        st.subheader("🎯 Job Role Suggestions")
        if st.button("Suggest Roles"):
            with st.spinner("Analyzing..."):
                roles = suggest_roles(resume_text)
                st.markdown(roles)

        st.subheader("🛠 Improve a Resume Bullet")
        resume_line = st.text_input("Paste a resume bullet point below", placeholder= "Paste here" )
        if st.button("Rewrite"):
            if resume_line.strip(): # if not empty
                with st.spinner("Thinking..."):
                    improved = rewrite_resume_line(resume_line)
                    st.success("Here's the revised version")
                    st.markdown(improved)
        
        st.subheader("🔍 Overall Resume Feedback")
        if st.button("Analyze Resume"):
            with st.spinner("Analyzing Resume..."):
                feedback = suggest_resume_improvements(resume_text)
                st.markdown(feedback)
                
