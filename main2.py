from utils import parse_harga, hitung_total_harga

# Input harga barang dari pengguna
data = input("Masukkan harga barang (pisahkan dengan koma): ")

# Mengubah input menjadi list harga
harga_barang = parse_harga(data)

# Menghitung total harga barang
total_harga = hitung_total_harga(harga_barang)

# Menampilkan hasil
print("Daftar harga barang:", harga_barang)
print("Total harga barang:", total_harga)
