from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    dimensions=64
)

texts = [
    "You are learning GEN_AI",
    "Python is a programming language"
]

vectors = embeddings.embed_documents(texts)

print(vectors)
print(len(vectors))
print(len(vectors[0]))