# Retrieval-Augmented Generation (RAG)
* Enables models to leverage external knowledge bases

## Why RAG
* Reduces reliance on **training data**
* Mitigates **hallucination** (where models generate incorrect or fabricated information)
* Enables models to leverage **external knowledge bases**, making them more effective for tasks like question answering, research, and domain-specific applications

## RAG Workflow Steps
1. Preprocessing
  * Collect data
  * Split data into `n` chunks
  * Convert the data into vector embeddings using embedding models
  * Store these embeddings in a vector database

```mermaid
graph LR
A1[What are the best places to visit in Japan in October?] --> B{embedding}
A2[Kyoto autumn foliage reports] --> B
A3[Tokyo festival schedules] --> B
A4[Hokkaido weather forecasts] --> B

B --> C1[0.15, 0.34, 0.72, ..., 0.08]
B --> C2[0.23, 0.45, 0.61, ..., 0.03]
B --> C3[0.19, 0.28, 0.55, ..., 0.07]
B --> C4[0.41, 0.67, 0.29, ..., 0.12]

C1 --> D{Store}
C2 --> D
C3 --> D
C4 --> D

D --> E[Vector DB]
```

2. User Query
  * Convert `user query` to an embedding
  * Search the vector database to find the top `n` most relevant documents based on similarity scores to the `user query`

```mermaid
graph LR
A[User Query:
What’s the weather like in Taipei today?] --> B{embedding}
B --> C[0.24, 0.73, 0.33, ..., 0.79]
C --> D{Search Vector DB}
D --> E[Top 5 Relevant Documents]
```

3. Response
  * Retrieved relevant documents and combined them to original query
  * Generate result based on those information by LLM

```mermaid
graph LR
A1[System Prompt:<br/>Please answer user's question according to context] --> B{concat}
A2[User Query:<br/>What’s the weather like in Taipei today?] --> B
A3[Context:<br/>Top 5 Relevant Documents] --> B

B --> C[Prompt]

C --> D[Generate Result]
```
