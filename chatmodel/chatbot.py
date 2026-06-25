from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatMistralAI(model="mistral-small-2603")

messages = [
    SystemMessage(content="You are a funny and witty AI agent")
]

print("____ Welcome, type 0 to exit ____")

print("1.Funny")
print("2.Serious")
print("3.Sarcastic")

personalities = {
    "1": "You are a funny and witty AI agent",
    "2": "You are a serious and professional AI agent",
    "3": "You are a sarcastic and witty AI agent"
}
choice=input("Choose personality:")
if choice not in personalities:
    print("Invalid choice, select from 1, 2, 3")
    exit()

print("Personality: ", personalities[choice])
messages.append(SystemMessage(content=personalities[choice]))   



while True:
    prompt = input("You: ")

    if prompt == "0":
        break

    messages.append(HumanMessage(content=prompt))

    response = model.invoke(messages)

    messages.append(AIMessage(content=response.content))

    print("Mistral:", response.content)













# import streamlit as st
# from dotenv import load_dotenv
# from pathlib import Path
# from langchain_mistralai import ChatMistralAI

# # Load .env from GENAI folder
# env_path = Path(__file__).parent.parent / ".env"
# load_dotenv(env_path)

# # Page Config
# st.set_page_config(
#     page_title="Mistral AI Assistant",
#     page_icon="🤖",
#     layout="wide"
# )

# # Custom CSS
# st.markdown("""
# <style>

# @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

# html, body, [class*="css"] {
#     font-family: 'Poppins', sans-serif;
# }

# /* Background */
# .stApp {
#     background: linear-gradient(
#         135deg,
#         #0f172a 0%,
#         #1e293b 50%,
#         #334155 100%
#     );
# }

# /* Text */
# p, div, span, label, h1, h2, h3 {
#     color: white !important;
# }

# /* Header */
# .main-title {
#     text-align: center;
#     color: white;
#     font-size: 3rem;
#     font-weight: 800;
#     margin-bottom: 0;
# }

# .sub-title {
#     text-align: center;
#     color: #d1d5db !important;
#     font-size: 1.1rem;
#     margin-bottom: 30px;
# }

# /* Sidebar */
# [data-testid="stSidebar"] {
#     background: #111827;
# }

# [data-testid="stSidebar"] * {
#     color: white !important;
# }

# /* Buttons */
# .stButton button {
#     width: 100%;
#     border-radius: 12px;
#     border: none;
#     background: linear-gradient(90deg,#2563eb,#7c3aed);
#     color: white;
#     font-weight: 600;
#     padding: 10px;
# }

# /* Chat Input */
# .stChatInput textarea {
#     background-color: #1f2937 !important;
#     color: white !important;
#     border-radius: 15px !important;
# }

# /* User Message */
# [data-testid="stChatMessage"] {
#     border-radius: 15px;
#     padding: 10px;
# }

# /* Code Blocks */
# pre {
#     background: #111827 !important;
#     color: white !important;
#     border-radius: 10px;
# }

# /* Scrollbar */
# ::-webkit-scrollbar {
#     width: 8px;
# }

# ::-webkit-scrollbar-thumb {
#     background: #4f46e5;
#     border-radius: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # Header
# st.markdown(
#     "<h1 class='main-title'>🤖 Mistral AI Assistant</h1>",
#     unsafe_allow_html=True
# )

# st.markdown(
#     "<p class='sub-title'>Fast • Smart • Powered by Mistral AI</p>",
#     unsafe_allow_html=True
# )

# # Sidebar
# with st.sidebar:
#     st.title("⚙️ Settings")

#     st.markdown("---")

#     if st.button("🗑️ Clear Chat"):
#         st.session_state.messages = []
#         st.rerun()

#     st.markdown("---")
#     st.success("Model: mistral-small-2603")
#     st.info("LangChain + Streamlit")

# # Chat History
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display Messages
# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# # User Input
# prompt = st.chat_input("Type your message here...")

# if prompt:

#     # Store User Message
#     st.session_state.messages.append(
#         {"role": "user", "content": prompt}
#     )

#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Assistant Response
#     with st.chat_message("assistant"):

#         with st.spinner("Thinking..."):

#             try:
#                 model = ChatMistralAI(
#                     model="mistral-small-2603",
#                     temperature=0.7
#                 )

#                 response = model.invoke(prompt)

#                 answer = response.content

#                 st.markdown(answer)

#                 st.session_state.messages.append(
#                     {
#                         "role": "assistant",
#                         "content": answer
#                     }
#                 )

#             except Exception as e:
#                 st.error(f"Error: {e}")