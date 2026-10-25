# import streamlit as st
# from features import features

# st.set_page_config(
#     page_title="AI Resume Analyzer",
#     layout="wide",
# )

# c1,c2, c3, c4, c5 = st.columns([6,1,1,1,1])
# with c1:
#     st.header("AI Resume Analyzer")

# with c2:
#     st.write("Features")

# with c3:
#     st.write("About")

# with c4:
#     st.write("Contact")
# with c5:
#     st.button("👤")

# st.divider()
# st.subheader("Turn your resume into opportunities.")

# c1,c2 = st.columns(2)
# with c1:
#     with st.container(border=True):
#         resume = st.file_uploader(
#             "Upload your resume",
#             type=["pdf"]
#         )

# with c2:
#     with st.container(border=True):
#         description = st.text_area(
#             "Enter Job Description",
#             placeholder="Paste the job description here..."
#         )



# if st.button("Analyze my resume"):
#     result = features()
#     st.success(result)



#     if resume is None:
#         st.warning("Please upload your resume first.")

#     elif not description.strip():
#         st.warning("Please enter a job description.")

#     else:
#         st.success("Resume uploaded successfully!")
#         st.info("Your resume is ready for analysis.")

# st.divider()
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

# st.divider()

# st.write("How it work")
# st.header("Get your resume analyzer in 3 simple step")

# c1, c2, c3 = st.columns(3)
# with c1:
#     with st.container(border=True):
#         st.header("Paste Description")
#         st.write("")

# with c2:
#     with st.container(border=True):
#         st.header("Upload Resumne")
#         st.write("Choose your file(PDF, DOCX, TXT)")


# with c3:
#     with st.container(border=True):
#         st.header("View Results")
#         st.write("Get your score, feedback and personalised suggestions")


# col1, col2 =st.columns(2)
# with col1:
#     st.write("Why use Resume Analyzer")
#     st.title("Built for students and job seeker")
#     st.write("Whether you're just starting orlooking for next big opportunities Resumne analyzser give you the insinght you to grow and succeed")

# with col2:
#     c1, c2, c3,= st.columns(3)
#     with c1:
#         with st.container(border=True):
#             st.write("Improve your chances")
#             st.write("Build a stronger resumne and get noticed.")

#     with c2:
#             with st.container(border=True):
#                 st.write("Save Time")
#                 st.write("Get instant feedback without the guesswork.")

#     with c3:
#             with st.container(border=True): 
#                 st.write("JOb Ready")
#                 st.write("Be confident and prepared for interviews.")


# c1, c2, c3, c4, c5, c6 = st.columns([2,0.5,0.5,0.5,0.5,1])
# with c1:
#     st.write("Resume Analyzse")
#     st.write("Analyze. Improve. Get Hired")

# with c2:
#     st.write("home")

# with c3:
#     st.write("Features")

# with c4:
#     st.write("About")

# with c5:
#     st.write("Contact")

# with c6:
#     st.write("Made by Neha")



# 



import os
from pathlib import Path

import streamlit as st

from analyzer import extract_resume_text, analyze_resume


# ---------------- PAGE CONFIGURATION ----------------

