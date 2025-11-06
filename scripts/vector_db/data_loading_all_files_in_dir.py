#%% packages
import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
# %% file reference
data_path = "./data"

#%% loader instance
loader = DirectoryLoader(path=data_path, loader_cls=TextLoader, glob="*.txt", loader_kwargs={"encoding": "utf-8"})
docs = loader.load()
# %% 
docs
# %% metadata of the book
docs[1].metadata
