from anomali.persegipanjang import PersegiPanjang
from anomali.segitiga import Segitiga
from anomali.bangun_ruang import BangunRuang
from anomali.vbalok import Balok

print('hello world!')
p1 = PersegiPanjang(20, 20)
print(p1.info())
print(p1.hitung_luas())

s1= Segitiga(20,60)
print(s1.info())
print(s1.hitung_luas())

ba1= Balok(25, 10, 6)
print(ba1.info())
print(ba1.hitung_volume())

print('\nPercobaan membuat objek dari kelas BangunRuang')
b1 = BangunRuang()
print(b1.info())
print(b1.hitung_luas())

#Polymophism: Kemampuaan object untuk merespon berbeda terhadap metode pemanggilan yang samaan
daftar_bangun_ruang = []
daftar_bangun_ruang.append(p1)
daftar_bangun_ruang.append(s1)
daftar_bangun_ruang.append(ba1)

print('\nPolymorphism')
for bangun_ruang in daftar_bangun_ruang:
    print(bangun_ruang.info())

