import json

sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}

##using dumps function to print dictionary with the spacing of two and having "," signs in between
data = json.dumps(sampleJson, indent=2, separators=(",", "="))

print(data)
