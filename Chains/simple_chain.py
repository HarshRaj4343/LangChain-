from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational"
)
prompt = PromptTemplate(
    input_variables=['topic'],
    template = "Generate 5 important facts about {topic}."
)

model = ChatHuggingFace(llm=llm)


parser = StrOutputParser()

chain = prompt | model | parser
result = chain.invoke({"topic": "the Eiffel Tower"})
print(result)

chain.get_graph().print_ascii()