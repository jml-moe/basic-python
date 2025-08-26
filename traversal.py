# Manipulasi -> perubahan dalam sebuah value ex: ketika concatenation sebuah value 

first_name = "jamil"
last_name = "moe"

fullname = first_name + " " + last_name # concatenation

print(fullname)
print(fullname.capitalize()) # manipulasi
print(fullname.upper()) # manipulasi -> upper case

# f-string
my_name = f"my name is {fullname}"

print(my_name)

my_prompt = """
the first line.
the second line.

{fullname}
"""

print(my_prompt)  # Mencetak string mentah dengan placeholder {fullname} tanpa perubahan
print(my_prompt.format(fullname=fullname))  # Mencetak string setelah mengganti {fullname} dengan nilai fullname yang sebenarnya


#traversal bisa ubah float ke int pun sebaliknya
my_age = 20
my_ipk = 3.79

print(float(my_age))
print(int(my_ipk))

#list 
my_fruits = ["apple", "durian", "mango"]
my_fruits.append("lemon")

print(my_fruits)

#tuple -> bisa di unpack (destructuring)
a, b = 0,1
print(a,b)

#dictionary -> bisa di get
user = {
    "name" : "Jamil",
    "age" : 20,
    "hobby" : "reading"
}

user["is_student"] = True
print(user.get("height", "-")) #set default value
print(user)