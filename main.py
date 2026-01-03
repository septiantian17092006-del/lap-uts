from utils import *

while True:
    print("\n=== Menu Bangun Datar ===")
    print("1. Segitiga Sama Sisi")
    print("2. Segitiga Sama Kaki")
    print("3. Segitiga Siku-siku")
    print("4. Setengah Lingkaran")
    print("5. Seperempat Lingkaran")
    print("6. Elips")
    print("7. Jajar Genjang")
    print("8. Trapesium Sama Kaki")
    print("9. Pentagon")
    print("10. Heksagon")
    print("11. Lingkaran")
    print("12. Keluar")

    pilih = int(input("\nPilih bangun datar: "))

    if pilih == 1:
        s = float(input("Masukkan sisi: "))
        k, l = segitiga_sama_sisi(s)
        print("Keliling:", k)
        print("Luas:", l)

    elif pilih == 2:
        a = float(input("Masukkan alas: "))
        s = float(input("Masukkan sisi miring: "))
        print("Keliling:", segitiga_sama_kaki(a, s))

    elif pilih == 3:
        a = float(input("Masukkan alas: "))
        t = float(input("Masukkan tinggi: "))
        print("Luas:", segitiga_siku_siku(a, t))

    elif pilih == 4:
        r = float(input("Masukkan jari-jari: "))
        print("Luas:", setengah_lingkaran(r))

    elif pilih == 5:
        r = float(input("Masukkan jari-jari: "))
        print("Luas:", seperempat_lingkaran(r))

    elif pilih == 6:
        a = float(input("Sumbu a: "))
        b = float(input("Sumbu b: "))
        print("Luas:", elips(a, b))

    elif pilih == 7:
        a = float(input("Sisi a: "))
        b = float(input("Sisi b: "))
        print("Keliling:", jajargenjang_keliling(a, b))

    elif pilih == 8:
        a = float(input("Sisi atas: "))
        b = float(input("Sisi bawah: "))
        c = float(input("Sisi miring: "))
        print("Keliling:", trapesium_sama_kaki(a, b, c))

    elif pilih == 9:
        s = float(input("Masukkan sisi: "))
        k, l = pentagon(s)
        print("Keliling:", k)
        print("Luas:", l)

    elif pilih == 10:
        s = float(input("Masukkan sisi: "))
        k, l = heksagon(s)
        print("Keliling:", k)
        print("Luas:", l)

    elif pilih == 11:
        r = float(input("Masukkan jari-jari: "))
        print("Keliling:", lingkaran_keliling(r))

    elif pilih == 12:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")
