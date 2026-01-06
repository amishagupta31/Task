employees = [
    {"name": "Ajay", "age": 22, "salary": 25000},
    {"name": "Rahul", "age": 25, "salary": 40000},
    {"name": "Kiran", "age": 21, "salary": 30000}
]

 
print(sorted(employees, key=lambda x: x["salary"], reverse=True))

 
print(sorted(employees, key=lambda x: (x["age"], x["salary"])))

 
def sort_employees(data, keys):
    return sorted(data, key=lambda x: tuple(x[k] for k in keys))

print(sort_employees(employees, ["age", "salary"]))
