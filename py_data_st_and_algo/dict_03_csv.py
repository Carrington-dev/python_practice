import csv

context = {
    "name": "Carrington",
    "surname":"Muleya",
    "age":"25",
}

with open("students.csv", "w") as f:
    writter = csv.writer(f)

    for key, value in context.items():
        writter.writerow([key, value])