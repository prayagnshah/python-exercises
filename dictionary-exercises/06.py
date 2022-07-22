sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]

for k in keys:   #iterate the keys
    sample_dict.pop(k)    #using pop function to remove the desired keys
    
print(sample_dict)
    

   