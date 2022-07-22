sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict.update({ 'location': 'New York' })    ##Adding the new entry 
sample_dict.pop('city')                         ## Deleting the entry

print(sample_dict)