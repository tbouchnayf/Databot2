
import openai
import gradio as gr

# Initialize conversation history as an empty list
conversation_history = []

def generate_response(user_query):
    global conversation_history
    local_datasets_info = "\n\n".join([f"{key}: {value}" for key, value in dataset_catalog.items()])
    # Your OpenAI API key
    openai.api_key = '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'

    # Append the user's query to the conversation history
    conversation_history.append(f"User: {user_query}\n\n")

    # Build the prompt including the conversation history
    prompt = f'''Chatbot for answering questions about datasets. Here is the information about our datasets:
{local_datasets_info}

The chatbot can provide the dataset or datasets to use for a specific task, information about dataset owners, attributes, and their descriptions. The answer should be precise and brief.

Conversation History:
{"".join(conversation_history)}

Response:'''

    # Sending the prompt to OpenAI's API
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Choose the appropriate model
        prompt=prompt,
        max_tokens=100  # Adjust based on the expected length of the response
    )

    # Append the AI's response to the conversation history
    ai_response = response.choices[0].text.strip()
    conversation_history.append(f"AI: {ai_response}\n")

    # Return the updated conversation history and an empty string to clear the query textbox
    return "".join(conversation_history), ""

def reset():
    global conversation_history
    conversation_history = []
    return "", ""

with gr.Blocks() as demo:
    with gr.Row():
        op = gr.Textbox(label="Conversation", lines=10, value="")
    with gr.Row():
        query = gr.Textbox(label="Your Query", lines=2, placeholder="Type your query here...")
    with gr.Row():
        send_button = gr.Button("Send", variant="primary")
        newsession_button = gr.Button("New Session", variant="primary")

    send_button.click(
        fn=generate_response,
        inputs=query,
        outputs=[op, query],
        queue=False
    )

    newsession_button.click(
        fn=reset,
        inputs=None,
        outputs=[op, query],
    )

demo.launch()
