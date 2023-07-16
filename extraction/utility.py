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
    with open("raw_content.txt" , "w") as files:
        files.write(content)

    with open("raw_content.txt","r") as files:
        final_content = files.readlines()

    if os.path.exists("raw_content.txt"):
        os.remove("raw_content.txt")
    else:
        print("file does not exist:")
    
    content_starting_point=0
    for i in range(len(final_content)):
        if "spark.sql(\"\"\"" in final_content[i] :
            content_starting_point=i
            break
    block_starting_point=[]
    for i in final_content[content_starting_point:]:
        if "spark.sql(\"\"\"" in i:
            block_starting_point.append(final_content.index(i))

    block_ending_point = block_starting_point[1:].copy()
    block_ending_point.append(len(final_content))
    # print(block_starting_point)
    # print(block_ending_point)
    blocks=[]
    for i in range(len(block_starting_point)):
        blocks.append(final_content[block_starting_point[i]:block_ending_point[i]])

    string_blocks=[]
    for i in blocks:
        strings=''
        for j in i:
            strings= strings + j
        string_blocks.append(strings)
    return string_blocks

def get_(block,starting_tag,ending_tag):
    starting_index = block.index(starting_tag)+len(starting_tag)
    ending_index = starting_index + block[starting_index:].index(ending_tag)
    return block[starting_index:ending_index]

def generate_path():
    current_dir = os.getcwd()
    path_element = current_dir.split("\\")
    path_of_input_file="d:\\"
    for i in path_element[1:-3]:
        path_of_input_file = path_of_input_file +"\\"+i

    path_of_input_file = path_of_input_file +"\\event_deployment\\test_1\\"
    return path_of_input_file

def artifact_content(event_id,event_name,list_of_queries,list_of_tables):
    list_for_artifact=[] #event_id,event_name,query,sequence,intermidate_table,final_table
    for i in range(len(list_of_tables)-1):
        list_for_artifact.append((event_id,event_name,list_of_queries[i],i+1,list_of_tables[i],None))

    list_for_artifact.append((event_id,event_name,list_of_queries[-1],len(list_of_tables),None,list_of_tables[-1]))
    return list_for_artifact