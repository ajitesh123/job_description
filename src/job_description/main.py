import sys
import os
from typing import Dict
from src.job_description.crew import JobPostingCrew
from dotenv import load_dotenv

def load_environment():
    """Load environment variables required for the application"""
    load_dotenv()
    
    required_vars = ['OPENAI_API_KEY', 'SERPER_API_KEY']
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        raise EnvironmentError(f"Missing required environment variables: {', '.join(missing_vars)}")

def get_job_posting_inputs() -> Dict[str, str]:
    """
    Define the inputs for job posting creation.
    Customize these values based on your specific job posting needs.
    """
    return {
        'company_domain': 'getarchieai.com',
        'company_description': (
            "Archie AI: Coding Automation platform for developers"
        ),
        'hiring_needs': 'Software Engineer, for a coding automation platform',
        'specific_benefits': 'Monthly Salary, Health Insurance, 401k',
    }
def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs =get_job_posting_inputs()
    JobPostingCrew().job_posting_team().kickoff(inputs=inputs)

if __name__ == "__main__":
    load_environment()
    run()