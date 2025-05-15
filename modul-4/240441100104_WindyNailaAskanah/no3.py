class Pasien:
    def __init__(self, nama, umur, keluhan):
        self.__nama = nama
        self.__umur = umur
        self.__keluhan = keluhan

    def get_nama(self):
        return self.__nama

    def get_umur(self):
        return self.__umur

    def get_keluhan(self):
        return self.__keluhan

    def tampilkan_info(self):
        print(f"Nama: {self.__nama}")
        print(f"Umur: {self.__umur}")
        print(f"Keluhan: {self.__keluhan}")
        print()

class Klinik:
    def __init__(self, kapasitas):
        self.daftar_pasien = []
        self.kapasitas = kapasitas

    def tambah_pasien(self, pasien):
        if len(self.daftar_pasien) < self.kapasitas:
            self.daftar_pasien.append(pasien)
        else:
            print("Klinik sudah penuh, tidak bisa menambah pasien lagi!")

    def tampilkan_daftar_pasien(self):
        if len(self.daftar_pasien) == 0:
            print("Tidak ada pasien di klinik.")
        else:
            for pasien in self.daftar_pasien:
                pasien.tampilkan_info()

def main():
    klinik = Klinik(3)

    klinik.tambah_pasien(Pasien("Windy", 15, "Batuk pilek"))
    klinik.tambah_pasien(Pasien("Naila", 25, "Demam "))
    klinik.tambah_pasien(Pasien("Askanah", 7, "Sakit kepala"))

    klinik.tampilkan_daftar_pasien()

main()