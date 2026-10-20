class Transaksi:
    def __init__(self, tanggal, aset, jenis, jumlah, harga):
        self.tanggal = tanggal
        self.aset = aset.upper()
        self.jenis = jenis.lower()
        self.jumlah = jumlah
        self.harga = harga

    def nilai_total(self):
        return self.jumlah * self.harga

    def to_list(self):
        return [
            self.tanggal,
            self.aset,
            self.jenis,
            self.jumlah,
            self.harga,
            self.nilai_total()
        ]
