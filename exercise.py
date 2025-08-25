first_name = "Jamil"
last_name = "Moe"
age = 21

my_height = 159.5
is_jamil_handsome = True

my_hobbies = ["Reading", "Coding", "Sleeping"]
my_hobbies.append("Writing")

print("Hello my name is " + first_name + " " + last_name)
print(age)
print(my_height)
print(is_jamil_handsome)
print(my_hobbies)

#Python String Concatenation
print("Hello my name is " + first_name + " " + last_name)  # No str() needed as first_name and last_name are likely already strings
print("I am " + str(age) + " years old.")  # age is likely an integer, needs conversion
print("My height is " + str(my_height) + " cm.")  # my_height is likely a float or integer
print("Am I handsome? " + str(is_jamil_handsome))  # is_jamil_handsome is likely a boolean
print("My hobbies are: " + str(my_hobbies))  # my_hobbies is likely a list or other collection

""""Saat menggabungkan string dengan tipe data lain menggunakan +, 
Python memerlukan konversi tipe data secara eksplisit"""

"""
Alternatif modern:
Sebagai alternatif penggunaan str() dengan +, kita dapat menggunakan f-string atau metode format()
"""
# Menggunakan f-string (Python 3.6+) -> lebih mudah dibaca dan efisien
print(f"Hello my name is {first_name} {last_name}")
print(f"I am {age} years old.")
print(f"My height is {my_height} cm.")
print(f"Am I handsome? {is_jamil_handsome}")
print(f"My hobbies are: {my_hobbies}")
