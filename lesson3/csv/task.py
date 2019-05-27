
import csv

out_file = "users_list.csv"
delim = ";"

users_list = [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]

with open(out_file, "a", encoding="utf-8") as f:
    fields = ["name", "age", "job"]
    writer = csv.DictWriter(f, fields, delimiter=delim)
    writer.writeheader()

    for user in users_list:
        writer.writerow(user)


