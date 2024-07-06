from crewai import Crew, Process
from langchain_openai import ChatOpenAI
from agents import AiNewsLatterAgents
from tasks import AiNewslatterTasks
from file_io import save_markdown

from dotenv import load_dotenv
import os
load_dotenv()

agents = AiNewsLatterAgents()
tasks = AiNewslatterTasks()

openai_api_key = os.getenv("OPENAI_API_KEY")

OpenAiGPT4 = ChatOpenAI(
    openai_api_key=openai_api_key,
    model = "gpt-3.5"
)

editor = agents.editor_agent()
news_fetcher = agents.news_fetcher_agent()
news_analyzer = agents.news_analyzer_agent()
newslatter_compiler = agents.newslatter_compiler_agent()

fatch_news_task = tasks.fatch_news_task(news_fetcher)
analyze_news_task = tasks.analyze_news_task(news_analyzer, [fatch_news_task])
compile_newslatter_task = tasks.compile_newslatter_task(
    newslatter_compiler, [analyze_news_task], save_markdown)

crew = Crew(
    agent = [editor, news_fetcher, news_analyzer, newslatter_compiler],
    tasks = [fatch_news_task, analyze_news_task, compile_newslatter_task],
    process = Process.hierarchical,
    manager_llm = OpenAiGPT4,
    verbose = True,
    )

results = crew.kickoff()

print("Crew work results:")
print(results)