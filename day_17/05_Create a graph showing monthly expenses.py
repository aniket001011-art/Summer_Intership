import matplotlib.pyplot as plt
monthly={
    "Travel_cost":int(input("Enter the monthly travel expenses..")),
    "Food_cost":int(input("Enter the monthly food expenses..")),
    "money_save":int(input("Enter the monthly saving..")),
    "other_expenese":int(input("Enter the other monthly expenses..")),
}
print(monthly)
sizes = list(monthly.values())
labls = list(monthly.keys())
plt.pie(sizes, labels=labls, startangle=90)
plt.show()