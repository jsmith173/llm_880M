import subprocess
import json

# Run the 'lms ls --json' command
result = subprocess.run(['lms', 'ls', '--json'], capture_output=True, text=True)

# Store the output in a string
output_str = result.stdout

# Parse the JSON output
output_json = json.loads(output_str)

json_data = json.dumps(output_json, ensure_ascii=False, indent=4)
with open('ls_models.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
