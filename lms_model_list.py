import subprocess
import json

# Run the 'lms list' command
result = subprocess.run(['lms', 'ls'], capture_output=True, text=True)

# Store the output in a string
output_str = result.stdout

# Split the output into lines and store them in an array
output_lines = output_str.splitlines()

m = 0
js = json.loads('{}')
js['models'] = []
for line in output_lines:
    if line.find('PARAMS') >= 0:
        m += 1
    elif m == 1 and line.strip():
        s_list = line.split()
        js['models'].append(s_list[0])       

json_data = json.dumps(js, ensure_ascii=False, indent=4)
with open('ls_models.json', 'w', encoding='utf-8') as file:
    file.write(json_data)
