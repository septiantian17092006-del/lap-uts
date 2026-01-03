from utils import parse_nilai, cari_terbesar, cari_terkecil

data = input("Masukkan nilai: ")

nilai = parse_nilai(data)

nilai_terbesar = cari_terbesar(nilai)
nilai_terkecil = cari_terkecil(nilai)

print("Daftar nilai:", nilai)
print("Nilai terbesar:", nilai_terbesar)
print("Nilai terkecil:", nilai_terkecil)