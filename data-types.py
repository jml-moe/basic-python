#numeric data types

#integer (whole number)
my_age = 21

#float (decimal)
my_phi = 3.14

result = my_age + my_phi # > float
# print(result)

#string (text)
my_name = "Jamil"
my_address = """
Malang, Jawa Timur
Indonesia
""" # > multiline string

# print(my_address)

#Boolean -> True/False  untuk control flow
is_jamil_handsome = True
is_jamil_rich = False

#SEQUENCE -> list of items

#list -> mutable, non-fixed size
my_hobbies = ["Reading", "Gaming", "Cooking"]
my_hobbies.append("Traveling")

#tuple -> immutable, fixed size
coordinates = (10.0, 20.0) 

#print(my_hobbies)

#Range -> bisa kita ubah menjadi list
my_range = range(5)
my_list = list(my_range)
# print(list(my_range)) # > [0, 1, 2, 3, 4]
print(my_list)
print(my_range)
