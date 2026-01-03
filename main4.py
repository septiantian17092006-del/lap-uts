from utils import parse_harga, hitung_total, hitung_diskon

# Input harga barang
data = input("Masukkan harga barang (pisahkan dengan koma): ")

# Mengubah input menjadi list harga
harga_barang = parse_harga(data)

# Menghitung total harga
total_harga = hitung_total(harga_barang)

# Menghitung diskon
diskon = hitung_diskon(total_harga)

# Menghitung total bayar
total_bayar = total_harga - diskon

# Menampilkan hasil transaksi
print("Daftar harga barang:", harga_barang)
print("Total harga: Rp", total_harga)
print("Diskon: Rp", int(diskon))
print("Total bayar: Rp", int(total_bayar))
