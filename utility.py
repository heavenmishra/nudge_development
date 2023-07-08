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

def filterout(content):
    final_content=[]
    content_lst=content.split("\n\n")
    for i in content_lst:
        if "spark.sql(\"\"\"" in i and "\"\"\"" in i:
            final_content.append(i)
    return final_content

def extract_query(final_content):
    
    pass
# def generate_path():
#     current_path=os.getcwd()
#     return current_path