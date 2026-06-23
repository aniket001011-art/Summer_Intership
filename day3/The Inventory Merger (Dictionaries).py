warehouse_north = {"Laptop": 5, "Mouse": 10}
warehouse_south = {"Keyboard": 8, "Mouse": 15}
total_inventory= warehouse_north.copy()
total_inventory.update(warehouse_south)
print(total_inventory)
