#immurtable_var = 1, 2, 3, 4
#immurtable_var2 = (1, 2, 3, 4)
#immurtable_var3 = tuple([1, 2, 3, 4])
#print(type(immurtable_var))
#print(immurtable_var2)
#print(immurtable_var3)

#immurtable_var4 = 1, 2, 3, True, "String"
#print(immurtable_var4)
#immurtable_var4[0] = 200
#print(immurtable_var)

mutable_list = ([1, 2], 0)
print(mutable_list)
mutable_list[0][0] = 2
print(mutable_list)
mutable_list = (1, 2) * 3
print(mutable_list)