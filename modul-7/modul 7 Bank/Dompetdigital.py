from pembayaran import Pembayaran

class EWallet(Pembayaran):
    def __init__(self, harga_barang):
        self.harga_barang = harga_barang

    def bayar(self):
        potongan = 0.10
        total_bayar = self.harga_barang * (1 - potongan)
        print(f"Anda telah melakukan pembayaran melalui E-Wallet sejumlah Rp{self.harga_barang} "
              f"dengan potongan 5%, total yang dibayar: Rp{total_bayar}")
        return total_bayar