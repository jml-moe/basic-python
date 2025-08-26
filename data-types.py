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

#tuple -> immutable, fixed size; often used for fixed collections of items, such as coordinates
coordinates = (10.0, 20.0) 

#print(my_hobbies)

#Range -> bisa kita ubah menjadi list
my_range = range(5)
my_list = list(my_range)
# print(list(my_range)) # > [0, 1, 2, 3, 4]
"""print(my_list)
print(my_range)"""

#Dict -> Key-Value pairs data -> mirip dengan object -> bisanya dibuat ketika punya set of value dengan entitas tertentu ex: transaksi, data user
# user = {}

# Membuat dictionary
my_info = {
    "name": "Jamil",
    "age": 21,
    "height": 159.5,
    "is_handsome": True,
    "hobbies": ["Reading", "Coding", "Sleeping"]
}

# Mengakses nilai dengan kunci
print(my_info["name"])        # Jamil
print(my_info["hobbies"][0])  # Reading

# Mengubah nilai
my_info["age"] = 22

# Menambah pasangan kunci-nilai baru
my_info["address"] = "Malang, Jawa Timur"

# Menghapus pasangan kunci-nilai
del my_info["is_handsome"]

# Method dictionary
print(my_info.keys())    # Menampilkan semua kunci
print(my_info.values())  # Menampilkan semua nilai
print(my_info.items())   # Menampilkan pasangan (kunci, nilai)

# Mengecek keberadaan kunci
if "name" in my_info:
    print("Ada nama di dictionary")
    
# Mengambil nilai dengan get() (lebih aman, tidak error jika kunci tidak ada)
# Example showing how get() works with default values
user1 = {"name": "John", "age": 30}
user2 = {"name": "Sarah", "age": 25, "address": "New York"}

# For user1, "address" key doesn't exist, so it returns the default value
print(user1.get("address", "Tidak ada alamat"))  # Output: Tidak ada alamat

# For user2, "address" key exists, so it returns the actual value
print(user2.get("address", "Tidak ada alamat"))  # Output: New York

# x = {1, 2, 3, 1, 3, 2, 4}
# y = {2, 4, 7, 2, 8}
# z = {2, 10, 8, 3, 4, 12, 12}
# print(z - (x & y))  