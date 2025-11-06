#%% packages
import os
from pprint import pprint
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
# %% file reference
data_path = "./data"

#%% loader instance
loader = DirectoryLoader(path=data_path, loader_cls=TextLoader, glob="*.txt", loader_kwargs={"encoding": "utf-8"})
docs = loader.load()
# %% 
docs
# %% Fixed size Splitter
# splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
# docs_splitted = splitter.split_documents(docs)
# len(docs_splitted)

#%% Recursive / Structure-based Splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400, separators=["\n\n\n", "\n\n", "\n", " ", ""])
docs_splitted = splitter.split_documents(docs)
len(docs_splitted)

#%% embedding model instance
MODEL_NAME="text-embedding-3-small"
embedding_model = OpenAIEmbeddings(model=MODEL_NAME)

#%% vector db instance
db = Chroma(persist_directory="db_weltliteratur", embedding_function=embedding_model)

# %% add documents to db
import time
for i, current_doc in enumerate(docs_splitted):
    time.sleep(0.5)
    print(f"füge Dokument {i+1}/{len(docs_splitted)}")
    db.add_documents(documents=[current_doc])
# %%
