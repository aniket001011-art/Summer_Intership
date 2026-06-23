A={
    "a":20,
    "b":36,
    "c":45,
    "d":3
}

print(max(A.values()))

for keys,Value in A.items():
    if Value == max(A.values()):
        print(f"{keys} it is the max value")
    else:
        pass