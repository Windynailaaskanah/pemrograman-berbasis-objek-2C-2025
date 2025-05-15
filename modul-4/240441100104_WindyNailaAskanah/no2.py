class Buku:
    def __init__(self, judul, penulis, jumlah_halaman):
        self.__judul = judul
        self.__penulis = penulis
        self.__jumlah_halaman = jumlah_halaman

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_jumlah_halaman(self):
        return self.__jumlah_halaman

    def tampilkan_info(self):
        print(f"Judul: {self.__judul}")
        print(f"Penulis: {self.__penulis}")
        print(f"Jumlah Halaman: {self.__jumlah_halaman}")
        print()

class Perpustakaan:
    def __init__(self, kapasitas):
        self.daftar_buku = []
        self.kapasitas = kapasitas

    def tambah_buku(self, buku):
        if len(self.daftar_buku) < self.kapasitas:
            self.daftar_buku.append(buku)
        else:
            print("Perpustakaan sudah penuh, tidak bisa menambah buku lagi.")

    def tampilkan_daftar_buku(self):
        if len(self.daftar_buku) == 0:
            print("Tidak ada buku di perpustakaan.")
        else:
            for buku in self.daftar_buku:
                buku.tampilkan_info()

def main():
    perpustakaan = Perpustakaan(5)

    perpustakaan.tambah_buku(Buku("Buku Python", "John Doe", 250))
    perpustakaan.tambah_buku(Buku("Belajar Java", "Jane Doe", 300))
    perpustakaan.tambah_buku(Buku("C++ Programming", "Rudi Hartono", 350))

    perpustakaan.tampilkan_daftar_buku()

main()