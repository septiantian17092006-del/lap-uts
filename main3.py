from utils import parse_nilai, tentukan_kelulusan

# Input nilai dari pengguna
data = input("Masukkan nilai (pisahkan dengan koma): ")
nilai_kelulusan = int(input("Masukkan nilai kelulusan: "))

# Mengubah input menjadi list nilai
nilai = parse_nilai(data)

# Menentukan kelulusan
rata_rata, status = tentukan_kelulusan(nilai, nilai_kelulusan)

# Menampilkan hasil
print("\n=== HASIL ===")
print("Daftar nilai        :", nilai)
print("Rata-rata nilai     :", round(rata_rata, 2))
print("Nilai kelulusan     :", nilai_kelulusan)
print("Status kelulusan    :", status)
