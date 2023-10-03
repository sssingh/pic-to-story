import gradio as gr
import model
from config import app_config
import mongo_utils as mongo


def clear():
    return None, 50, 0.7, None, None


def create_interface():
    with gr.Blocks(
        title=app_config.title, theme=app_config.theme, css=app_config.css
    ) as app:
        # Dark mode toggle functionality
        with gr.Row():
            darkmode_checkbox = gr.Checkbox(label="Dark Mode", value=False)
            darkmode_checkbox.change(
                None,
                None,
                None,
                _js="""() => {
              if (document.querySelectorAll('.dark').length) {
                document.querySelector('body').classList.remove('dark');
              } else {
                document.querySelector('body').classList.add('dark');
              }
            }
            """,
                api_name=False,
            )
        with gr.Row():
            with gr.Column(scale=5):
                gr.Markdown(
                    """
                    # Storyteller
                    **This app can craft captivating narratives from captivating images, 
                    potentially surpassing even Shakespearean standards. Select an image 
                    that inspires a story, choose a story length (up to 100 words), and 
                    adjust the creativity index to enhance its creative flair.**  
                    <br>
                    ***Please exercise patience, as the models employed are extensive and may
                    require a few seconds to load. If you encounter an unrelated story, 
                    it is likely still loading; wait a moment and try again.***
                    """
                )
            with gr.Column(scale=2):
                max_count = gr.Textbox(
                    label="Max allowed OpenAI requests:",
                    value=app_config.openai_max_access_count,
                )
                curr_count = gr.Textbox(
                    label="Used up OpenAI requests:",
                    value=app_config.openai_curr_access_count,
                )
                available_count = gr.Textbox(
                    label="Available OpenAI requests:",
                    value=app_config.openai_max_access_count
                    - app_config.openai_curr_access_count,
                )
        with gr.Row():
            with gr.Column():
                image = gr.Image(
                    type="filepath",
                )
                # Word Count Slider
                word_count = gr.Slider(
                    label="Story Length (words):",
                    minimum=25,
                    maximum=100,
                    value=50,
                    step=5,
                )
                creativity = gr.Slider(
                    label="Creativity Index:",
                    minimum=0.3,
                    maximum=1.0,
                    value=0.7,
                    step=0.1,
                )
                with gr.Row():
                    submit_button = gr.Button(
                        value="Generate Story", elem_classes="orange-button"
                    )
                    clear_button = gr.ClearButton(elem_classes="gray-button")
            with gr.Column():
                story = gr.Textbox(
                    label="Story:",
                    placeholder="Generated story will appear here.",
                    lines=12,
                )
        with gr.Row():
            with gr.Accordion("Expand for examples:", open=False):
                gr.Examples(
                    examples=[
                        ["assets/examples/cheetah-deer.jpg", 50, 0.5],
                        ["assets/examples/man-child-pet-dog.jpg", 100, 0.6],
                        ["assets/examples/man-child.jpeg", 60, 1.0],
                        ["assets/examples/men-fighting.jpg", 50, 0.4],
                        ["assets/examples/teacher-school.jpg", 80, 0.7],
                    ],
                    inputs=[image, word_count, creativity],
                    outputs=[story],
                )
        submit_button.click(
            fn=model.generate_story,
            inputs=[image, word_count, creativity],
            outputs=[story, max_count, curr_count, available_count],
        )
        clear_button.click(
            fn=clear, inputs=[], outputs=[image, word_count, creativity, story]
        )
        image.clear(fn=clear, inputs=[], outputs=[image, word_count, creativity, story])

    return app


if __name__ == "__main__":
    mongo.fetch_curr_access_count()
    app = create_interface()
    app.launch()
