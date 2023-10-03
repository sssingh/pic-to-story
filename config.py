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
    # HF_TOKEN = os.getenv("HF_TOKEN")
    # OPENAI_KEY = os.getenv("OPENAI_KEY")
    # I2T_API_URL = os.getenv("I2T_API_URL")
    # MONGO_CONN_STR = os.getenv("MONGO_CONN_STR")


app_config = AppConfig()
