def duplicate(my_list):
    my_list.extend(my_list)


l = [1, 2]
duplicate(l) 
print l # [1, 2, 1, 2]