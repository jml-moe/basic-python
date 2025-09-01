# Logical Operator -> boolean
x = False
y = True

print(x and y) # -> True ketika kedua perbandingannya sama2 True 
print(x or y) # True ketika SALAH SATUNYA True -> ex: admin or moderator
print(not x) # -> True ketika Valuenya False -> ex: not user

def check_data(**config):
    username = config.get("username", None)
    if not username:
        raise ValueError("Username is required")
    
# PASTIKAN PAHAM KONSEP, PAHAM PENGGUNAAN, BELAJAR KONSEP JANGAN BELAJAR NGETIK, MUNGKIN SEKARANG BELUM KEBAYANG INI BUAT APA ITU BUAT APA.

# You shall not pass… unless your fundamentals are strong

# addition +
result = 1 + 2
# subtraction -
result = 1 - 2
# multiplication *
result = 1 * 2
# division /
result = 4 / 3
# float division // -> pembagian yang dibulatkan kebawah menjadi integer
result = 4 // 3
# modulus % -> remainder a.k.a value dari sisa bagi 
result = 4 % 3
# exponentiation ** -> pangkat
result = 2 ** 3

# ! Comparison Operators -> membandingkan value dari sebuah variabel
# menghasilkan boolean

# equal
value_a = 4
value_b = 4
print(value_a == value_b)

# not equal
print(value_a != value_b)
# greater than
print(value_a > value_b)
# less than
print(value_a < value_b)
# greater than or equal to
print(value_a >= value_b)
