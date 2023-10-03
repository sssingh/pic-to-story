---
title: Picture to Story Generator 
emoji: 📖
colorFrom: yellow
colorTo: red
sdk: gradio
sdk_version: 3.46.0
app_file: app.py
pinned: false
license: mit
---

<a href="https://huggingface.co/spaces/sssingh/pic-to-story"  target="_blank"><img src="https://img.shields.io/badge/click_here_to_open_gradio_app-orange?style=for-the-badge&logo=dependabot"/></a>


# The Storyteller  
***A Large Language Model Based App to Generate Stories from Pictures***

<img src="https://github.com/sssingh/pic-to-story/blob/main/assets/title.jpg?raw=true" width="1000" height="350"/><br><br> 

>This application employs a Image2Text model hosted by Huggingface, which is a modified adaptation of the Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation (BLIP) model. First, it generates a descriptive caption for an image. Then, it utilizes this caption to construct a prompt, which is subsequently used with OpenAI's GPT-3.5 to create engaging stories based on the provided picture. 

## App Flow

<img src="https://github.com/sssingh/pic-to-story/blob/main/assets/app-design.png?raw=true" width="1000" height="450"/><br><br> 

BLIP Image2Text model details can be found [here](https://huggingface.co/Sof22/image-caption-large-copy)

## App Details 

* It's important to note that this sample demonstration app is hosted on the free tiers of Huggingface Spaces, which means it is functional but may exhibit slower performance.
* Additionally, when using the app for the first time or after an extended period (more than 1 hour), you might encounter an "Internal Error" message or receive a story unrelated to the provided image. This is a normal occurrence during the model loading process. Please wait a few seconds and try again; it should function as intended.
* Please be aware that due to cost and resource constraints, the app currently has a maximum story length limit of 100 words per request.

App UI is shown below:

<img src="https://github.com/sssingh/pic-to-story/blob/main/assets/story-teller-app.png?raw=true" width="1000" height="450"/><br><br> 

**Dark Mode Toggle**: Activate it to switch between dark and light mode.  
**Image Selector**: Click on it to pick an image from your computer, or drag and drop an image onto it directly. Click the 'X' to clear the selection and resets the app.  
**Story Length (in words) Slider**: Adjust the slider to specify the desired length of the generated story.  
**Creativity Index Slider**: Modify the slider to indicate the desired level of creativity for the generated story. A range between 0.5 and 0.7 is recommended. Setting it to 1.0 results in highly creative, sometimes amusing output.  
**Generate Story Button**: Press this button to initiate the story generation process.  
**Clear Button**: Clears all settings and resets the app to its default state.  
**Story Text Area**: This is where the generated story will be displayed.  
**Example Section Expander**: Click to expand the section and access built-in examples for quick testing. Simply select an example, click "Generate Story," and no image upload will be necessary.  

The app includes pre-defined examples for your convenience, allowing you to quickly test its capabilities. Explore the examples section, choose one, and click "Generate Story" without needing to upload an image.

<img src="https://github.com/sssingh/pic-to-story/blob/main/assets/story-teller-examples.png?raw=true" width="1000" height="350"/><br><br> 

# Project Source
[👉 Visit GitHub Repo](https://github.com/sssingh/pic-to-story)

# Contact Me
[![email](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sunil@sunilssingh.me)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/@thesssingh)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sssingh/)
[![website](https://img.shields.io/badge/web_site-8B5BE8?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sunilssingh.me)

