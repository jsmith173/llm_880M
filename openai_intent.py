from openai import OpenAI
import json

# model0 = "llama3.1"
model = "llama-3.2-3b-instruct"

port=11434
#port=1234

# Set up the OpenAI client
client = OpenAI(
    base_url=f'http://127.0.0.1:{port}/v1',
    api_key='ollama'  # required, but unused
)

# Define JSON schema for response_format
response_format = {
      "type": "json_schema",
      "json_schema": {
        "name": "joke_response",
        "strict": "true",
        "schema": {
          "type": "object",
          "properties": {
            "joke": {
              "type": "string"
            }
          },
        "required": ["joke"]
        }
      }
}

# Function to handle non-streaming responses
def get_response(model, messages):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=False,
        n=1,
        frequency_penalty=0,
        presence_penalty=0,
        seed=12345,
        top_p=0.1,
        max_tokens=5000,
        response_format=response_format
    )
    return response.choices[0].message.content

# Example messages
messages = [
    {"role": "system", "content": "Analyze the following sentence."},
    {"role": "user", "content": "Design an oscillator of 1MHz?"}
]

response = get_response(model, messages)
print(response)
