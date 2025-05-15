class RekeningBank:
    def __init__(self, no_rek, nama_pemilik, saldo):
        self._no_rek = no_rek
        self._nama_pemilik = nama_pemilik
        self._saldo = saldo

    def get_no_rek(self):
        return self._no_rek

    def get_nama_pemilik(self):
        return self._nama_pemilik

    def get_saldo(self):
        return self._saldo

    def setor(self, jumlah):
        if jumlah > 0:
            self._saldo += jumlah

    def tarik(self, jumlah):
        if 0 < jumlah <= self._saldo:
            self._saldo -= jumlah

    def tampilkan_info(self):
        print(f"No. Rekening: {self._no_rek}")
        print(f"Nama Pemilik: {self._nama_pemilik}")
        print(f"Saldo: {self._saldo}")

class Bank:
    def __init__(self, max_rekening):
        self._daftar_rekening = []
        self._max_rekening = max_rekening

    def tambah_rekening(self, no_rek, nama_pemilik, saldo_awal):
        if len(self._daftar_rekening) < self._max_rekening:
            rekening = RekeningBank(no_rek, nama_pemilik, saldo_awal)
            self._daftar_rekening.append(rekening)
        else:
            print("Bank sudah penuh! tidak bisa menambahkan rekening baru!!")

    def setor(self, no_rek, jumlah):
        for rekening in self._daftar_rekening:
            if rekening.get_no_rek() == no_rek:
                rekening.setor(jumlah)
                break
        else:
            print(f"Rekening {no_rek} tidak ditemukan.")

    def tarik(self, no_rek, jumlah):
        for rekening in self._daftar_rekening:
            if rekening.get_no_rek() == no_rek:
                rekening.tarik(jumlah)
                break
        else:
            print(f"Rekening {no_rek} tidak ditemukan.")

    def tampilkan_semua_rekening(self):
        if not self._daftar_rekening:
            print("Tidak ada rekening yang terdaftar.")
        else:
            for rekening in self._daftar_rekening:
                rekening.tampilkan_info()
                print("-------------------------")

def main():
    bank = Bank(max_rekening=5)

    bank.tambah_rekening("001", "Windy", 5000000)
    bank.tambah_rekening("002", "Naila", 3000000)
    bank.tambah_rekening("003", "Askanah", 1000000)

    bank.setor("001", 150000)
    bank.tarik("002", 50000)

    bank.tampilkan_semua_rekening()

main()