import math

def segitiga_sama_sisi(s):
    keliling = 3 * s
    luas = (math.sqrt(3) / 4) * s * s
    return keliling, luas

def segitiga_sama_kaki(alas, sisi):
    return alas + 2 * sisi

def segitiga_siku_siku(alas, tinggi):
    return 0.5 * alas * tinggi

def setengah_lingkaran(r):
    return 0.5 * math.pi * r * r

def seperempat_lingkaran(r):
    return 0.25 * math.pi * r * r

def elips(a, b):
    return math.pi * a * b

def jajargenjang_keliling(a, b):
    return 2 * (a + b)

def trapesium_sama_kaki(a, b, c):
    return a + b + 2 * c

def pentagon(s):
    keliling = 5 * s
    luas = (1/4) * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * s * s
    return keliling, luas

def heksagon(s):
    keliling = 6 * s
    luas = (3 * math.sqrt(3) / 2) * s * s
    return keliling, luas

def lingkaran_keliling(r):
    return 2 * math.pi * r
