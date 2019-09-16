import csv

f = open('csv-files/file_name.csv', 'r', encoding='utf-8')

rdf = csv.reader(f)

for line in rdf:
  print(line)

f.close()