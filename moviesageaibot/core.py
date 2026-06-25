# # MOVIE SAGE AI BOT
# # 1. Take a raw paragraph about a movie
# # 2. Extract important structured information
# # 3. Generate a clean summary
# # 4. Return everything in JSON format

# from dotenv import load_dotenv
# load_dotenv()

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_mistralai import ChatMistralAI

# # Initialize Model
# model = ChatMistralAI(
#     model="mistral-small-2603",
#     temperature=0
# )

# # Prompt Template
# prompt = ChatPromptTemplate.from_messages([
#     (
#         "system",
#         """
#         You are MovieSage AI, an expert movie analyst and information specialist.

#         Your tasks:
#         1. Extract important movie details.
#         2. Generate a concise summary.
#         3. Return ONLY valid JSON.

#         Use this JSON structure:

#         {{
#             "title": "",
#             "genre": "",
#             "director": "",
#             "release_year": "",
#             "cast": [],
#             "summary": ""
#         }}

#         Do not add explanations.
#         Do not use markdown.
#         Return only JSON.
#         """
#     ),
#     (
#         "human",
#         "{movie_text}"
#     )
# ])

# # Create Chain
# chain = prompt | model

# print("=" * 50)
# print("🎬 MOVIE SAGE AI BOT")
# print("=" * 50)

# movie_text = input("\nEnter Movie Description:\n\n")

# response = chain.invoke({
#     "movie_text": movie_text
# })

# print("\nJSON OUTPUT:\n")
# print(response.content)












import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

load_dotenv()

st.set_page_config(
page_title="Movie Sage AI",
page_icon="🎬",
layout="wide"
)

st.markdown("""

<style>
.main {
    background: linear-gradient(135deg,#0f172a,#1e293b);
}
.stTextArea textarea {
    border-radius: 12px;
}
.result-box {
    padding:20px;
    border-radius:15px;
    background:#111827;
    border:1px solid #374151;
}
.title {
    text-align:center;
    font-size:3rem;
    font-weight:bold;
    color:white;
}
.subtitle {
    text-align:center;
    color:#cbd5e1;
}
</style>

""", unsafe_allow_html=True)

st.markdown('<p class="title">🎬 Movie Sage AI</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">AI Movie Analyst & Information Extractor</p>', unsafe_allow_html=True)

model = ChatMistralAI(
model="mistral-small-2603",
temperature=0
)

prompt = ChatPromptTemplate.from_messages([
(
"system",
"""
You are MovieSage AI.

```
    Extract:
    - title
    - genre
    - director
    - release_year
    - cast
    - summary

    Return ONLY valid JSON.
    """
),
("human", "{movie_text}")


])

chain = prompt | model

movie_text = st.text_area(
"Enter Movie Description",
height=250,
placeholder="Paste movie information here..."
)

if st.button("Analyze Movie", use_container_width=True):
    if movie_text.strip():


        with st.spinner("Analyzing Movie..."):

            response = chain.invoke({
            "movie_text": movie_text
        })

    st.success("Analysis Complete")

    st.subheader("JSON Output")
    st.code(response.content, language="json")

else:
    st.warning("Please enter a movie description.")