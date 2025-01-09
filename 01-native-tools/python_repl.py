from langchain_experimental.utilities import PythonREPL
# Essa funcionalidade está na fase experimental e depois pode ser colocada no pacote "langchain_community" ou outro

python_repl = PythonREPL()

result = python_repl.run('print(5 * 5)')

print(result)