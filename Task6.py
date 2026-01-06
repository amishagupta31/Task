transactions = [
    {"id": 1, "amount": 500, "location": "Chennai"},
    {"id": 2, "amount": 45000, "location": "Delhi"},
    {"id": 3, "amount": 52000, "location": "Chennai"},
    {"id": 4, "amount": 200, "location": "Coimbatore"}
]

visited_locations = set()
suspicious = []

for tx in transactions:
 
    if tx["amount"] > 50000:
        suspicious.append(tx)
 
    if visited_locations and tx["location"] not in visited_locations:
        suspicious.append(tx)

    visited_locations.add(tx["location"])
 
suspicious = list({tx["id"]: tx for tx in suspicious}.values())

print(suspicious)
