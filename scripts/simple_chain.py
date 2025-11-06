#%% packages
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

#%% prompt template
messages = [
    ("system", "You are an AI assistant that translates text into other languages."),
    ("user", "Translate the text: {text_to_translate} into the target language {target_language}")
]
prompt_template = ChatPromptTemplate.from_messages(messages=messages)

#%% model instance
MODEL_NAME = "openai/gpt-oss-120b"
model = ChatGroq(model=MODEL_NAME)

#%% parser
parser = StrOutputParser()

#%% chain setup
chain = prompt_template | model | parser

#%% chain invocation
inputs = {
    "text_to_translate": "Wir besuchen einen Rheinwerk-Kurs zu Generativer KI.",
    "target_language": "Spanish"
}
res = chain.invoke(input=inputs)
res
#%%
