import openai
import os
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import json
import time

from langchain_community.document_loaders import AzureBlobStorageContainerLoader
from langchain.text_splitter import CharacterTextSplitter
from utils import create_index, generate_embeddings
print("packages loaded")

# Azure openai creds
AZURE_OPENAI_API_TYPE = "azure"
AZURE_OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_AZURE")
AZURE_OPENAI_API_BASE = "https://dev-aims-ai.openai.azure.com/"
AZURE_OPENAI_API_VERSION = "2023-12-01-preview"#"2023-12-01-preview" #"2024-02-15-preview"
EMBEDDING_MODEL = "text-embedding-ada-002"
DEPLOYMENT_EMBEDDING_MODEL_NAME = "embeddings-aims"
openai.api_type = AZURE_OPENAI_API_TYPE
openai.api_key = AZURE_OPENAI_API_KEY
openai.api_base = AZURE_OPENAI_API_BASE
openai.api_version = AZURE_OPENAI_API_VERSION
print("loaded azure open ai creds")

# azure ai search creds
AZURE_COG_SEARCH_ENDPOINT = os.getenv("SEARCH_ENDPOINT")
VECTOR_STORE_PASSWORD = os.getenv("SEARCH_KEY")
INDEX_NAME = "try-index-py-aims-4" # add index name here hi pawan
CREDENTIAL = AzureKeyCredential(VECTOR_STORE_PASSWORD) # add azure search key here
print("loaded azure search creds")

# azure blob storage creds
ACCOUNT_KEY = os.getenv("AZURE_BLOB_CONTAINER_KEY") # add account key for blob storage
AZURE_CONNECTION_STRING = os.getenv("AZURE_BLOB_CONNECTION_STRING")
CONTAINER_NAME = "container-aims"
print("loaded bolb stoarge container creds")

# function to create and upload index
def create_and_upload_index():
    
    # document loading
    loader = AzureBlobStorageContainerLoader(conn_str=AZURE_CONNECTION_STRING, 
                                    container=CONTAINER_NAME)
    print("loaded blob container")
    # print(len(loader.load()))
    documents = loader.load()
    # print(documents)
    text_splitter = CharacterTextSplitter(chunk_size=2000)
    pages = text_splitter.split_documents(documents)
    pages_ = [{'id':str(idx),'content':page.page_content, 'metadata':page.metadata['source']}  
              for idx, page in enumerate(pages)]
    print(f"Created {len(pages_)} documents")
    
    # Generate embeddings for content field
    for item in pages_:
        content = item['content']
        content_embeddings = generate_embeddings(DEPLOYMENT_EMBEDDING_MODEL_NAME, content)
        item['contentVector'] = content_embeddings
        
    # Output embeddings to docVectors.json file
    with open("../utils/docVectors.json", "w") as f:
        json.dump(pages_, f)

    # create index
    create_index(AZURE_COG_SEARCH_ENDPOINT, CREDENTIAL, INDEX_NAME)
    print("index created in azure search")
    
    # Insert text and embeddings into vector store
    with open('../utils/docVectors.json', 'r') as file:  
        docs = json.load(file)
    search_client = SearchClient(endpoint=AZURE_COG_SEARCH_ENDPOINT, index_name=INDEX_NAME, 
                                 credential=CREDENTIAL)
    result = search_client.upload_documents(docs)
    print(f"Uploaded {len(docs)} documents")
       
# function call
print("called function")
start_time = time.time()
create_and_upload_index()
print("--- %s seconds ---" % round(time.time() - start_time, 2))
print("function ended")
