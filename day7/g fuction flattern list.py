list1 = [[1],[2,3],[4],[5,6]]
def fattern_list():
    for i in list1:
        for j in i: 
          if type(j)== list:
             for k in j:
                yield k
          else:
             yield j

x = fattern_list()
for y in x:
    print(y)