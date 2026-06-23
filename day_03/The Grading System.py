score = int(input("\n Enter the score--"))
if score >= 90:
    print("\n the overall Grade of the student = A")
elif score in range(80,90):
    print("\n the overall Grade of the student = B")
elif score in range(70,80):
    print("\n the overall Grade of the student = C")
else:
    print("\n the overall Grade of the student= F")