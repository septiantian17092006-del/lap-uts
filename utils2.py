   # Fungsi untuk mengubah input menjadi list harga barang
def parse_harga(data):
    return list(map(int, data.split(",")))

# Fungsi untuk menghitung total harga barang
def hitung_total_harga(harga):
    return sum(harga)

