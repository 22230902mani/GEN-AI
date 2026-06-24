from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

llm = HuggingFaceEndpoint(repo_id="deepseek-ai/deepseek-chat-v4-flash",)

model = ChatHuggingFace(llm=llm)

response = model.invoke("Who is Narendra Modi?")
print(response.content)