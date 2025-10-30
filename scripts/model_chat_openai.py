#%% packages
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% Modellinstanz
model = ChatOpenAI(model="gpt-4o-mini")


#%% Modellinferenz
res = model.invoke("Was ist Rheinwerk?")

#%%
res.model_dump()

#%%
res.content