from reservasi import Reservasi

class BukuReferensi(Reservasi):
    def __init__(self, judul):
        self.judul = judul

    def reservasi(self, nama):
        return f"{nama} berhasil melakukan reservasi buku referensi: '{self.judul}'."

    def pinjam(self):
        return f"Buku referensi '{self.judul}' tidak boleh dipinjam, hanya bisa dibaca di tempat."
