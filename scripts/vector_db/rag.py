#%% packages
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
#%% embedding model instance
MODEL_NAME="text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=MODEL_NAME)

#%% vector db instance
db = Chroma(persist_directory="db_weltliteratur", embedding_function=embedding_model)

#%% create retriever
retriever = db.as_retriever(kwargs={"search_type": "similarity", "k": 3})

#%% 1. Retrieval
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
def rag(user_query):
    res = retriever.invoke(input=user_query)
# list[Documents]  -> str
    # 2. Augmentation (str)
    context_info = ", next chunk: ".join([r.page_content  for r in res])
    # 3. Generation 
    prompt_template = ChatPromptTemplate.from_messages([
    ("system", """  
        Du kannst Fragen auf Basis von Kontextinformationen beantworten.
        Nutze ausschließlich die Kontextinformationen für die Antwort.
        Wenn der Kontext die Frage nicht beantworten lässt, sag 'Ich weiß es nicht.'
    """),
    ("user", f"User Query: {user_query}, Contextinformation: {context_info}")
    ])
 
    model = ChatGroq(model = "openai/gpt-oss-120b")
    chain = prompt_template | model | StrOutputParser()
    res = chain.invoke({"user_query": user_query, "context_info": context_info})
    return res

rag(user_query="Wer ist Frankenstein?")
# %%
