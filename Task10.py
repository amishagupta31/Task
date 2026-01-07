attendance = [
    ("Ajay", "2026-01-01", "Present"),
    ("Ajay", "2026-01-02", "Absent"),
    ("Rahul", "2026-01-01", "Present")
]

from collections import defaultdict

records = defaultdict(list)

for name, date, status in attendance:
    records[name].append(status)

for name, logs in records.items():
    total = len(logs)
    present = logs.count("Present")
    percent = (present / total) * 100
    print(f"{name}: {percent:.2f}%")

    if percent < 75:
        print(f"⚠ {name} below 75%")


    streak = max_streak = 0
    for s in logs:
        if s == "Present":
            streak += 1
            max_streak = max(max_streak, streak)
        else:
            streak = 0
    print("Longest Present Streak:", max_streak)
