from utility import *

with open("d:\\CI_CDdemo\\event_deployment\\test_1\\test1.ipynb","r") as file:
    raw_content = file.read()
    file.close()

content = convert_from_json(raw_content)
print(content)

print(generate_path())