list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

list1[2][1][2].extend(["h", "i", "j"])   ##use the indexing and then tried to insert new chars 
print(list1)