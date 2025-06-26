from Peminjaman import Peminjaman
from reservasi import Reservasi

class BukuFiksi(Peminjaman, Reservasi):
    def __init__(self, judul):
        self.judul = judul
        self.status = "tersedia"

    def pinjam(self, nama):
        if self.status == "tersedia":
            self.status = "dipinjam"
            return f"{nama} berhasil meminjam buku fiksi: '{self.judul}'."
        return f"Buku '{self.judul}' sedang tidak tersedia untuk dipinjam."

    def reservasi(self, nama):
        if self.status == "dipinjam":
            return f"{nama} berhasil melakukan reservasi buku fiksi: '{self.judul}'."
        return f"Buku '{self.judul}' masih tersedia, silakan langsung pinjam."
