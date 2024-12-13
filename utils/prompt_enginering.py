from langchain_core.prompts import ChatPromptTemplate


def define_prompt_template():
    prompt=ChatPromptTemplate.from_messages(
        prompt = ChatPromptTemplate.from_messages([
        ("system", 
         """You are an expert conversational assistant designed to provide accurate and concise answers. 
         Use the following context to respond to user queries. If the context does not provide enough information, 
         say "I’m sorry, I do not have enough information to answer that." 
         Ensure your responses are:
         - Clear and easy to understand.
         - Limited to three sentences unless explicitly requested otherwise.
         - Factually correct, avoiding speculation or assumptions.
         """),
        ("user", 
         """User Question:\n{question}"""),
        ("assistant", 
         """Response:""")
    ])
    )
    return prompt