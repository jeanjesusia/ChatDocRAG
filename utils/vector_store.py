import os
from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings


def load_existing_vector_store(persist_directory):
    # if vector store already exists, return conection
    if os.path.exists(os.path.join(persist_directory)):
        vector_store = Chroma(
            persist_directory=persist_directory,
            embedding_function=OpenAIEmbeddings()
        )
        return vector_store
    return None


def add_to_vector_store(chunks, vector_store=None, persist_directory=None):
    if vector_store:
        vector_store.add_documents(chunks)
    else:
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=OpenAIEmbeddings(),
            persist_directory=persist_directory
        )
    return vector_store


def check_key(api_key):
    llm = ChatOpenAI(api_key=api_key)
    llm.invoke("Test")