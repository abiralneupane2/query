import json

from src.create_db import engine
from src.query import Query



# read the json file
f = open("query.json")
input_data=json.loads(f.read())
query_object=Query(input_data)


# evaluate and print the query
query_object.evaluate()

# uncomment following lines to display the data
# result = query_object.execute(engine)
# for row in result:
#     print(row)


print(str(query_object.q))









