import os


from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ExaSearchTool
)






@CrewBase
class AutonomousDataCollectionCrew:
    """AutonomousDataCollection crew"""

    
    @agent
    def news_trends_specialist_in_industry_and_society(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["news_trends_specialist_in_industry_and_society"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def academic_research_specialist_in_industry_and_society(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["academic_research_specialist_in_industry_and_society"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def market_data_statistics_analyst(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["market_data_statistics_analyst"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def social_impact_research_specialist(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["social_impact_research_specialist"],
            
            
            tools=[				ExaSearchTool()],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    
    @agent
    def report_writer_and_publisher(self) -> Agent:
        
        
        return Agent(
            config=self.agents_config["report_writer_and_publisher"],
            
            
            tools=[],
            
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            apps=[
                    "googledocs/create_document_markdown",
                    ],
            
            
            max_execution_time=None,
            llm=LLM(
                model="openai/gpt-4o-mini",
                
                
            ),
            
        )
        
    

    
    @task
    def collect_news_and_trends(self) -> Task:
        return Task(
            config=self.tasks_config["collect_news_and_trends"],
            markdown=False,
            
            
        )
    
    @task
    def collect_academic_research(self) -> Task:
        return Task(
            config=self.tasks_config["collect_academic_research"],
            markdown=False,
            
            
        )
    
    @task
    def collect_market_data_and_statistics(self) -> Task:
        return Task(
            config=self.tasks_config["collect_market_data_and_statistics"],
            markdown=False,
            
            
        )
    
    @task
    def collect_social_impact_reports(self) -> Task:
        return Task(
            config=self.tasks_config["collect_social_impact_reports"],
            markdown=False,
            
            
        )
    
    @task
    def compile_and_publish_report_to_google_docs(self) -> Task:
        return Task(
            config=self.tasks_config["compile_and_publish_report_to_google_docs"],
            markdown=False,
            
            
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AutonomousDataCollection crew"""

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,

            chat_llm=LLM(model="openai/gpt-4o-mini"),
        )


