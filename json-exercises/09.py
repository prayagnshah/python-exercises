import json

sampleJson = [
    {"id": 1, "name": "name1", "color": ["red", "green"]},
    {"id": 2, "name": "name2", "color": ["pink", "yellow"]},
]

contents = []

try:
    with open("sampleJson.json", "r") as file:
        contents = json.load(file)
except Exception as e:
    print(e)
