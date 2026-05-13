#%% Pakete
import os
import ssl
import truststore
import httpx
import openrouter
from langchain_openrouter import ChatOpenRouter
from dotenv import load_dotenv
load_dotenv()
# %%
os.getenv("OPENROUTER_API_KEY")

# %% httpx-Client mit Windows-Zertifikatspeicher (löst SSL: CERTIFICATE_VERIFY_FAILED)
ctx = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
headers = {"HTTP-Referer": "https://docs.langchain.com", "X-Title": "LangChain"}
http_client = httpx.Client(verify=ctx, headers=headers, follow_redirects=True)
async_http_client = httpx.AsyncClient(verify=ctx, headers=headers, follow_redirects=True)

sdk_client = openrouter.OpenRouter(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    client=http_client,
    async_client=async_http_client,
)

# %% Modellinstanz erstellen
MODEL="anthropic/claude-sonnet-4.6"
model=ChatOpenRouter(model=MODEL, client=sdk_client)
# %%
query="Was ist Rheinwerk?"
res = model.invoke(query)
# %%
res.model_dump()

# %%
