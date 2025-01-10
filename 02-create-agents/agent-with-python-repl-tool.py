from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_community.tools import Tool
from langchain_experimental.utilities import PythonREPL
from langchain_experimental.agents.agent_toolkits import create_python_agent

model = ChatGroq(model='llama-3.3-70b-versatile')

python_repl_tool = Tool(
    name='Python REPL',
    description='Um shell Python. Use isso para executar código Python. Execute apenas códigos Python válidos.',
    func=PythonREPL().run
)

agent_executor = create_python_agent(
    llm=model,
    tool=python_repl_tool,
    verbose=True
)

# Criar template do prompt
prompt_template = PromptTemplate(
    input_variables=['query'],
    template='''Resolva o problema: {query}'''
)

# Gerar o input para o agente
prompt = prompt_template.format(query='quanto é 20% de 3000')

# Executar agente
response = agent_executor.run(prompt)

# Exibir resposta
print(response)
