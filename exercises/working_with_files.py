with open('llc-chapters.csv') as chapters_file:
    print(chapters_file.read())


import csv
with open('llc-chapters.csv') as chapters_file:
     chapters_data = csv.DictReader(chapters_file)
     chapter = next(chapters_data)
     print(chapter['Province'])
