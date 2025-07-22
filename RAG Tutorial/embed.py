import chunk
import chromadb
from google import genai

google_client = genai.Client(api_key="")
EMBEDDING_MODEL = "gemini-embedding-001"

# https://ai.google.dev/gemini-api/docs/models#gemini-2.5-flash
# "gemini-2.5-flash-lite-preview-06-17" | "gemini-2.5-flash" | "gemini-2.5-pro"
LLM_MODEL = "gemini-2.5-flash-lite-preview-06-17"

chromadb_client = chromadb.PersistentClient("./chroma.db")
chromadb_collection = chromadb_client.get_or_create_collection("example_vector_db")

def embedding(text: str, store: bool) -> list[float]:
    """Embedding text to a vector by task_type"""
    result = google_client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text,
        config={
            "task_type": "RETRIEVAL_DOCUMENT" if store else "RETRIEVAL_QUERY"
        }
    )

    assert result.embeddings
    assert result.embeddings[0].values
    return result.embeddings[0].values

def create_db() -> None:
    """Embedding each chunk into chromadb"""
    for idx, c in enumerate(chunk.get_chunks()):
        print(f"Process: {c}")

        embedding_result = embedding(c, store=True)
        chromadb_collection.upsert(
            ids=str(idx),
            documents=c,
            embeddings=embedding_result
        )

def query_db(question: str) -> list[str]:
    """Query answer from chromadb"""
    question_embedding = embedding(question, store=False)
    result = chromadb_collection.query(
        query_embeddings = question_embedding,
        n_results = 5
    )

    assert result["documents"]
    return result["documents"][0]


if __name__ == "__main__":
    # create_db()
    # question = "令狐沖領悟了甚麼魔法"
    question = "令狐冲领悟了什么魔法？"
    
    chunks = query_db(question)

    prompt = "Please answer user's question according to context\n"
    prompt += f"Question: {question}"
    prompt += "Context:\n"
    for c in chunks:
        prompt += f"{c}"
        prompt += "-" * 10

    result = google_client.models.generate_content(
        model=LLM_MODEL,
        contents=prompt
    )

    print(result)