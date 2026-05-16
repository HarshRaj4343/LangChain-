from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="conversational"
)

model = ChatHuggingFace(llm=llm)

review_schema = {
    "title": "Review",
    "description": "Extract structured information from a product review.",
    "type": "object",
    "properties": {
        "key_themes": {
            "type": "array",
            "items": {"type": "string"},
            "description": "The main themes discussed in the review, such as performance, battery life, camera quality, etc.",
        },
        "summary": {
            "type": "string",
            "description": "A brief summary of the review",
        },
        "sentiment": {
            "type": "string",
            "enum": ["pos", "neg"],
            "description": "The sentiment of the review, either positive or negative",
        },
        "pros": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of pros mentioned in the review, if any",
        },
        "cons": {
            "type": ["array", "null"],
            "items": {"type": "string"},
            "description": "A list of cons mentioned in the review, if any",
        },
    },
    "required": ["key_themes", "summary", "sentiment"],
}

structured_model = model.with_structured_output(
    review_schema,
    method="json_schema",
)


result = structured_model.invoke("I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver. The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.Pros:Insanely powerful processor (great for gaming and productivity)Stunning 200MP camera with incredible zoom capabilities Long battery life with fast charging S-Pen support is unique and usefulCons:Bulky and heavy-not great for one-handed useBloatware still exists in One UIone handed useExpensive compared to competitors")

print(result)


# with_structured_output has a second argument called method which can be set to "json_schema" or "pydantic". If method is set to "json_schema", the schema should be defined as a JSON schema. If method is set to "pydantic", the schema should be defined as a Pydantic model. By default, method is set to "json_schema".
# also, it has options for function calling and json schema. If you want to use function calling, you can set method to "function_calling" and define the schema as a function signature. If you want to use json schema, you can set method to "json_schema" and define the schema as a JSON schema. By default, method is set to "json_schema".
# claude and gemini support function calling, while huggingface models support json schema. same goes for openai models. gpt-3.5-turbo and gpt-4 support both function calling and json schema, while gpt-4-0613 and gpt-4-1106 only support function calling.
