import streamlit as st
from src.job_description.crew import JobPostingCrew
from typing import Dict
import os

def get_job_posting(inputs: Dict[str, str]) -> str:
    """Generate job posting using CrewAI"""
    try:
        # Execute crew and get the output file path
        JobPostingCrew().job_posting_team().kickoff(inputs=inputs)
        
        # Read the generated output file
        output_path = 'output/job_posting.md'
        if os.path.exists(output_path):
            with open(output_path, 'r') as f:
                return f.read()
        else:
            raise FileNotFoundError("Job posting output file not found")
    except Exception as e:
        st.error(f"Error generating job posting: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="AI Job Description Generator",
        page_icon="🤖",
        layout="centered",
    )

    st.title("AI Job Description Generator", )
    st.markdown("### Generate professional job descriptions using AI")
    st.markdown("---")

    # Input form
    with st.form("job_posting_form"):
        company_domain = st.text_input(
            "Company Domain",
            placeholder="e.g., example.com"
        )
        
        company_name = st.text_input(
            "Company Name",
            placeholder="e.g., Archie AI"
        )
        
        role = st.text_input(
            "Hiring Position",
            placeholder="e.g., Software Engineer"
        )

        specific_benefits = st.text_area(
            "Benefits",
            placeholder="List the benefits offered (optional)"
        )

        submit_button = st.form_submit_button("Generate Job Description")

    # Generate job description when form is submitted
    if submit_button:
        if not all([company_domain, company_name, role]):
            st.error("Please fill in all required fields")
            return

        with st.spinner("Generating job description..."):
            inputs = {
                'company_domain': company_domain,
                'company_name': company_name,
                'role': role,
                'specific_benefits': specific_benefits or '',
            }
            
            result = get_job_posting(inputs)
            
            if result:
                st.success("Job description generated successfully!")
                st.markdown("### Generated Job Description")
                st.markdown(result)
                
                # Add download button
                st.download_button(
                    label="Download Job Description",
                    data=result,
                    file_name="job_description.md",
                    mime="text/markdown"
                )
                
                # Add copy button
                st.button(
                    "Copy to Clipboard",
                    on_click=lambda: st.write(result)
                )

if __name__ == "__main__":
    main() 