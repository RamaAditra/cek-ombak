from anomali.bangun_ruang import BangunRuang


class Balok(BangunRuang):

    def __init__(self, panjang, lebar, tinggi):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def info(self):
        return f'Berikut adalah caranya menghitung volume pada balok dengan panjang = {self.panjang}, lebar =' \
               f' {self.lebar} dan tinggi = {self.tinggi}'

    def hitung_volume(self):
        return self.panjang * self.tinggi * self.lebar
