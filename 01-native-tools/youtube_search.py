from langchain_groq import ChatGroq
from langchain_community.tools import YouTubeSearchTool

youtube_tool = YouTubeSearchTool()

results = youtube_tool.run('Segurança em aplicações web')

print(results)