from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.utilities.sql_database import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.tools.sql_database.tool import (
    InfoSQLDatabaseTool, 
    ListSQLDatabaseTool, 
    QuerySQLDataBaseTool,
    QuerySQLCheckerTool
)

model = ChatGroq(model='llama-3.2-90b-vision-preview')

db = SQLDatabase.from_uri('sqlite:///ipca.db')

toolkit = SQLDatabaseToolkit(db=db, llm=model)

system_message = hub.pull('hwchase17/react')

agent = create_react_agent(
    llm=model,
    tools=toolkit.get_tools(),
    prompt=system_message,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=toolkit.get_tools(),
)

prompt = '''
Use as ferrmentas necessárias para responder perguntas relacionadas ao histórico de IPCA ao longo dos anos.
Responda tudo em português brasileiro.
Perguntas: {q}
'''
prompt_template = PromptTemplate.from_template(prompt)

question = '''
Baseado nos dados históricos de IPCA desde 2004,
faça uma previsão dos valores de IPCA de cada mês futuro até o final de 2025.
'''

output = agent_executor.stream(
    {
        'input': prompt_template.format(q=question),
    },
)

for event in output:
    event["messages"][-1].pretty_print()