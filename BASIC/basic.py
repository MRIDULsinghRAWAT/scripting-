#variables 
name="don"
age=31
print(name)
print(age)
#-----------------------------------------------------------
#data  types
name="don"
age=31
print(type(name))
print(type(age))
#-----------------------------------------------------------
#list
my_list=[1,2,3,4,5]
print(my_list)
print(type(my_list))
#-----------------------------------------------------------
#tuple
my_tuple=(1,2,3,4,5)
print(my_tuple)
print(type(my_tuple))

# diff btw list and tuple
#list is mutable and tuple is immutable

#set
my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))  

#dictionary
my_dict={"name":"don","age":31}  # why colon ? becoz dictionary is key value pair -
#means-  key is name and value is don, key is age and value is 31
print(my_dict)
print(type(my_dict))

# set and dictionary are unordered collection of data types
#difference- set contains unique elements while dictionary contains key-value pairs

# difference between list, tuple, set and dictionary
#list- ordered, mutable, allows duplicate elements
#tuple- ordered, immutable, allows duplicate elements
#set- unordered, mutable, does not allow duplicate elements
#dictionary- unordered, mutable, does not allow duplicate keys


# input output 
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Your name is", name)
print("Your age is", age)