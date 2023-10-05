import gradio as gr
import model
from config import app_config
import mongo_utils as mongo


def clear():
    return None, 50, 0.7, None, None


def create_interface():
    js_enable_darkmode = """() => 
    {
        document.querySelector('body').classList.add('dark');
    }"""
    js_toggle_darkmode = """() => 
    {
        if (document.querySelectorAll('.dark').length) {
            document.querySelector('body').classList.remove('dark');
        } else {
            document.querySelector('body').classList.add('dark');
        }
    }"""

    with gr.Blocks(
        title=app_config.title, theme=app_config.theme, css=app_config.css
    ) as app:
        # enable darkmode
        app.load(fn=None, inputs=None, outputs=None, _js=js_enable_darkmode)
        with gr.Row():
            darkmode_checkbox = gr.Checkbox(
                label="Dark Mode", value=True, interactive=True
            )
            # toggle darkmode on/off when checkbox is checked/unchecked
            darkmode_checkbox.change(
                None, None, None, _js=js_toggle_darkmode, api_name=False
            )
        with gr.Row():
            with gr.Column():
                gr.Markdown(
                    """
                    # The Storyteller
                    **This app can craft captivating narratives from captivating images, 
                    potentially surpassing even Shakespearean standards.  
                    <br>
                    Select an `Image` that inspires a story, choose a `Story Genre`, 
                    `Story Writing Style`, `Story Length (up to 200 words)`, and 
                    adjust the `Creativity Index` to enhance its creative flair. Then 
                    hit `Generate Story` button.
                    Alternatively, just select one the pre-configured `Examples`**  
                    <br>
                    ***Please exercise patience, as the models employed are extensive 
                    and may require a few seconds to load. If you encounter an unrelated 
                    story, it is likely still loading; wait a moment and try again.***
                    """
                )
            with gr.Column():
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
                with gr.Row():
                    with gr.Column():
                        genre = gr.Dropdown(
                            label="Story Genre: ",
                            value="Poetry",
                            choices=app_config.genre,
                        )
                        style = gr.Dropdown(
                            label="Story Writing Style:",
                            value="Cinematic",
                            choices=app_config.writing_style_list,
                        )
                    with gr.Column():
                        # Word Count Slider
                        word_count = gr.Slider(
                            label="Story Length (words):",
                            minimum=30,
                            maximum=200,
                            value=50,
                            step=10,
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
                    lines=21,
                )
        with gr.Row():
            with gr.Accordion("Expand for examples:", open=False):
                gr.Examples(
                    examples=[
                        [
                            "assets/examples/cheetah-deer.jpg",
                            "Horror",
                            "Narrative",
                            80,
                            0.5,
                        ],
                        [
                            "assets/examples/man-child-pet-dog.jpg",
                            "Fiction",
                            "Formal",
                            100,
                            0.6,
                        ],
                        [
                            "assets/examples/man-child.jpeg",
                            "Children Literature",
                            "Symbolic",
                            120,
                            1.0,
                        ],
                        [
                            "assets/examples/men-fighting.jpg",
                            "Comedy",
                            "Experimental",
                            60,
                            0.4,
                        ],
                        [
                            "assets/examples/teacher-school.jpg",
                            "Surrealism",
                            "Non-linear",
                            80,
                            0.7,
                        ],
                    ],
                    fn=model.generate_story,
                    inputs=[image, genre, style, word_count, creativity],
                    outputs=[story, max_count, curr_count, available_count],
                    run_on_click=True,
                )
        submit_button.click(
            fn=model.generate_story,
            inputs=[image, genre, style, word_count, creativity],
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
