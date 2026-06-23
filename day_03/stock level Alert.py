inventory={
    "apples":50,
    "bananas":4,
    "oranges":12,
    "mangoes":2
}
for key, value in inventory.items():
    if value<=10:
        print(f"Alert: {key} is running low!")
    else:
        pass