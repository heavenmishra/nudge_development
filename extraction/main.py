from utility import *

input_path = generate_path()
with open(input_path+"test2.ipynb","r") as file:
    raw_content = file.read()
    file.close()

content = convert_from_json(raw_content)
final_content = filterout(content)

# print(final_content)
list_of_queries = []
query_starting_tag = 'spark.sql("""'
query_ending_tag = '""")'
for i in final_content:
    list_of_queries.append(get_(i,query_starting_tag,query_ending_tag))

list_of_tables = []
table_starting_tag = 'createOrReplaceTempView("'
table_ending_tag = '")'
for i in final_content:
    list_of_tables.append(get_(i,table_starting_tag,table_ending_tag))

# print(list_of_queries)
# print(list_of_tables)

# print(artifact_content("0000","Testing",list_of_queries,list_of_tables))