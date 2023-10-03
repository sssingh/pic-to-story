import os
from dataclasses import dataclass
import gradio as gr


@dataclass
class AppConfig:
    title = "Picture to Story Generator"
    theme = "freddyaboulton/dracula_revamped"
    css = "style.css"
    HF_TOKEN = os.getenv("HF_TOKEN")
    OPENAI_KEY = os.getenv("OPENAI_KEY")
    I2T_API_URL = os.getenv("I2T_API_URL")


app_config = AppConfig()
