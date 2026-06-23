l1={"a":10,"b":20}
l2={"b":30,"c":40}
A = l1 | l2
print(A)
m=l1.copy()
m.update(l2)
print(m)

m=l2.copy()
m.update(l1)
print(m)