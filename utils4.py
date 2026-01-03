# Mengubah input harga menjadi list angka
def parse_harga(data):
    return list(map(int, data.split(",")))

# Menghitung total harga
def hitung_total(harga):
    return sum(harga)

# Menghitung diskon (0,1% jika total > 50)
def hitung_diskon(total):
    if total > 50:
        return total * 0.1   # 0,1%
    else:
        return 0
