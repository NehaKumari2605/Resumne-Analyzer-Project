import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
)

c1,c2 = st.columns([7,1])
with c1:
    st.header("AI Resume Analyzer")
with c2:
    st.button("👤")
st.divider()
st.subheader("Turn your resume into opportunities.")

c1,c2 = st.columns(2)
with c1:
    with st.container(border=True):

        st.file_uploader(
            "Upload your resume",
            type=["pdf"]
        )

with c2:
    with st.container(border=True):
        st.text_area(
            "text your descrition"
        )


if st.button("Analyze my resume"):
        st.success("Resume uploaded successfully!")

st.divider()
st.write("Key Features")
st.header("Everything you need")
st.write("Powerful features to help you analyze,improve and stand out ")
c1,c2,c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.header("ATS score")
        st.write("Check how wellyour resumn matches ATS standard")

with c2:
    with st.container(border=True):
        st.header("Details Feedback")
        st.write("Find strenghts and area to improve")

with c3:
    with st.container(border=True):
        st.header("Job Match")
        st.write("See how well your match with target roles")


c1,c2,c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.header("Smart Suggestion")
        st.write("Get AI powered tips to make your resume better")

with c2:
    with st.container(border=True):
        st.header("Smart Suggestion")
        st.write("Get AI powered tips to make your resume better")

with c3:
    with st.container(border=True):
        st.header("Smart Suggestion")
        st.write("Get AI powered tips to make your resume better")