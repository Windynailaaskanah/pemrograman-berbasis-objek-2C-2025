from pemesanan import Pemesanan

class Mobil(Pemesanan):
    def __init__(self):
        self.tarif_per_jam = 100000
        self.asuransi = 50000

    def proses_pemesanan(self, nama, usia):
        if usia < 18:
            return f"Maaf {nama}, usia minimal untuk menyewa mobil adalah 18 tahun."
        return f"Booking mobil atas nama {nama} berhasil."

    def hitung_biaya(self, durasi):
        return durasi * self.tarif_per_jam

    def tambah_asuransi(self):
        return self.asuransi
