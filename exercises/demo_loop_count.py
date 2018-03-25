import csv

with open('llc-chapters.csv') as chapters_file:
    chapters_data = csv.DictReader(chapters_file)

    count = 0
    for row in chapters_data:
        count += 1

    print("There are " + str(count) + " chapters")
