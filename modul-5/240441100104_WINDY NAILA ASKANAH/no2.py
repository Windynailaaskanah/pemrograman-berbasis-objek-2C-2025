from abc import ABC, abstractmethod

class PerangkatElektronik(ABC):
    def __init__(self, nama):
        self.nama = nama
        self.energi_tersisa = 100

    @abstractmethod
    def nyalakan_perangkat(self):
        pass

    @abstractmethod
    def matikan_perangkat(self):
        pass

    @abstractmethod
    def gunakan_perangkat(self, jam):
        pass

    def status(self):
        print(f"Tipe perangkat: {self.nama}")
        print(f"Energi tersisa: {self.energi_tersisa}%")

class Laptop(PerangkatElektronik):
    def __init__(self, nama):
        super().__init__(nama)
        print("Laptop")

    def nyalakan_perangkat(self):
        print("Laptop telah dinyalakan.")

    def matikan_perangkat(self):
        print("Laptop telah dimatikan.")

    def gunakan_perangkat(self, jam):
        print(f"Laptop sudah digunakan selama {jam} jam.")
        self.energi_tersisa -= 10 * jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("Baterai laptop telah habis, silakan isi ulang daya!")
        else:
            print("Penggunaan laptop telah selesai.")

class Kulkas(PerangkatElektronik):
    def __init__(self, nama):
        super().__init__(nama)
        print("Kulkas")

    def nyalakan_perangkat(self):
        print("Kulkas telah dinyalakan.")

    def matikan_perangkat(self):
        print("Kulkas telah dimatikan.")

    def gunakan_perangkat(self, jam):
        print(f"Kulkas telah digunakan selama {jam} jam.")
        self.energi_tersisa -= 5 * jam
        if self.energi_tersisa <= 0:
            self.energi_tersisa = 0
            print("Tidak ada energi tersisa.")
        elif self.energi_tersisa < 20:
            print("Energi rendah, mohon isi daya!")
        else:
            print("Energi masih cukup.")

print("=== laptop ===")
laptop = Laptop("Lenovo")
laptop.nyalakan_perangkat()
laptop.gunakan_perangkat(7)
laptop.status()
laptop.matikan_perangkat()

print("\n===  kulkas ===")
kulkas = Kulkas("Sharp")
kulkas.nyalakan_perangkat()
kulkas.gunakan_perangkat(12)
kulkas.status()
kulkas.matikan_perangkat()
