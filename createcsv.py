import csv
person = [['SN', 'Person', 'DOB'],
['1', 'John', '18/1/1997'],
['2', 'Marie','19/2/1998'],
['3', 'Simon','20/3/1999'],
['4', 'Erik', '21/4/2000'],
['5', 'Ana', '22/5/2001']]
csv.register_dialect('myDialect',
quoting=csv.QUOTE_ALL,
skipinitialspace=True)
with open('person1.csv', 'w') as f:
    writer = csv.writer(f, dialect='myDialect')
    for row in person:
        writer.writerow(row)
f.close()
