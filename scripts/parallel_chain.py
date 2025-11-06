#%% packages
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% model instance
MODEL_NAME = "openai/gpt-oss-120b"
model = ChatGroq(model=MODEL_NAME)

#%% parser
parser = StrOutputParser()
#%% Chain Friendly
messages_friendly = [
    ("system", "You are an AI assistant that answers short and in a friendly way."),
    ("user", "User query: {user_query}")
]
prompt_template_friendly = ChatPromptTemplate.from_messages(messages=messages_friendly)

# chain setup
chain_friendly = prompt_template_friendly | model | parser

#%% Chain Sarcastic
messages_sarcastic = [
    ("system", "You are an AI assistant that answers short and in a sarcastic and angry way."),
    ("user", "User query: {user_query}")
]
prompt_template_sarcastic = ChatPromptTemplate.from_messages(messages=messages_sarcastic)

# chain setup
chain_sarcastic = prompt_template_sarcastic | model | parser

#%% combined chain
combined_chain = RunnableParallel[dict](
    friendly = chain_friendly,
    sarcastic = chain_sarcastic
)

# %% chain invocation
inputs={"user_query": "What is the meaning of life?"}
res = combined_chain.invoke(input=inputs)

#%%
from pprint import pprint
pprint(res, width=40)