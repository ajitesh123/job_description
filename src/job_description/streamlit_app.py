import streamlit as st
from src.job_description.crew import JobPostingCrew
from typing import Dict

def get_job_posting(inputs: Dict[str, str]) -> str:
    """Generate job posting using CrewAI"""
    try:
        result = JobPostingCrew().job_posting_team().kickoff(inputs=inputs)
        return result
    except Exception as e:
        st.error(f"Error generating job posting: {str(e)}")
        return None

def main():
    st.set_page_config(
        page_title="Job Description Generator",
        page_icon="📝",
        layout="wide"
    )

    st.title("🤖 AI Job Description Generator")
    st.markdown("Generate professional job descriptions using AI")

    # Input form
    with st.form("job_posting_form"):
        company_domain = st.text_input(
            "Company Domain",
            placeholder="e.g., example.com"
        )
        
        company_description = st.text_area(
            "Company Description",
            placeholder="Brief description of your company"
        )
        
        hiring_needs = st.text_input(
            "Hiring Position",
            placeholder="e.g., Senior Software Engineer"
        )
        
        specific_benefits = st.text_area(
            "Benefits",
            placeholder="List the benefits offered (optional)"
        )

        submit_button = st.form_submit_button("Generate Job Description")

    # Generate job description when form is submitted
    if submit_button:
        if not all([company_domain, company_description, hiring_needs]):
            st.error("Please fill in all required fields")
            return

        with st.spinner("Generating job description..."):
            inputs = {
                'company_domain': company_domain,
                'company_description': company_description,
                'hiring_needs': hiring_needs,
                'specific_benefits': specific_benefits or '',
            }
            
            result = get_job_posting(inputs)
            
            if result:
                st.success("Job description generated successfully!")
                st.markdown("### Generated Job Description")
                st.markdown(result)
                
                # Add copy button
                st.button(
                    "Copy to Clipboard",
                    on_click=lambda: st.write(result)
                )

if __name__ == "__main__":
    main() 