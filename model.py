import requests
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import (
    PromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)
from config import app_config
import mongo_utils as mongo


def __image2text(image):
    """Generates a short description of the image"""
    headers = {"Authorization": app_config.HF_TOKEN}
    try:
        response = requests.post(app_config.I2T_API_URL, headers=headers, data=image)
        response = response.json()[0]["generated_text"]
    except Exception as e:
        print(e)
    return response


def __text2story(image_desc, word_count, creativity):
    """ "Generates a short story based on image description text prompt"""
    ## chat LLM model
    story_model = ChatOpenAI(
        model="gpt-3.5-turbo",
        openai_api_key=app_config.OPENAI_KEY,
        temperature=creativity,
    )
    ## chat message prompts
    sys_prompt = PromptTemplate(
        template="You are an expert storyteller that can generate"
        + " imaginative {word_count} words long story from the input text",
        input_variables=["word_count"],
    )
    system_msg_prompt = SystemMessagePromptTemplate(prompt=sys_prompt)
    human_prompt = PromptTemplate(
        template="{image_desc}", input_variables=["image_desc"]
    )
    human_msg_prompt = HumanMessagePromptTemplate(prompt=human_prompt)
    chat_prompt = ChatPromptTemplate.from_messages(
        [system_msg_prompt, human_msg_prompt]
    )
    ## LLM chain
    story_chain = LLMChain(llm=story_model, prompt=chat_prompt)
    response = story_chain.run(image_desc=image_desc, word_count=word_count)
    return response


def generate_story(image_file, word_count, creativity):
    """Generates a story given an image"""
    # read image as bytes arrayS
    with open(image_file, "rb") as f:
        input_image = f.read()
    # generate caption for image
    image_desc = __image2text(image=input_image)
    # generate story from caption
    story = __text2story(
        image_desc=image_desc, word_count=word_count, creativity=creativity
    )
    # increment the openai access counter and compute count stats
    mongo.increment_curr_access_count()
    max_count = app_config.openai_max_access_count
    curr_count = app_config.openai_curr_access_count
    available_count = max_count - curr_count
    return story, max_count, curr_count, available_count
