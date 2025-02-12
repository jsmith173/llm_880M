import json

# Open the text file in read mode
with open('output.txt', 'r') as file:
    # Read all lines and store them in a list
    lines = file.readlines()

m = 0
js = json.loads('{}')
js['models'] = []
for line in lines:
    if line.find('PARAMS') >= 0:
        m += 1
    elif m == 1 and line.strip():
        s_list = line.split()
        js['models'].append(s_list[0])       

json_data = json.dumps(js, ensure_ascii=False, indent=4)
with open('ls_models.json', 'w', encoding='utf-8') as file:
    file.write(json_data)

a=1
