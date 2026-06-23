age = int(input("Enter your age--->"))
num_ticket = int(input("Enter the number of-->"))
price = int(input("Enter the price of single ticket-->"))
if age<18:
    total_price = price*(50/100)
    after_discount = price-total_price
    final_price = after_discount*num_ticket
    print("final bill after discount..",final_price)
else:
    final_price1 = price*num_ticket
    print("final bill...",final_price1)
