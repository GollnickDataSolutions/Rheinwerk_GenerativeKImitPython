#%% packages
from langchain_ollama import ChatOllama

#%% Modellinstanz
model = ChatOllama(model="gemma3:4b", temperature=0.3)


#%% Modellinferenz
res = model.invoke("Was ist Rheinwerk?")

#%%
res.model_dump()

#%%
from pprint import pprint
pprint(res.content, width=30)