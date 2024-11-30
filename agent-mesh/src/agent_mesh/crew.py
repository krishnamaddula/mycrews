from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from agent_mesh.tools.agent_discovery_tool import AgentDiscoveryTool


@CrewBase
class AgentMesh():
    """AgentMesh crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[AgentDiscoveryTool()],
            verbose=True
        )

    @agent
    def quality_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['quality_analyst'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['quality_task']
        )

    @task
    def output_task(self) -> Task:
        return Task(
            config=self.tasks_config['output_task'],
            tools=[AgentDiscoveryTool()],
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AgentMesh crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
