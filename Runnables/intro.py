import random
from abc import ABC, abstractmethod

# =============================================================================
# METHOD 1: AAM ZINDAGI (The Basic/Traditional Way)
# =============================================================================

class AamNakliPromptTemplate:
    def __init__(self, template: str, input_variables: list):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict: dict) -> str:
        return self.template.format(**input_dict)


class AamNakliLLM:
    def __init__(self):
        print('Aam LLM created')

    def predict(self, prompt: str) -> dict:
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}


class AamNakliLLMChain:
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict: dict) -> str:
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result['response']


# =============================================================================
# METHOD 2: MENTOS ZINDAGI (The LCEL / Abstract Base Class Way)
# =============================================================================

class Runnable(ABC):
    @abstractmethod
    def invoke(self, input_data):
        pass


class MentosNakliPromptTemplate(Runnable):
    def __init__(self, template: str, input_variables: list):
        self.template = template
        self.input_variables = input_variables

    def invoke(self, input_dict: dict) -> str:
        return self.template.format(**input_dict)

    def format(self, input_dict: dict) -> str:
        return self.template.format(**input_dict)


class MentosNakliLLM(Runnable):
    def __init__(self):
        print('Mentos LLM created')

    def invoke(self, prompt: str) -> dict:
        return self.predict(prompt)

    def predict(self, prompt: str) -> dict:
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}


class MentosNakliStrOutputParser(Runnable):
    def __init__(self):
        pass

    def invoke(self, input_data: dict) -> str:
        return input_data['response']


class RunnableConnector(Runnable):
    def __init__(self, runnable_list: list):
        self.runnable_list = runnable_list

    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
        return input_data


# =============================================================================
# EXECUTION BLOCK (Testing Both Methods)
# =============================================================================

if __name__ == "__main__":
    
    print("--------------------------------------------------")
    print("TESTING METHOD 1: AAM ZINDAGI (Basic Chain)")
    print("--------------------------------------------------")
    
    aam_template = AamNakliPromptTemplate(
        template='Write a {length} poem about {topic}',
        input_variables=['length', 'topic']
    )
    aam_llm = AamNakliLLM()
    
    # 1. Simple Template formatting test
    aam_prompt_str = aam_template.format({'length': 'short', 'topic': 'india'})
    print(f"Formatted Prompt: {aam_prompt_str}")
    
    # 2. Chain test
    aam_chain = AamNakliLLMChain(aam_llm, aam_template)
    aam_result = aam_chain.run({'length': 'short', 'topic': 'india'})
    print(f"Chain Output: {aam_result}\n")
    
    
    print("--------------------------------------------------")
    print("TESTING METHOD 2: MENTOS ZINDAGI (Runnable/LCEL)")
    print("--------------------------------------------------")
    
    mentos_llm = MentosNakliLLM()
    mentos_parser = MentosNakliStrOutputParser()

    # 1. Simple Runnable Chain
    print("\n--- Running Single Chain ---")
    mentos_template1 = MentosNakliPromptTemplate(
        template='Write a {length} poem about {topic}',
        input_variables=['length', 'topic']
    )
    single_chain = RunnableConnector([mentos_template1, mentos_llm, mentos_parser])
    result_single = single_chain.invoke({'length': 'long', 'topic': 'india'})
    print(f"Single Chain Output: {result_single}")
    
    # 2. Multi-Chain Composability
    print("\n--- Running Composed Chains ---")
    joke_template = MentosNakliPromptTemplate(
        template='Write a joke about {topic}',
        input_variables=['topic']
    )
    explain_template = MentosNakliPromptTemplate(
        template='Explain the following joke {response}',
        input_variables=['response']
    )
    
    chain1 = RunnableConnector([joke_template, mentos_llm])
    chain2 = RunnableConnector([explain_template, mentos_llm, mentos_parser])
    
    final_chain = RunnableConnector([chain1, chain2])
    result_composed = final_chain.invoke({'topic': 'cricket'})
    print(f"Composed Chain Output: {result_composed}")
    print("--------------------------------------------------")