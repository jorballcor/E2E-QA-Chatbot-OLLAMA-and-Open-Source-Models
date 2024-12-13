import os
from dotenv import load_dotenv

def activate_langchain_tracking():
    load_dotenv()

    ## Langsmith Tracking
    os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"]=os.getenv("LANGCHAIN_TRACING_V2")
    os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT")