#different type of sets in python
# set ofintegers
my_set = {1 ,2 ,3}
print(my_set)

# set fof mixed datatypes
my_set = {1.0, "hello", (1,2,3)}
print(my_set)

# set cannot have duplicates
my_set = {1,2,3,4,3,2}


#we can make set from a list
my_set = set[1,2,3,2]
print(my_set,"/n")


# remove a number from a set
num_set =set ([0,1,3,4,5])
print("original set:")
print(num_set)
num_set.pop()
print("after removing the first element from the said set:")
print(num_set,"/n")
