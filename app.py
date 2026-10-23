import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
)

c1,c2 = st.columns([7,1])
with c1:
    st.title("AI Resume Analyzer")
with c2:
    st.button("👤")

c1,c2 = st.columns(2)
with c1:
    st.write("Upload your resume to analyze it.")

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf"]
    )

with c2:
    st.write("Upload your resume to analyze it.")

if st.button("Analyzer"):
        st.success("Resume uploaded successfully!")