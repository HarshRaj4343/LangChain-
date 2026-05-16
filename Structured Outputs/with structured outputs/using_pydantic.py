from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)


# Pydantic is a data validation and data parsing library that uses Python type annotations to define data models. It provides a way to validate and parse data based on the defined models, making it easier to work with structured data in Python applications. Pydantic models can be used to define the expected structure of data, and they will automatically validate and convert incoming data to match the defined types.

