list1=input("\n Enter the first string--",)
list2=input("\n Enter the second string--",) 
# print(list1.lower())
# list1= sorted(list1.lower())
# list2= sorted(list2.lower())
# print(list1)
# print(list2)
# a = list1==list2[::-1]
# print(a)
def is_anagram(string1,string2):
    if (sorted(string1.lower())== sorted(string2.lower())):
        return True
    else:
        return False
# list1=input("\n Enter the first string--",)
# list2=input("\n Enter the second string--",)    
a = is_anagram(list1,list2)
print("\n the answers is--",a)