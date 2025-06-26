from abc import ABC, abstractmethod

class Pemesanan(ABC):
    @abstractmethod
    def proses_pemesanan(self, nama, usia):
        pass

    @abstractmethod
    def hitung_biaya(self, durasi):
        pass

    @abstractmethod
    def tambah_asuransi(self):
        pass
