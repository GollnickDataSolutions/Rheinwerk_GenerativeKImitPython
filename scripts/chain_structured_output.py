#%% packages
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from pprint import pprint
#%% output definition
class RecipeOutput(BaseModel):
    title: str
    ingredients: list[str]
    process_steps: list[str]
    total_time: str

class RecipesOutput(BaseModel):
    recipes: list[RecipeOutput]
#%% parser
parser = PydanticOutputParser(pydantic_object=RecipesOutput)

#%% prompt template
messages = [
    ("system", "Du bist ein Weltklasse-Koch und lieferst eine definierte Anzahl an Rezepten zurück. Verwende strikt das vorgegebene Schema {format_instructions}"),
    ("user", "Rezeptbeschreibung: {recipe_descriptions}, Anzahl Rezepte: {recipe_count}")
]
prompt_template = ChatPromptTemplate.from_messages(messages=messages).partial(format_instructions=parser.get_format_instructions())
prompt_template
#%% model instance
MODEL_NAME = "openai/gpt-oss-120b"
model = ChatGroq(model=MODEL_NAME)

#%% chain setup
chain = prompt_template | model | parser

#%% chain invocation
inputs = {
    "recipe_descriptions": "ein veganes Gericht mit Reis",
    "recipe_count": 5
}
res = chain.invoke(input=inputs)
res
#%% output 
recipes = res.model_dump()["recipes"]
for recipe in recipes:
    print(f"Titel: {recipe["title"]}")
    print(f"Gesamtdauer: {recipe["total_time"]}")
    print(f"Zutaten: {"; ".join(recipe["ingredients"])}")
    print(f"Vorgehensweise: {"; ".join(recipe["process_steps"])}")
    print("-"*20)
    
    
# %%
