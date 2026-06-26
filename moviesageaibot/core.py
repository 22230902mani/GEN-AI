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










#sir github code


# MovieSage AI bot
# 1 take a raw para about a movie
# 2 Extract important sturtured info
# 3 Generate a clean summary
# 4 Returns it into JSON Format

from dotenv import load_dotenv

load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel
from typing import List,Optional

model = ChatMistralAI(model="mistral-small-2603")

#from langchain_core.prompts import ChatPromptTemplate


class Movie(BaseModel):
    title: str
    genre: str
    director: str
    writers: List[str]
    producers: List[str]
    cast: List[str]
    release_year: Optional[int]
    runtime: Optional[str]
    language: Optional[str]
    country: Optional[str]
    plot_summary: str
    main_characters: List[str]
    themes: List[str]
    notable_facts: List[str]
    awards: List[str]
    box_office: Optional[str]
    rating: Optional[str]
    keywords: List[str]

parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are MovieSage AI, an expert movie analyst and information extraction assistant.

```
    Your responsibilities:

    1. Carefully read and understand the entire movie description.
    2. Extract all important movie-related information.
    3. Generate a concise and engaging plot summary.
    4. Identify key characters, themes, and notable facts.
    5. Extract factual information only from the provided text.
    6. If information is not available, return null.
    7. Never hallucinate or invent details.
    8. Return ONLY valid JSON.
    9. Do not include markdown, explanations, comments, or additional text.

    Extract the following fields:

    - title
    - genre
    - director
    - writers
    - producers
    - cast
    - release_year
    - runtime
    - language
    - country
    - plot_summary
    - main_characters
    - themes
    - notable_facts
    - awards
    - box_office
    - rating
    - keywords

    
    """,
        ),
        (
            "human",
            """
    Analyze the following movie description and extract all relevant information.

    Movie Description:
    {movie_description}
    """,
        ),
    ]
)

para = input("give your paragraph")
final_prompt = prompt.invoke({
                                "movie_description": para,
                                "format_instructions":parser.get_format_instructions()
                            })

res = model.invoke(final_prompt)
print(res.content)


#AI->JSON->Backend->API->Frontend->




