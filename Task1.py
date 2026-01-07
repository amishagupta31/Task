logs = [
    "2026-01-02 10:15:32 ERROR Database connection failed",
    "2026-01-02 10:16:10 INFO User logged in",
    "2026-01-02 10:17:45 ERROR Database connection failed",
    "2026-01-02 10:18:00 WARNING Disk space low"
]

result = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_messages = {}

for log in logs:
    parts = log.split()
    level = parts[2]
    message = " ".join(parts[3:])

    result[level] += 1

    if level == "ERROR":
        error_messages[message] = error_messages.get(message, 0) + 1

# most frequent error
result["most_common_error"] = max(error_messages, key=error_messages.get)

print(result)
