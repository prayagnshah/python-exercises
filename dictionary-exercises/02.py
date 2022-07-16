dict_1 = { 'Ten': 10, 'Twenty' : 20, 'Thirty' : 30 }
dict_2 = {'Thirty': 30, 'Fourty' : 40, "Fifty": 50}


# dict_4 = dict_1.update({'Thirty': 30, 'Fourty' : 40, "Fifty": 50})

dict_3 = {**dict_1, **dict_2}   ##using the operator ** to merge the two variables 



print(dict_3)




