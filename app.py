import streamlit as st
from features import features

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide",
)

c1,c2, c3, c4, c5 = st.columns([6,1,1,1,1])
with c1:
    st.header("AI Resume Analyzer")

with c2:
    st.write("Features")

with c3:
    st.write("About")

with c4:
    st.write("Contact")
with c5:
    st.button("👤")

st.divider()
st.subheader("Turn your resume into opportunities.")

c1,c2 = st.columns(2)
with c1:
    with st.container(border=True):
        resume = st.file_uploader(
            "Upload your resume",
            type=["pdf"]
        )

with c2:
    with st.container(border=True):
        description = st.text_area(
            "Enter Job Description",
            placeholder="Paste the job description here..."
        )



if st.button("Analyze my resume"):
    result = features()
    st.success(result)



    if resume is None:
        st.warning("Please upload your resume first.")

    elif not description.strip():
        st.warning("Please enter a job description.")

    else:
        st.success("Resume uploaded successfully!")
        st.info("Your resume is ready for analysis.")

st.divider()
# st.write("Key Features")
# st.header("Everything you need")
# st.write("Powerful features to help you analyze,improve and stand out ")
# c1,c2,c3 = st.columns(3)
# with c1:
#     with st.container(border=True):
#         st.header("ATS score")
#         st.write("Check how well your resume matches ATS standard")

# with c2:
#     with st.container(border=True):
#         st.header("Details Feedback")
#         st.write("Find strenghts and area to improve")

# with c3:
#     with st.container(border=True):
#         st.header("Job Match")
#         st.write("See how well your match with target roles")


# c1,c2,c3 = st.columns(3)
# with c1:
#     with st.container(border=True):
#         st.header("Resume Analysis")
#         st.write("Get an overall score and detailed feedback on your resumne")

# with c2:
#     with st.container(border=True):
#         st.header("Smart Suggestion")
#         st.write("Get AI powered tips to make your resume better")

# with c3:
#     with st.container(border=True):
#         st.header("Download Report")
#         st.write("Save your analysis results for future reference")

st.divider()

st.write("How it work")
st.header("Get your resume analyzer in 3 simple step")

c1, c2, c3 = st.columns(3)
with c1:
    with st.container(border=True):
        st.header("Paste Description")
        st.write("")

with c2:
    with st.container(border=True):
        st.header("Upload Resumne")
        st.write("Choose your file(PDF, DOCX, TXT)")


with c3:
    with st.container(border=True):
        st.header("View Results")
        st.write("Get your score, feedback and personalised suggestions")


col1, col2 =st.columns(2)
with col1:
    st.write("Why use Resume Analyzer")
    st.title("Built for students and job seeker")
    st.write("Whether you're just starting orlooking for next big opportunities Resumne analyzser give you the insinght you to grow and succeed")

with col2:
    c1, c2, c3,= st.columns(3)
    with c1:
        with st.container(border=True):
            st.write("Improve your chances")
            st.write("Build a stronger resumne and get noticed.")

    with c2:
            with st.container(border=True):
                st.write("Save Time")
                st.write("Get instant feedback without the guesswork.")

    with c3:
            with st.container(border=True): 
                st.write("JOb Ready")
                st.write("Be confident and prepared for interviews.")


c1, c2, c3, c4, c5, c6 = st.columns([2,0.5,0.5,0.5,0.5,1])
with c1:
    st.write("Resume Analyzse")
    st.write("Analyze. Improve. Get Hired")

with c2:
    st.write("home")

with c3:
    st.write("Features")

with c4:
    st.write("About")

with c5:
    st.write("Contact")

with c6:
    st.write("Made by Neha")
