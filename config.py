import os
from dataclasses import dataclass


@dataclass
class AppConfig:
    title = "Picture to Story Generator"
    theme = "freddyaboulton/dracula_revamped"
    css = "style.css"
    openai_max_access_count = 200
    openai_curr_access_count = None
    mongo_client = None
    db = "mydb"
    collection = "pic2story-openai-access-counter"
    key = "current_count"
    HF_TOKEN = os.getenv("HF_TOKEN")
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    I2T_API_URL = os.getenv("I2T_API_URL")
    MONGO_CONN_STR = os.getenv("MONGO_CONN_STR")
    genre_list = genre = [
        "Adventure",
        "Children Literature",
        "Comedy",
        "Drama",
        "Fantasy",
        "Fiction",
        "Horror",
        "Mystery",
        "Non-fiction",
        "Poetry",
        "Romance",
        "Satire",
        "Surrealism",
        "Urban Fantasy",
    ]
    writing_style_list = [
        "Cinematic",
        "Conversational",
        "Descriptive",
        "Experimental",
        "First-Person",
        "Formal",
        "Informal",
        "Metaphorical",
        "Minimalist",
        "Narrative",
        "Non-linear",
        "Objective",
        "Sensory",
        "Stream of Consciousness",
        "Symbolic",
        "Third-Person Limited",
        "Third-Person Omniscient",
    ]

    HF_TOKEN = "Bearer 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"
    OPENAI_KEY = "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"
    I2T_API_URL = (
        "https://api-inference.huggingface.co/models/Sof22/image-caption-large-copy"
    )
    MONGO_CONN_STR = "mongodb+srv://sssingh:Topsycret1@cluster0.fcwxggj.mongodb.net/"


app_config = AppConfig()
