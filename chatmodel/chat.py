# pyrefly: ignore [missing-import]
# from IPython import display_functions 
from dotenv import load_dotenv
#from langchain_openai import ChatOpenAI
#from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_groq import ChatGroq
#from langchain.chat_models import init_chat_model
from langchain_mistralai import ChatMistralAI
load_dotenv()

# from langchain_openai import ChatOpenAI

# model1=ChatOpenAI(model="gpt-3.5-turbo")
# response = model1.invoke("Hello, how are you? i am gpt")
# print(response.content)

# model2=ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite")
# response = model2.invoke("Hello, how are you? i am gemini")
# print(response.content)

# model3=ChatGroq(model="openai/gpt-oss-120b")
# response = model3.invoke("Hello, how are you? i am groq")
# print(response.content)

model4=ChatMistralAI(model="mistral-small-2603")
response = model4.invoke("Hello, can you say who is the world cup winner in 2011 in cricket odi")
print(response.content)

# model=init_chat_model("groq:openai/gpt-oss-120b")
# res=model.invoke("Hello, how are you? i am groq")
# print(res.content)
