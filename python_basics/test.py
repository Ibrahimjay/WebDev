largest_num = -1
for i in [4,1,4.5,37,4,51]:
    if i > largest_num:
        largest_num = i    
#print(largest_num)


list =  [1,2,3,4,0.2,5,6,7,8,8,9]
list.reverse()
#print(list)
smallest_num = max(list)
for j in list:
    if j <= smallest_num:
        smallest_num = j
        #print(smallest_num) 
print(smallest_num)       


smallest = None
for values in [1,2,3,4,0.2,5,6,7,8,8,9]:
    if smallest is None:
        smallest = values
    elif values < smallest:
        smallest = values
print(smallest)