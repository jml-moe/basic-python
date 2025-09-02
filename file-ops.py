"""
# Sintaks dasar
file = open('namafile.txt', 'mode')
 
# Mode yang umum digunakan:
# 'r' - Read/Baca (default)
# 'w' - Write/Tulis (menimpa file)
# 'a' - Append/Tambah (menambah di akhir file)
# 'x' - Exclusive creation/Pembuatan eksklusif
# 'b' - Binary mode/Mode biner
# 't' - Text mode/Mode teks (default)
 
# Menggunakan with statement (direkomendasikan)
with open('namafile.txt', 'r') as file:
    # operasi file di sini
    pass  # file otomatis tertutup setelah blok selesai
"""


with open("data.txt", "w") as file:
    file.write("Heloo geyztt")