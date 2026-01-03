import math

def prisma_segiempat(p, l, t):
    return p * l * t

def prisma_segilima(luas_alas, tinggi):
    return luas_alas * tinggi

def limas_segilima(luas_alas, tinggi):
    return (1/3) * luas_alas * tinggi

def limas_segienam(luas_alas, tinggi):
    return (1/3) * luas_alas * tinggi

def kerucut_terpancung(r1, r2, t):
    return (1/3) * math.pi * t * (r1*r1 + r1*r2 + r2*r2)

def tabung_terpancung(r1, r2, t):
    return math.pi * t * (r1*r1 + r1*r2 + r2*r2)

def bola_pejal(r):
    return (4/3) * math.pi * r**3

def bola_berongga(r_luar, r_dalam):
    return (4/3) * math.pi * (r_luar**3 - r_dalam**3)

def setengah_tabung(r, t):
    return 0.5 * math.pi * r * r * t

def prisma_trapesium(a, b, tinggi_trap, panjang):
    luas_alas = 0.5 * (a + b) * tinggi_trap
    return luas_alas * panjang

def luas_kerucut(r, s):
    return math.pi * r * (r + s)
