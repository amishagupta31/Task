inventory = {
    "Laptop": {"price": 60000, "stock": 5},
    "Mouse": {"price": 500, "stock": 50},
    "Keyboard": {"price": 1500, "stock": 20}
}

 
def sell(product, qty):
    if inventory[product]["stock"] >= qty:
        inventory[product]["stock"] -= qty
        print("Sold successfully")
    else:
        print("Insufficient stock")

sell("Laptop", 2)

 
total_value = 0
for item in inventory:
    total_value += inventory[item]["price"] * inventory[item]["stock"]

print("Total Inventory Value:", total_value)

 
print("Low Stock Items:")
for item in inventory:
    if inventory[item]["stock"] < 10:
        print(item)
