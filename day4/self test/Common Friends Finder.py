list1=list(input("Enter the first list of frends--"))
list2=list(input("Enter the second list of frends--"))
print(list1)
print(list2)
def find_common_friends(user1_friends,user2_friends):
    if user1_friends in user2_friends:
        