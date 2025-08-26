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


