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
Crie uma tabela chamada CARROS e insira 3 modelos de carros a essa tabela e no final retorne se deu certo ou errado, caso tenha dado certo retorne os carros que foram inseridos a tabela. A tabela CARROS ainda não existe, precisa ser CRIADA. Insira os valores, depois use um SELECT para ver se os valores foram adicionados.
'''

output = agent_executor.invoke(
    {
        'input': prompt,
    },
)

print(output.get('output'))