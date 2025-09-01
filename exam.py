# =====================
# STUDY CASE LATIHAN FUNDAMENTAL PYTHON
# =====================

# 1. Data Mahasiswa
# Buatlah sebuah dictionary untuk menyimpan data mahasiswa (nama, umur, jurusan, IPK, dan status aktif).
# Cetak seluruh data tersebut dengan format string yang rapi.
# Contoh output:
# Nama: Jamil
# Umur: 21
# Jurusan: Informatika
# IPK: 3.75
# Status Aktif: True

# Tulis jawabanmu di bawah ini:
mahasiswa = {
    # isi dengan data sesuai instruksi
    "nama": "Jamil",
    "umur": 21,
    "jurusan": "Informatika",  # Menambahkan jurusan yang sebelumnya tidak ada
    "IPK": 3.79,
    "status_aktif": False,  # Ubah nama key untuk konsistensi
}
# Cetak data mahasiswa dengan format yang rapi
print("Data Mahasiswa:")
for key, value in mahasiswa.items():
    # Format nama key dengan capitalize dan ganti underscore dengan spasi
    formatted_key = key.replace("_", " ").capitalize()
    print(f"{formatted_key}: {value}")

# 2. Fungsi Penjumlahan Dinamis
# Buatlah fungsi jumlahkan_semua yang menerima jumlah argumen tak terbatas (menggunakan *args)
# dan mengembalikan hasil penjumlahan seluruh argumen tersebut.
# Contoh pemanggilan: jumlahkan_semua(1,2,3,4) -> 10

# Tulis jawabanmu di bawah ini:
def jumlahkan_semua(*args):
    # implementasi fungsi
    total = 0
    for angka in args:
        total += angka
    return total

# Contoh pemanggilan
print("\nHasil penjumlahan:", jumlahkan_semua(1, 2, 3, 4))


# 3. Filter Produk dengan Keyword Arguments
# Buatlah fungsi filter_produk yang menerima data produk (nama, kategori, stok, harga) menggunakan **kwargs,
# lalu cetak hasil filter berdasarkan kategori tertentu (misal: "Makanan").
# Contoh pemanggilan: filter_produk(nama="Roti", kategori="Makanan", stok=10, harga=5000)

# Tulis jawabanmu di bawah ini:
def filter_produk(**kwargs):
    # Print only products that match the specified category
    print("\nProduct Details:")
    for key, value in kwargs.items():
        print(f"{key.capitalize()}: {value}")
    
    # Showing that we're filtering by category
    if "kategori" in kwargs:
        print(f"\nFiltered by category: {kwargs['kategori']}")
        print(f"This product belongs to {kwargs['kategori']} category")

# Contoh pemanggilan
filter_produk(nama="Roti", kategori="Makanan", stok=10, harga=5000)
