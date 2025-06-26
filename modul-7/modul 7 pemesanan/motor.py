from pemesanan import Pemesanan

class Motor(Pemesanan):
    def __init__(self):
        self.tarif_per_jam = 50000
        self.asuransi = 25000

    def proses_pemesanan(self, nama, usia):
        if usia < 17:
            return f"Maaf {nama}, usia minimal untuk menyewa motor adalah 17 tahun."
        return f"Booking motor atas nama {nama} berhasil."

    def hitung_biaya(self, durasi):
        return durasi * self.tarif_per_jam

    def tambah_asuransi(self):
        return self.asuransi
