str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", "", False]

## in filter(function, iterable) as this only works for list
str_new = list(filter(None, str_list))

print(str_new)
