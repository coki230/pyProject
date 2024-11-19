from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
import cProfile
import os

def query():
    folder = "index"
    # check if folder exists
    if not os.path.exists(folder):
        documents = SimpleDirectoryReader('C:\\Users\\Coki_Zhao\\Desktop\\temp\\').load_data()
        Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
        Settings.llm = Ollama(model="llama3.1", request_timeout=360.0)
        index = VectorStoreIndex.from_documents(documents)
        index.storage_context.persist(folder)
    else:
        con = StorageContext.from_defaults(persist_dir=folder)
        index = load_index_from_storage(con)

    qe = index.as_query_engine()
    res = qe.query("what is Scrapy?")
    print(res)


print(os.path.exists("index1"))

cProfile.run("query()")