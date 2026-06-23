# list=["Banana", "Orange", "Apple"]
# def contains_item(target_list,item_to_find ):
#     if item_to_find in target_list:
#         return True
#     else:
#         return False
# q=contains_item(list,"Apple")
# print(q)

list=["Banana", "Orange", "Apple"]
def contains_item(target_list,item_to_find ):
    for i in list:
        if item_to_find in target_list:
          return True
        else:
          return False
q=contains_item(list,"Apple")
print(q)