#%% packages
import os
from langchain_community.document_loaders import TextLoader
# %% file reference
file_path = "./data/Frankenstein.txt"

#%% loader instance
loader = TextLoader(file_path=file_path, encoding="utf-8")
docs = loader.load()
# %% content of the book
docs[0].page_content
# %% metadata of the book
docs[0].metadata
