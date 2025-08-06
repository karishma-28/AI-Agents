from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader

def respond_to_query(documents_path: str, query: str) -> dict:
    documents = SimpleDirectoryReader(documents_path).load_data()
    index = GPTVectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query(query)
    return {
        "query": query,
        "response": str(response)
    }
