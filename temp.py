import csv

data = csv.DictReader(open('sample.csv'))
my_list = list(data)

for i in my_list: print(i)