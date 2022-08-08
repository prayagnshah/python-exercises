import json

data = {"key1": "value1", "key2": "value2", "key3": 3}

##double quotation is formed once they are converted into json format
##dumps() function used to convert dictionary into Json
jsonData = json.dumps(data)

print(jsonData)
