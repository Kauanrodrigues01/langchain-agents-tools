from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
# Essas classes dependem da lib "wikipedia", instale ela usando: pip install wikipedia


wikipedia = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(
        lang='pt'
    )
)

wikipedia_results = wikipedia.run('Qual a extensão territorial do brasil?')

print(wikipedia_results)