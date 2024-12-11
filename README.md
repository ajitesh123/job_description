# JobDescription Crew

Welcome to the JobDescription Crew project, powered by [crewAI](https://crewai.com). This project helps you generate professional job postings using a multi-agent AI system that researches, writes, and reviews job descriptions while considering company culture and industry requirements.

## Installation

Ensure you have Python >=3.10 <=3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```

### Configuration

1. Create a `.env` file and add your API keys:
```
OPENAI_API_KEY=your_key_here
SERPER_API_KEY=your_key_here
```

2. Customize the configuration files:
- Modify `src/job_description/config/agents.yaml` to configure the research, writer, and review agents
- Modify `src/job_description/config/tasks.yaml` to adjust the tasks for company research, role requirements, job posting drafting, and review
- Modify `src/job_description/crew.py` to customize agent tools and task configurations
- Modify `src/job_description/main.py` to update the input parameters for your job posting

## Running the Project

To generate a job posting, run this from the root folder:

```bash
$ crewai run
```

The default configuration expects these inputs:
- company_domain: Your company's career website
- company_description: A brief description of your company
- hiring_needs: The position title and basic requirements
- specific_benefits: Key benefits offered for the position

## Understanding Your Crew

The JobDescription Crew consists of three specialized agents:
1. Research Agent: Investigates company culture and role requirements
2. Writer Agent: Drafts the initial job posting
3. Review Agent: Reviews and refines the final posting

These agents work sequentially through five main tasks:
- Research company culture
- Analyze role requirements
- Draft the job posting
- Review and edit the posting
- Conduct industry analysis

## Support

For support, questions, or feedback regarding the JobDescription Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
