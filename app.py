import gradio as gr
from core import chat
from voice_processor import generate_audio_and_update_chat
from image_generator import generate_image_async
from ui_utils import do_entry, handle_voice_input

# FlightAI Voice Chat Assistant
# Features: Voice input, AI chat, synchronized audio-text responses, image generation

with gr.Blocks() as ui:
    with gr.Row():
        chatbot = gr.Chatbot(height=500, type="messages")
        image_output = gr.Image(height=500)
    with gr.Row():
        entry = gr.Textbox(label="Chat with our AI Assistant:")
        voice_input = gr.Button("🎤 Voice Input", variant="primary")
        voice_status = gr.Textbox(label="Voice Status", interactive=False, value="Click microphone to speak")
    with gr.Row():
        clear = gr.Button("Clear")
        loading_indicator = gr.Textbox(label="Status", interactive=False, value="Ready", visible=False)

    # Hidden component to store the AI reply for audio
    reply_store = gr.Textbox(visible=False)

    # Text input handling - generate audio first, then show text and audio simultaneously
    entry.submit(
        lambda: "Processing...", inputs=None, outputs=[loading_indicator]
    ).then(
        do_entry, inputs=[entry, chatbot], outputs=[entry, chatbot]
    ).then(
        chat, inputs=[chatbot], outputs=[chatbot, image_output, reply_store, loading_indicator]
    ).then(
        generate_audio_and_update_chat, inputs=[reply_store, loading_indicator, chatbot], outputs=[voice_status, chatbot]
    ).then(
        lambda: "Ready", inputs=None, outputs=[loading_indicator]
    ).then(
        generate_image_async, inputs=[chatbot], outputs=[image_output]
    )

    # Voice input handling - generate audio first, then show text and audio simultaneously
    voice_input.click(
        lambda: "Processing voice...", inputs=None, outputs=[loading_indicator]
    ).then(
        handle_voice_input, inputs=[chatbot], outputs=[chatbot, voice_status]
    ).then(
        chat, inputs=[chatbot], outputs=[chatbot, image_output, reply_store, loading_indicator]
    ).then(
        generate_audio_and_update_chat, inputs=[reply_store, loading_indicator, chatbot], outputs=[voice_status, chatbot]
    ).then(
        lambda: "Ready", inputs=None, outputs=[loading_indicator]
    ).then(
        generate_image_async, inputs=[chatbot], outputs=[image_output]
    )

    clear.click(lambda: (None, None, "", "Click microphone to speak", "Ready"), inputs=None, outputs=[chatbot, image_output, reply_store, voice_status, loading_indicator], queue=False)

ui.launch(inbrowser=True)
