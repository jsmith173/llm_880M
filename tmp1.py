import openai

# Set up the OpenAI client
openai.api_key = 'your-api-key-here'  # Replace with your OpenAI API key

# Function to handle streaming responses
def stream_response(model, messages):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        stream=True,  # Enable streaming mode
        frequency_penalty=0,
        presence_penalty=0,
        top_p=0.1,
        max_tokens=1024
    )
    for chunk in response:
        if 'content' in chunk['choices'][0]['delta']:
            content = chunk['choices'][0]['delta']['content']
            print(content, end='')

# Example messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The LA Dodgers won in 2020."},
    {"role": "user", "content": "Where was it played?"}
]

# Run the streaming response function
stream_response("gpt-3.5-turbo", messages)