st.set_page_config(
    page_title="Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ---------------- LOAD CSS ----------------

css_path = Path("assets/style.css")

if css_path.exists():
    with open(css_path, "r", encoding="utf-8") as file:
        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


# ---------------- SESSION STATE ----------------

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "analysis" not in st.session_state:
    st.session_state.analysis = None

if "resume_name" not in st.session_state:
    st.session_state.resume_name = ""


# ---------------- NAVIGATION ----------------

logo, nav1, nav2, nav3, nav4 = st.columns(
    [3, 1, 1, 1, 1]
)

with logo:
    st.markdown("## 📄 Resume Analyzer")

with nav1:
    if st.button("Home", use_container_width=True):
        st.session_state.page = "Home"

with nav2:
    if st.button("Features", use_container_width=True):
        st.session_state.page = "Features"

with nav3:
    if st.button("About", use_container_width=True):
        st.session_state.page = "About"

with nav4:
    if st.button("Analyze Resume", use_container_width=True):
        st.session_state.page = "Analyze"


st.divider()


# ---------------- HOME PAGE ----------------

if st.session_state.page == "Home":

    left, right = st.columns([1.1, 1])

    with left:

        st.markdown(
            '<div class="hero-title">'
            'Turn Your Resume<br>'
            'into <span>Opportunities</span>'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            '<div class="hero-description">'
            'Improve your resume with AI-powered analysis, '
            'skills feedback and personalized suggestions. '
            'Discover strengths and identify areas to improve.'
            '</div>',
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "🚀 Analyze My Resume",
            type="primary",
            use_container_width=True
        ):
            st.session_state.page = "Analyze"
            st.rerun()

        st.caption("Supported formats: PDF, DOCX and TXT")

    with right:

        st.markdown(
            """
            <div style="
                background: linear-gradient(135deg,#e9f2ff,#f4edff);
                border-radius: 25px;
                padding: 55px 20px;
                text-align: center;
                font-size: 85px;">
                📄 🔎
                <div style="
                    font-size: 22px;
                    font-weight: bold;
                    color: #2447a5;">
                    AI Resume Analysis
                </div>
                <div style="
                    font-size: 15px;
                    color: #61749b;
                    margin-top: 10px;">
                    Skills · Experience · Feedback
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # -------- DESCRIPTION SECTION --------

    st.markdown(
        """
        <div class="about-card">
            <h2 style="color:#163574;">
                📘 About Resume Analyzer
            </h2>

            <p>
                Resume Analyzer is an AI-powered tool designed
                to help students and job seekers improve their
                resumes and prepare for career opportunities.
            </p>

            <p>
                Upload your resume to receive feedback on your
                skills, work experience, education and formatting.
                The system identifies strengths, highlights areas
                for improvement and provides personalized
                recommendations for creating a more effective
                resume.
            </p>

            <p>
                Whether you are applying for your first internship
                or preparing for a software developer role,
                Resume Analyzer helps you understand how to
                present your qualifications more effectively.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


    # -------- FEATURES SECTION --------

    st.markdown(
        '<div class="section-title">Everything You Need</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Powerful features to help you analyze, improve and stand out.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    features = [
        (
            "📄",
            "Resume Analysis",
            "Review your resume and receive detailed feedback."
        ),
        (
            "🛡️",
            "ATS Compatibility",
            "Identify potential improvements for ATS readability."
        ),
        (
            "💡",
            "Smart Suggestions",
            "Get practical recommendations to improve your resume."
        ),
        (
            "📊",
            "Skills Analysis",
            "Identify important skills and missing keywords."
        ),
        (
            "📝",
            "Detailed Feedback",
            "Understand strengths and weaknesses in each section."
        ),
        (
            "📥",
            "Download Report",
            "Save your analysis as a text report."
        )
    ]

    rows = st.columns(3)

    for index, feature in enumerate(features):

        with rows[index % 3]:

            st.markdown(
                f"""
                <div class="feature-card">
                    <div class="feature-icon">{feature[0]}</div>
                    <div class="feature-title">{feature[1]}</div>
                    <div class="feature-text">{feature[2]}</div>
                </div>
                """,
                unsafe_allow_html=True
            )


    # -------- HOW IT WORKS --------

    st.markdown(
        '<div class="section-title">'
        'How It Works'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Get your resume analyzed in three simple steps.'
        '</div>',
        unsafe_allow_html=True
    )

    st.write("")

    steps = st.columns(3)

    step_data = [
        ("1️⃣", "Upload Resume", "Choose your PDF, DOCX or TXT file."),
        ("2️⃣", "AI Analysis", "Let AI review your resume."),
        ("3️⃣", "View Results", "Read your feedback and suggestions.")
    ]

    for column, step in zip(steps, step_data):

        with column:

            st.markdown(
                f"""
                <div class="step-card">
                    <div style="font-size:35px;">{step[0]}</div>
                    <h3>{step[1]}</h3>
                    <p style="color:#62769c;">{step[2]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )


    # -------- FOOTER --------

    st.markdown(
        """
        <div class="footer">
            <h3>📄 Resume Analyzer</h3>
            Analyze · Improve · Get Hired
            <br><br>
            Built with Python and Streamlit
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- FEATURES PAGE ----------------

elif st.session_state.page == "Features":

    st.title("✨ Resume Analyzer Features")

    st.write(
        "Explore the tools designed to help you improve your resume."
    )

    st.markdown(
        """
        - 📄 AI-powered resume review
        - 📊 Overall resume quality score
        - 🎯 Job-description keyword comparison
        - 💡 Personalized improvement suggestions
        - 📝 Skills and experience feedback
        - 📥 Downloadable analysis report
        """
    )

    if st.button("Start Analyzing"):
        st.session_state.page = "Analyze"
        st.rerun()


# ---------------- ABOUT PAGE ----------------

elif st.session_state.page == "About":

    st.title("📘 About Our Project")

    st.write(
        """
        Resume Analyzer is a resume-review application built
        using Python and Streamlit.

        It extracts text from resumes and uses a generative AI
        model to provide feedback on resume quality, skills,
        experience and potential improvements.

        The tool is intended to assist students and job seekers.
        Its feedback is advisory and should be reviewed before
        making changes to a resume.
        """
    )

    st.info(
        "The analysis score is an estimate, not an official ATS score."
    )


# ---------------- ANALYZE PAGE ----------------

elif st.session_state.page == "Analyze":

    st.title("🔎 Analyze Your Resume")

    st.write(
        "Upload your resume and optionally provide a target "
        "job description for more relevant feedback."
    )

    uploaded_file = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx", "txt"]
    )

    job_description = st.text_area(
        "Target job description (optional)",
        placeholder=(
            "Paste the job description here to get "
            "more relevant feedback..."
        ),
        height=180
    )

    st.caption(
        "Use a resume you are authorized to upload. "
        "Remove sensitive information you do not want processed."
    )

    if st.button(
        "🚀 Analyze Resume",
        type="primary",
        use_container_width=True
    ):

        if uploaded_file is None:

            st.warning("Please upload your resume first.")

        else:

            try:

                with st.spinner("Reading your resume..."):

                    resume_text = extract_resume_text(
                        uploaded_file
                    )

                with st.spinner("AI is analyzing your resume..."):

                    analysis = analyze_resume(
                        resume_text,
                        job_description
                    )

                st.session_state.analysis = analysis
                st.session_state.resume_name = uploaded_file.name

                st.success("Resume analysis completed!")

            except Exception as error:

                st.error(f"Unable to analyze the resume: {error}")


    # -------- DISPLAY ANALYSIS --------

    if st.session_state.analysis:

        st.divider()

        st.subheader("📊 Analysis Results")

        st.caption(
            f"Resume: {st.session_state.resume_name}"
        )

        st.markdown(
            '<div class="result-card">',
            unsafe_allow_html=True
        )

        st.markdown(st.session_state.analysis)

        st.markdown("</div>", unsafe_allow_html=True)

        st.download_button(
            label="📥 Download Analysis Report",
            data=st.session_state.analysis,
            file_name="resume_analysis.txt",
            mime="text/plain",
            use_container_width=True
        )

        st.caption(
            "AI-generated feedback may contain errors. "
            "Review all suggestions before using them."
        )
        st.caption(
                    "AI-generated feedback may contain errors. "
                    "Review all suggestions before using them."
        )
