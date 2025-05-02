class Karyawan:
    def __init__(self, nama, gaji, departemen):
        self.nama = nama
        self.gaji = gaji
        self.departemen = departemen

    def info(self):
        print(f"Nama: {self.nama}")
        print(f"Gaji: {self.gaji}")
        print(f"Departemen: {self.departemen}")

class KaryawanTetap(Karyawan):
    def __init__(self, nama, gaji, departemen, tunjangan):
        super().__init__(nama, gaji, departemen)
        self.tunjangan = tunjangan

    def info(self):
        print("Jenis Karyawan: Karyawan Tetap")
        super().info()
        print(f"Tunjangan: {self.tunjangan}")

class KaryawanHarian(Karyawan):
    def __init__(self, nama, gaji, departemen, jam_kerja):
        super().__init__(nama, gaji, departemen)
        self.jam_kerja = jam_kerja

    def info(self):
        print("Jenis Karyawan: Karyawan Harian")
        super().info()
        print(f"Jam Kerja: {self.jam_kerja} jam/hari")

class ManajemenKaryawan:
    def __init__(self):
        self.daftar_karyawan = []

    def tambah_karyawan(self, Karyawan):
        self.daftar_karyawan.append(Karyawan)

    def tampilkan_semua_karyawan(self):
        print("Daftar Karyawan: ")
        for Karyawan in self.daftar_karyawan:
            Karyawan.info()
            print("-" * 30)

manajeman = ManajemenKaryawan()

k1 = KaryawanTetap("windy", 5000000, "IT", 1000000)
k2 = KaryawanTetap("naila", 4500000, "IT", 900000)
k3 = KaryawanHarian("askanah", 2500000, "Teknisi", 11)
k4 = KaryawanHarian("erika", 3700000, "Teknisi", 13)

manajeman.tambah_karyawan(k1)
manajeman.tambah_karyawan(k2)
manajeman.tambah_karyawan(k3)
manajeman.tambah_karyawan(k4)

manajeman.tampilkan_semua_karyawan()