from langchain_core.prompts import ChatPromptTemplate


def define_prompt_template():
    prompt=ChatPromptTemplate.from_messages(
        [
            ("system","You are a helpful massistant . Please  repsonse to the user queries"),
            ("user","Question:{question}")
        ]
    )
    return prompt