from utils import *

while True:
    print("\n=== Menu Bangun Ruang ===")
    print("1. Prisma Segiempat")
    print("2. Prisma Segilima")
    print("3. Limas Segilima")
    print("4. Limas Segienam")
    print("5. Kerucut Terpancung")
    print("6. Tabung Terpancung")
    print("7. Bola Pejal")
    print("8. Bola Berongga")
    print("9. Setengah Tabung")
    print("10. Prisma Trapesium")
    print("11. Kerucut (Luas Permukaan)")
    print("12. Keluar")

    pilih = int(input("\nPilih bangun ruang: "))

    if pilih == 1:
        p = float(input("Panjang: "))
        l = float(input("Lebar: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segiempat(p, l, t))

    elif pilih == 2:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi: "))
        print("Volume:", prisma_segilima(la, t))

    elif pilih == 3:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", limas_segilima(la, t))

    elif pilih == 4:
        la = float(input("Luas alas: "))
        t = float(input("Tinggi limas: "))
        print("Volume:", limas_segienam(la, t))

    elif pilih == 5:
        r1 = float(input("Jari-jari atas: "))
        r2 = float(input("Jari-jari bawah: "))
        t = float(input("Tinggi: "))
        print("Volume:", kerucut_terpancung(r1, r2, t))

    elif pilih == 6:
        r1 = float(input("Jari-jari atas: "))
        r2 = float(input("Jari-jari bawah: "))
        t = float(input("Tinggi: "))
        print("Volume:", tabung_terpancung(r1, r2, t))

    elif pilih == 7:
        r = float(input("Jari-jari: "))
        print("Volume:", bola_pejal(r))

    elif pilih == 8:
        r1 = float(input("Jari-jari luar: "))
        r2 = float(input("Jari-jari dalam: "))
        print("Volume:", bola_berongga(r1, r2))

    elif pilih == 9:
        r = float(input("Jari-jari: "))
        t = float(input("Tinggi: "))
        print("Volume:", setengah_tabung(r, t))

    elif pilih == 10:
        a = float(input("Sisi sejajar a: "))
        b = float(input("Sisi sejajar b: "))
        tt = float(input("Tinggi trapesium: "))
        p = float(input("Panjang prisma: "))
        print("Volume:", prisma_trapesium(a, b, tt, p))

    elif pilih == 11:
        r = float(input("Jari-jari: "))
        s = float(input("Garis pelukis: "))
        print("Luas permukaan:", luas_kerucut(r, s))

    elif pilih == 12:
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak tersedia!")
