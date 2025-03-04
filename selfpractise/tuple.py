tuple = (12, 21, 34, 43, 50, 'a','b','a')
print(tuple)
tuple_1 = tuple + (65, 72, 85) # This is how we can add new elements in tuple
print(tuple_1)
#we can not remove elements from tuple. we need to convert tuple into list to do so.

my_list = list(tuple)
my_list.remove('a')
print(my_list)