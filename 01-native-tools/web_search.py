from langchain_community.tools import DuckDuckGoSearchRun # tem que instalar o duckduckgo-search

ddg_search = DuckDuckGoSearchRun()

search_result = ddg_search.run('Quem foi Cristiano Ronaldo')

print(search_result)