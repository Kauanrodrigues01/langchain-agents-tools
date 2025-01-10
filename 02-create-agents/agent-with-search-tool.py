from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_experimental.agents.agent_toolkits import create_python_agent

model = ChatGroq(model='llama-3.3-70b-versatile')

ddg_tool = DuckDuckGoSearchRun()

agent_executor = create_python_agent(
    llm=model,
    tool=ddg_tool,
    verbose=True, # Mostra todo o processo e tomada de decissões do agent para gerar a resposta
)

promt_template = PromptTemplate(
    input_variables=['query'],
    template='''
    Pesquise na web sobre {query} e forneça um resumo sobre o assunto.
    Responda tudo em português do Brasil.
    '''
)

prompt = promt_template.format(query='Cristiano Ronaldo')

response = agent_executor.invoke(prompt)

print(response.get('output'))