class PersegiPanjang():
    def __init__(self, p, l):
        self.p = p
        self.l = l
    def info(self):
        return f'Berikut adalah object persegi panjang dengan panjang = {self.p} dan lebar = {self.l}'

    def hitung_luas(self):
        return self.p * self.l
