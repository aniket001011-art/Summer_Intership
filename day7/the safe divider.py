def safe_divide():
    try:
        num1 = input("Enter the first input-->")
        num2 = input("Enter the second input-->")
        ab = float(num1)/float(num2)
        print(ab)
    except ZeroDivisionError:
        print("Error: cannot divide by zero!")
    except ValueError:
        print("Error: Please enter numbers only!")
x = safe_divide()
print(x)