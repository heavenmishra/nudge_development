from utility import *

with open("d:\\CI_CDdemo\\event_deployment\\test_1\\test2.ipynb","r") as file:
    raw_content = file.read()
    file.close()

content = convert_from_json(raw_content)
final_content = filterout(content)

for i in final_content:
    print(i)