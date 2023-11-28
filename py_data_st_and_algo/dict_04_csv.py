import csv
labels = ['name', 'surname', 'age']

context = [
    {
    "name": "Carrington",
    "surname":"Muleya",
    "age":"25",
    },
    {
    "name": "Chalmers",
    "surname":"Muleya",
    "age":"15",
    },
    {
    "name": "Avhurengwi",
    "surname":"Muleya",
    "age":"16",
    },
    {
    "name": "Rendani",
    "surname":"Muleya",
    "age":"11",
    },
    {
    "name": "Ndivhuwo",
    "surname":"Muleya",
    "age":"10",
    },
    {
    "name": "Portia",
    "surname":"Muleya",
    "age":"23",
    },

]

with open("students2.csv", "w") as f:
    # writter = csv.writer(f)
    writer = csv.DictWriter(f, fieldnames=labels)
    writer.writeheader()
    for elem in context:
            writer.writerow(elem)


    # for item in context:
    #     writter.writerow(item)

print("Done!!!!")
    # for key, value in context.items():
    #     writter.writerow([key, value])