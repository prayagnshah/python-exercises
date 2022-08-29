# import matplotlib.pyplot as plt

# x = [24,35,67]
# y = [45,34,23]

# plt.plot(x,y)

# plt.show()

from sqlite3 import DataError, requests
import json

response = requests.get("http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow")

# print(response.json()['items']['task'])

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['link'])
        print(data['title'])
    else:
        print('skipped')
    print()
    