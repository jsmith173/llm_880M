import subprocess
import os,json

INP = 'json_inp.json'
if os.path.exists(INP):
	with open(INP, 'r', encoding='utf-8') as f:
		js_inp = json.load(f)
else:
	js_inp = json.loads('{}')
	js_inp['cmd'] = 'LS'
	json_data = json.dumps(js_inp, ensure_ascii=False, indent=4)
	with open('js_test.json', 'w', encoding='utf-8') as file:
		file.write(json_data)

if js_inp['cmd'] == 'LS':
	# Run the 'lms ls --json' command
	result = subprocess.run(['lms', 'ls', '--json'], capture_output=True, text=True)

	# Store the output in a string
	output_str = result.stdout

	# Parse the JSON output
	output_json = json.loads(output_str)

	json_data = json.dumps(output_json, ensure_ascii=False, indent=4)
	with open('ls_models.json', 'w', encoding='utf-8') as file:
		file.write(json_data)

elif js_inp['cmd'] == 'LOAD':
	result = subprocess.run(['lms', 'load', js_inp['model']], capture_output=True, text=True)
	output_str = result.stdout
	output_lines = output_str.splitlines()

	# Write the lines to a file
	with open('ls_cmd.txt', 'w') as file:
		for line in output_lines:
			file.write(line + '\n')
