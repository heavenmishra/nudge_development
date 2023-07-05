import json
import os

def convert_from_json(raw_content):
    y=json.loads(raw_content)
    content=""
    for i in y['cells']:
        for j in i["source"]:
            content = content + j
        content=content+'\n\n'
    return content.strip()

def generate_path():
    current_path=os.getcwd()
    return current_path