system_ports = (80,443,8080,443)
print("\n The total number of time 443 is appears--",system_ports.count(443))

system_ports=list(system_ports)
system_ports.append(33)
system_ports= tuple(system_ports)
print("\nAfter adding 33 with append--",system_ports)

# direct 
system_ports=system_ports+(22,)
print("After adding 22 witout append--",system_ports)
