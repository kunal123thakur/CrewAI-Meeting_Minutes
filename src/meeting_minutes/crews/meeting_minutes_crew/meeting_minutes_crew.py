from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileWriterTool

file_writer_tool_summary = FileWriterTool(file_name='summary.txt', directory='meeting_minutes')
file_writer_tool_action_items = FileWriterTool(file_name='action_items.txt', directory='meeting_minutes')
file_writer_tool_sentiment = FileWriterTool(file_name='sentiment.txt', directory='meeting_minutes')
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


@CrewBase
class MeetingMinutesCrew():
	"""Meeting Minutes Crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	@agent
	def meeting_minutes_summarizer(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_minutes_summarizer'],
			tools=[file_writer_tool_summary, file_writer_tool_action_items, file_writer_tool_sentiment],
		)
	
	@agent
	def meeting_minutes_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['meeting_minutes_writer'],
		)

    # mutile tasks can be created for the same agent 2 agent does not means 2 tasks it can be more than 2 tasks

	@task
	def meeting_minutes_summary_task(self) -> Task:
		return Task(
			config=self.tasks_config['meeting_minutes_summary_task'],
		)

	@task
	def meeting_minutes_writing_task(self) -> Task:
		return Task(
			config=self.tasks_config['meeting_minutes_writing_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the Research Crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)