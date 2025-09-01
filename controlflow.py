# mengatur arah dari sebuah program (if-else)

# struktur dasar if-else
"""
if kondisi:
    # blok kode jika kondisi benar
else:
    # blok kode jika kondisi salah  
"""
grade = 95

if grade > 90:
    print(f"Nilai anda {grade}, anda berhak mendapat grade A")
else:
    print(f"Nilai anda {grade}, anda berhak mendapat grade C")


def screentime_checker(screentime):
    if screentime > 8:
        print("Istirahat Sekarang!")
    elif screentime < 5 and screentime > 6:
        print("Jangan lupa istirahat")
    else:
        print("Masih Normal")
screentime_checker(1)
        
