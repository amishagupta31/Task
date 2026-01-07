weather = [
    {"day": "Mon", "temp": 32, "rain": False},
    {"day": "Tue", "temp": 35, "rain": True},
    {"day": "Wed", "temp": 30, "rain": False}
]

hottest = max(weather, key=lambda x: x["temp"])["day"]
avg_temp = sum(w["temp"] for w in weather) / len(weather)
rainy_days = sum(1 for w in weather if w["rain"])

summary = {
    "hottest_day": hottest,
    "average_temp": avg_temp,
    "rainy_days": rainy_days
}

print(summary)
