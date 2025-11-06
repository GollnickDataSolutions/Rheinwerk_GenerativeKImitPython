#%% packages
import os
from pprint import pprint
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter
# %% file reference
data_path = "./data"

#%% loader instance
loader = DirectoryLoader(path=data_path, loader_cls=TextLoader, glob="*.txt", loader_kwargs={"encoding": "utf-8"})
docs = loader.load()
# %% 
docs
# %% Fixed size Splitter
splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=400)
docs_splitted = splitter.split_documents(docs)
len(docs_splitted)

#%% Recursive / Structure-based Splitter
splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=400, separators=["\n\n\n", "\n\n", "\n", " ", ""])
docs_splitted = splitter.split_documents(docs)
len(docs_splitted)

#%% 
pprint(docs[0].page_content, width=30)