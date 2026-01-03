# Mengubah input menjadi list harga
def parse_harga(data):
    return list(map(int, data.split(",")))

# Menghitung total harga
def hitung_total(harga):
    return sum(harga)

# Menghitung pajak (0,1% jika total > 50
def hitung_pajak(total):
    if total > 50:
        return total * 0.001
    else:
        return 0

# Format angka ke Rupiah
def format_rupiah(angka):
    return "Rp {:,.0f}".format(angka).replace(",", ".")
