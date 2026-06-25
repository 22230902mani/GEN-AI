from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts = [
    "Hello I am Manikanta L",
    "I am from Andhra Pradesh",
    "I am a student"
]

vectors = embeddings.embed_documents(texts)

print(vectors)
print(len(vectors))
print(len(vectors[0]))  # embedding dimension