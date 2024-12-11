from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from src.job_description.crew import JobPostingCrew

app = FastAPI(
    title="Job Description Generator API",
    description="API for generating job descriptions using CrewAI",
    version="1.0.0"
)

class JobPostingInput(BaseModel):
    company_domain: str
    company_description: str
    hiring_needs: str
    specific_benefits: Optional[str] = None

@app.post("/generate-job-posting")
async def generate_job_posting(input_data: JobPostingInput):
    try:
        inputs = {
            'company_domain': input_data.company_domain,
            'company_description': input_data.company_description,
            'hiring_needs': input_data.hiring_needs,
            'specific_benefits': input_data.specific_benefits or '',
        }
        
        # Create crew instance and kickoff the process
        result = JobPostingCrew().crew().kickoff(inputs=inputs)
        
        return {
            "status": "success",
            "result": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return {
        "message": "Job Description Generator API",
        "version": "1.0.0",
        "endpoints": {
            "/generate-job-posting": "POST - Generate a job posting"
        }
    } 