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
    verbose=True
)

prompt = '''
Pegue os ultimos 3 registros da tabela IPCA, o nome da tabela é apenas "IPCA", dá para saber o que saõ olhando o nome da coluna ao qual o valor pertence. Como os meses não estão em numeros, ex: janeiro = 1, então não tem como ordenar pelo mês, você vai ter que analisar os meses e definir qual vem primeiro e qual vem por ultimo. Quando me refiro aos 3 ultimos quero dizer os 3 mais recentes com base na data.

Sempre traga os valores mais formatados e organizados possível para o usuário.
'''

output = agent_executor.invoke(
    {
        'input': prompt,
    },
)

print(output.get('output'))