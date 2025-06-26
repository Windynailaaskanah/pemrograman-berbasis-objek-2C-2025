from pembayaran import Pembayaran

class PembayaranTunai(Pembayaran):
    def __init__(self, harga_barang):
        self.harga_barang = harga_barang

    def bayar(self):
        diskon = 0.10  
        total_bayar = self.harga_barang * (1 - diskon)
        print(f"Anda telah melakukan pembayaran secara tunai sejumlah Rp{self.harga_barang} "
              f"dengan diskon 10%, Anda hanya perlu membayar Rp{total_bayar}")
        return total_bayar
