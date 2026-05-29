from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.tools import ShellTool
from langchain_community.tools import tool
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from typing import Type


# Built-in Tool usage

search_tool = DuckDuckGoSearchRun()
result = search_tool.invoke("What is the current capital of St. Kitts country in Carribeans")
print(result)
print(search_tool.name)
print(search_tool.description)
print(search_tool.args)

# Using Shell Tool 

shell_tool = ShellTool()
res = shell_tool.invoke("whoami")
print(res)
print(shell_tool.name)
print(shell_tool.description)
print(shell_tool.args)

# Building custom tools

# M1

@tool
def factorial(n: int) -> int:
    """
    This tool must be used when the user prompts to find factorial of a given number n.
    """
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

a = factorial.invoke({"n":4})
print(a)
print(factorial.name)
print(factorial.description)
print(factorial.args)



# M2 (Using Structured Tool and Pydantic)

class FactorialInput(BaseModel):
    n: int = Field(required=True, description="The number for which factorial needs to be calculated.")

def factorial(n: int) -> int:
    """
    This tool must be used when the user prompts to find factorial of a given number n.
    """
    res = 1
    for i in range(1,n+1):
        res*=i
    return res

Factorial_tool = StructuredTool.from_function(
    func=factorial,
    name="compute_fact",
    description="This tool must be used when the user prompts to find factorial of a given number n.",
    args_schema=FactorialInput
)

b = Factorial_tool.invoke({"n":5})
print(b)


# M3 (Using BaseTool class)

class FactorialInput(BaseModel):
    n: int = Field(required=True, description="The number for which factorial needs to be calculated.")

class FactorialTool(BaseTool):
    name: str = "compute_fact"
    description: str = "This tool must be used when the user prompts to find factorial of a given number n."
    args_schema: Type[BaseModel] = FactorialInput

    def _run(self, n: int) -> int:
        """
        This tool must be used when the user prompts to find factorial of a given number n.
        """
        res = 1
        for i in range(1,n+1):
            res*=i
        return res
fact_ = FactorialTool()
result_ = fact_.invoke({"n":6})

print(result_)
print(fact_.name)
print(fact_.description)


# Making of a Toolkit


# Custom tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add, multiply]


toolkit = MathToolkit()
tools = toolkit.get_tools()

for tool in tools:
    print(tool.name, "=>", tool.description)
