A ={
    "A":12,
    "B":13,
    "C":45
}
B={
    "A":12,
    "B":34,
    "C":54
}
equ = A == B
print(equ)

for i in A.keys():
    for j in B.keys():
        if i==j:
            print(f"{i} equal {j}")
        else:
            print(f"{i} not equal {j}")

for i in A.values():
    for j in B.values():
        if i==j:
            print(f"{i} equal {j}")
        else:
            print(f"{i} not equal {j}")