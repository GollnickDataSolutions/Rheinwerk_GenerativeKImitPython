#%% packages
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from autogen import ConversableAgent

#%% LLM configuration
llm_config = {
    "config_list": [
        {
            "model": "llama-3.3-70b-versatile",
            "temperature": 0.8,
            "base_url": "https://api.groq.com/openai/v1",
            "api_key": os.getenv("GROQ_API_KEY")
        }
    ]
}

#%% Agent 1: Flacherdler
jack_flat_earther = ConversableAgent(
    name="Jack",
    llm_config=llm_config,
    system_message="""
    Du bist überzeugt, dass die Erde eine Scheibe ist.
    Du versuchst andere von deiner Meinung zu überzeugen.
    Du antwortest kurz und bündig.
    """,
    human_input_mode="NEVER"
)


#%% Agent 2: Physikerin
alice_scientist = ConversableAgent(
    name="Alice",
    llm_config=llm_config,
    system_message="""
    Du bist eine rational denkende Wissenschaftlerin und davon überzeugt, dass die Erde nahezu rund ist.
    Antworte freundlich, kurz und bündig.
    """,
    human_input_mode="NEVER"
)

#%%
result = jack_flat_earther.initiate_chat(
    recipient=alice_scientist,
    message="Hallo, wie weit ist es von Hamburg bis zum Rand der Erde?",
    max_turns=2
)
# %%
