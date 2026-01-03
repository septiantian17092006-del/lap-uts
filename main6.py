from utils import parse_harga, hitung_total, hitung_pajak, format_rupiah

# Input harga barang
data = input("Masukkan harga barang (pisahkan dengan koma): ")

# Proses data
harga_barang = parse_harga(data)
total_harga = hitung_total(harga_barang)
pajak = hitung_pajak(total_harga)
total_bayar = total_harga + pajak

# Output
print("Daftar harga barang:", harga_barang)
print("Total harga :", format_rupiah(total_harga))
print("Pajak       :", format_rupiah(pajak))
print("Total bayar :", format_rupiah(total_bayar))
