import json

from src.create_db import engine
from src.query import Query

# import src.create_db
# import src.load_data


# read the json file
f = open("query.json")
input_data=json.loads(f.read())
query_object=Query(input_data)




# evaluate and print the query
query_object.evaluate()

# query_object.execute(engine)

query_string = str(query_object.q)

print(query_string)









