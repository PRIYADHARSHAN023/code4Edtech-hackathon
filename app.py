import streamlit as st
import pandas as pd
from components.jd_management import jd_management_page
from components.resume_upload import resume_upload_page
from components.results_dashboard import results_dashboard_page
from components.feedback_generator import feedback_generator_page
from utils.database import initialize_session_state

def main():
    """Main application entry point"""
    st.set_page_config(
        page_title="ResuMatch - Resume Relevance Check System",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    
    # Initialize session state
    initialize_session_state()
    
    # Sidebar navigation
    st.sidebar.title("ResuMatch Navigation")
    page = st.sidebar.selectbox(
        "Select Page",
        ["Job Description Management", "Resume Upload & Processing", "Results Dashboard", "Candidate Feedback"]
    )
    
    # Main title
    st.title("📄 ResuMatch - Automated Resume Relevance Check System")
    st.markdown("---")
    
    # Route to appropriate page
    if page == "Job Description Management":
        jd_management_page()
    elif page == "Resume Upload & Processing":
        resume_upload_page()
    elif page == "Results Dashboard":
        results_dashboard_page()
    elif page == "Candidate Feedback":
        feedback_generator_page()

if __name__ == "__main__":
    main()
