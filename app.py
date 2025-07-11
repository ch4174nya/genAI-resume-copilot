import streamlit as st
from resume_parser import extract_text_from_pdf
from role_matcher import suggest_roles
from feedback_engine import rewrite_resume_line, suggest_resume_improvements
from rag_compare.resume_embedder import chunk_text, embed_chunks, build_faiss_index
from rag_compare.resume_to_jd_comparer import compare_resume_to_jd
from rag_compare.faiss_utils import build_faiss_index, search

st.title("GenAI Resume Copilot (Prototype)")

uploaded_file = st.file_uploader("Upload your resume (PDF only)", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    if resume_text:

        with st.expander("Show Extracted Resume Text"):
            st.text_area("Resume Content", resume_text, height=400)

        chunks = chunk_text(resume_text)
        embeddings = embed_chunks(chunks=chunks)
        index = build_faiss_index(embeddings=embeddings)

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

        st.subheader("📌 Paste a Job Description to Compare")
        job_desc = st.text_area("Enter the target job description here", placeholder="Paste job description here")

        if st.button("Compare Resume to JD"):
            if job_desc.strip():
                jd_embeddings  = embed_chunks([job_desc])[0]    # single vector? TODO
                k = 5
                top_indices = search(index, jd_embeddings, k)
                relevant_chunks = [chunks[i] for i in top_indices]
                
                with st.spinner("Comparing..."):
                    feedback = compare_resume_to_jd(job_desc.strip(),"\n".join(relevant_chunks))
                    st.subheader("🔍 Resume vs JD Feedback")
                    st.markdown(feedback)
                    with st.expander("🔍 Retrieved Resume Sections"):
                        for chunk in relevant_chunks:
                            st.markdown(f"- {chunk}")