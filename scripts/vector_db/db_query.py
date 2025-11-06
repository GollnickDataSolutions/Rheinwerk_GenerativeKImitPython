#%% packages
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

#%% embedding model instance
MODEL_NAME="text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=MODEL_NAME)

#%% vector db instance
db = Chroma(persist_directory="db_weltliteratur", embedding_function=embedding_model)

#%% create retriever
retriever = db.as_retriever(kwargs={"search_type": "similarity", "k": 3})

#%% query db
user_query = "Wer ist Ahab?"
res = retriever.invoke(input=user_query)

#%% output
for r in res:
    print(r.page_content)
    print(r.metadata)
    print("-"*20)
# %%
