#%% packages
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_ollama.embeddings import OllamaEmbeddings

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%%
MODEL_NAME="text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=MODEL_NAME)
# %% create OpenAI embeddings
text_sample = ["hallo und willkommen"]
embeddings = embedding_model.embed_documents(text_sample)

#%% create local embeddings
local_embedding_model = OllamaEmbeddings(model="nomic-embed-text")
embeddings = local_embedding_model.embed_documents(text_sample)
#%% output
len(embeddings[0])
