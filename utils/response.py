from langchain_core.output_parsers import StrOutputParser
from langchain_ollama.llms import OllamaLLM
from utils.prompt_enginering import define_prompt_template

## Define prompt template
prompt=define_prompt_template()

def generate_response(question,llm,temperature,max_tokens):
    llm=OllamaLLM(model=llm)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    answer=chain.invoke({'question':question})
    return answer