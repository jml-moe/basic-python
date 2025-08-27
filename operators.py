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
