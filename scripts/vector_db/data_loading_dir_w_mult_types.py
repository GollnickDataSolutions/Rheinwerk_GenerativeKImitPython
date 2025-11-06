#%% packages
import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader, PyMuPDFLoader
# %% file reference
data_path = "./data"

#%% function for selecting the right loader class
def select_loader(file_path: str):
    _, ext = os.path.splitext(file_path)
    if ext == ".txt":
        return TextLoader(file_path=file_path, encoding="utf-8")
    if ext == ".pdf":
        return PyMuPDFLoader(file_path=file_path, mode="single")
    raise ValueError(f"Unsupported file type: {ext} for {file_path}")

#%% loader instance
loader = DirectoryLoader(path=data_path, loader_cls=select_loader)
docs = loader.load()
# %% 
docs
# %% metadata of the book
docs[2].metadata
