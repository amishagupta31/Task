students = [
    ("Ajay", [78, 85, 90]),
    ("Kumar", [65, 70, 60]),
    ("Rahul", [88, 92, 95])
]

result = {}
topper = ""
highest_avg = 0

for name, marks in students:
    avg = sum(marks) / len(marks)

    if avg >= 85:
        status = "Distinction"
    elif avg >= 50:
        status = "Pass"
    else:
        status = "Fail"

    result[name] = {"average": round(avg, 2), "status": status}

    if avg > highest_avg:
        highest_avg = avg
        topper = name

print(result)
print("Topper:", topper)
