sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}
# Keys to extract
keys = ["name", "salary"]

my_dict = {}  ##adding data into empty dictionary

for k in keys:
    my_dict[k] = sample_dict[k]  ##matching keys value to our sample dictionary

print(my_dict)
