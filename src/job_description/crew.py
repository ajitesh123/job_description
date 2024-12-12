from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, WebsiteSearchTool, FileReadTool
from pydantic import BaseModel, Field

web_search_tool = WebsiteSearchTool()
serper_search_tool = SerperDevTool()
job_description_reader = FileReadTool(
    file_path='job_description_example.md',
    description='A tool to read the job description example file.'
)

class JobRequirementsSpec(BaseModel):
    """Specification for job requirements"""
    skills: List[str] = Field(..., description="List of recommended skills for the ideal candidate aligned with the company's culture, ongoing projects, and the specific role's requirements.")
    experience: List[str] = Field(..., description="List of recommended experience for the ideal candidate aligned with the company's culture, ongoing projects, and the specific role's requirements.")
    qualities: List[str] = Field(..., description="List of recommended qualities for the ideal candidate aligned with the company's culture, ongoing projects, and the specific role's requirements.")

@CrewBase
class JobPostingCrew:
    """Crew for creating professional job postings"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def company_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['company_researcher'],
            tools=[web_search_tool, serper_search_tool],
            verbose=True
        )
    
    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            tools=[web_search_tool, serper_search_tool, job_description_reader],
            verbose=True
        )
    
    @task
    def analyze_company_profile(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_profile'],
            agent=self.company_researcher()
        )

    @task
    def define_job_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['define_job_requirements'],
            agent=self.company_researcher(),
            output_json=JobRequirementsSpec
        )

    @task
    def write_job_posting(self) -> Task:
        return Task(
            config=self.tasks_config['write_job_posting'],
            agent=self.content_creator()
        )

    @crew
    def job_posting_team(self) -> Crew:
        """Creates the job posting creation team"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )