# Mengubah input menjadi list nilai
def parse_nilai(data):
    return list(map(int, data.split(",")))

# Menentukan kelulusan berdasarkan nilai minimum
def tentukan_kelulusan(nilai, nilai_kelulusan):
    rata_rata = sum(nilai) / len(nilai)

    if rata_rata >= nilai_kelulusan:
        status = "LULUS"
    else:
        status = "TIDAK LULUS"

    return rata_rata, status
