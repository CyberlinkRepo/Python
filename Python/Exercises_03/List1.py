my_list = [1,2,3,4,"A"]
a = len (my_list)
print(a)
slice_1 = my_list[1:3:1]
print(slice_1)
my_character = my_list[-1]
print(my_character)




my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatentated_list = my_list_1 + my_list_2
print(concatentated_list)


my_list_1 = [1,2,3,4,"A"]
my_list_2 = ["S","T","Fish",9,10]
concatentated_list = [my_list_1, my_list_2]
print(concatentated_list)



my_list_1 = ["S","T","Fish",9,10]
print (my_list_1)
my_list_1[2] = "Chips"
print(my_list_1)



my_list = ["One","Two","Three"]
print (my_list)
my_list.append("Four")
print(my_list)



my_list = ["One","Two","Three"]
my_tuple = ("one", "two", "three")
print(type(my_list))
print(type(my_tuple))



my_tuple = ("One","Two","Three", "One")
# How many times does "One" appear in the tuple
print(my_tuple.count("One"))
# At what position in the tuple can I first find "One"
print(my_tuple.index("One"))


my_tuple = ("One","Two","Three", "One")
# How many times does "One" appear in the tuple
print(my_tuple.count("One"))
# At what position in the tuple can I first find "One"
print(my_tuple.index("Two"))



my_tuple = ("One","Two","Three", "One")
# How many times does "One" appear in the tuple
print(my_tuple.count("One"))
# At what position in the tuple can I first find "One"
print(my_tuple.index("Two"))