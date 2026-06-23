def register_voter():
    age = int(input("Enter your age...."))
    if age<0:
        raise ValueError("Age Cannot be negative!")
    if age<=18:
        raise ValueError("Must be 18 or older to vote")
    print("Registration successful!")
x = register_voter()
print(x)