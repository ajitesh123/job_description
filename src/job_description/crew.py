from typing import List
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# Check our tools documentations for more information on how to use them
from crewai_tools import SerperDevTool, WebsiteSearchTool

web_search_tool = WebsiteSearchTool()
serper_search_tool = SerperDevTool()

@CrewBase
class JobPostingCrew:
    """Crew for creating professional job postings"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[web_search_tool, serper_search_tool],
            verbose=True
        )
    
    @agent
    def content_creator(self) -> Agent:
        return Agent(
            config=self.agents_config['content_creator'],
            tools=[web_search_tool, serper_search_tool],
            verbose=True
        )
    
    @task
    def analyze_company_profile(self) -> Task:
        return Task(
            config=self.tasks_config['analyze_company_profile'],
            agent=self.researcher()
        )

    @task
    def define_job_requirements(self) -> Task:
        return Task(
            config=self.tasks_config['define_job_requirements'],
            agent=self.researcher(),
        )

    @task
    def write_job_posting(self) -> Task:
        return Task(
            config=self.tasks_config['write_job_posting'],
            agent=self.content_creator(),
            output_file='output/job_posting.md'
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