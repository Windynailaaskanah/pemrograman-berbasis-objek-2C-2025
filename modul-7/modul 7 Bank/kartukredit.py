from pembayaran import Pembayaran

class PembayaranKartukredit(Pembayaran):
    def __init__(self, harga_barang):
        self.harga_barang = harga_barang

    def bayar(self):
        biaya_admin = 0.02  
        total_bayar = self.harga_barang * (1 + biaya_admin)
        print(f"Anda telah melakukan pembayaran menggunakan kartu kredit sejumlah Rp{self.harga_barang} "
              f"dengan biaya admin 2%, total yang dibayar: Rp{total_bayar}")
        return total_bayar
