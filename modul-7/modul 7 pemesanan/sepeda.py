from pemesanan import Pemesanan

class Sepeda(Pemesanan):
    def __init__(self):
        self.tarif_per_jam = 20000
        self.asuransi = 10000

    def proses_pemesanan(self, nama, usia):
        if usia < 10:
            return f"Maaf {nama}, usia minimal untuk menyewa sepeda adalah 10 tahun."
        return f"Booking sepeda atas nama {nama} berhasil."

    def hitung_biaya(self, durasi):
        return durasi * self.tarif_per_jam

    def tambah_asuransi(self):
        return self.asuransi
