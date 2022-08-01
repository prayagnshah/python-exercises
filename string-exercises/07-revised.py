s1 = "Yn"
s2 = "PYnative"


set1 = set(s1)
set2 = set(s2)

sets_union = set1.union(set2)


##using this expression to print boolean expression
is_subset = sets_union == set2

print(is_subset)
