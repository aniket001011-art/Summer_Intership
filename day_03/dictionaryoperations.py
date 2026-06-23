d1={
    "Name":"Aniket",
    "Age":21
}
d2={
    "Name":"Ani",
    "Age":22
}
#add new key value
d1["location"]="chandigarh"
print("\n",d1)

print("\n",d1["Name"])

d1["Age"]=22
print("\n",d1)
print("\n",d1.items())
print("\n",d1.keys())
print("\n",d1.values())

d1.pop("Age")
print("\n",d1)


fruits={
    "apple":50,
    "mangoo":10,
    "orange":4
}
print(fruits)
for keys,value in fruits.items():
    if value>=10:
        print(f"aleart {keys} is max")
    else:
        pass

 