from openai import OpenAI
import json,time

model = "DesignSoft/TINA_AI2_Q4"
#model = "llama-3.2-3b-instruct_4tina2"

port=11434
#port=1234

max_tokens=2100

# Set up the OpenAI client
client = OpenAI(
    base_url=f'http://127.0.0.1:{port}/v1',
    api_key='ollama'  # required, but unused
)

# Function to handle streaming responses
def stream_response(model, messages):
	response = client.chat.completions.create(
		model=model,
		messages=messages,
		stream=True,  # Enable streaming mode
		n=1,
		frequency_penalty=0,
		presence_penalty=0,
		top_p=0.1,
		max_tokens=max_tokens
	)
	for chunk in response:
		content = chunk.choices[0].delta.content
		print(content, flush=True, end='')

# Example messages
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Tell me the history of France in 1000 words"}
]

start_time = time.time()
stream_response(model, messages)
end_time = time.time()
elapsed_time = end_time-start_time

# Calculate minutes and remaining seconds
elapsed_minutes = int(elapsed_time // 60)
remaining_seconds = elapsed_time % 60

# Print both minutes and seconds
print(f"\n>> {elapsed_minutes} min {remaining_seconds:.1f} s")

