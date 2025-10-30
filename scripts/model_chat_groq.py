#%% packages
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% test, ob umgebungsvariable wirklich geladen wurde und verfügbar ist
os.getenv("GROQ_API_KEY")

#%% Modellinstanz
model = ChatGroq(model="openai/gpt-oss-120b")


#%% Modellinferenz
res = model.invoke("Was ist Rheinwerk?")

#%%
res.model_dump()

#%%
res.content