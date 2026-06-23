def calculate_total(price, tax_rate=0.05):
    total_cost = price + (price * tax_rate)
    return (total_cost)
print(calculate_total(1000))