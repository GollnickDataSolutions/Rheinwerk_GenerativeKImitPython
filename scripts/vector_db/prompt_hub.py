#%% packages
import warnings
from langsmith import Client
client = Client()
prompt = client.pull_prompt("rlm/rag-prompt", include_model=True)


# %%
prompt_name = "rlm/rag-prompt"
prompt_template = client.pull_prompt(prompt_name)

#%%
prompt_template