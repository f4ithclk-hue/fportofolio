import csv
import os
from datetime import date, datetime
from models import Transaksi

FILE_CSV = "transaksi.csv"
HEADER = ["Tanggal", "Aset", "Jenis", "Jumlah", "Harga per Unit", "Nilai Total"]


def simpan_transaksi():
    print("\n=== TAMBAH TRANSAKSI ===")
    tanggal = input("Tanggal (YYYY-MM-DD, kosong = hari ini): ").strip()
    if not tanggal:
        tanggal = date.today().isoformat()

    try:
        tanggal = datetime.strptime(tanggal, "%Y-%m-%d").date().isoformat()
    except ValueError:
        print("Format tanggal salah. Contoh: 2026-10-13")
        return

    aset = input("Nama aset (contoh: BTC, ETH, IDR): ").strip().upper()
    jenis = input("Jenis (beli/jual): ").strip().lower()

    if not aset or len(aset) > 12 or jenis not in ("beli", "jual"):
        print("Nama aset wajib diisi (maksimal 12 karakter) dan jenis harus beli atau jual.")
        return

    try:
        jumlah = float(input("Jumlah aset/uang: "))
        harga = float(input("Harga per unit (untuk IDR isi 1): "))
        if jumlah <= 0 or harga <= 0:
            print("Jumlah dan harga harus lebih dari 0.")
            return
    except ValueError:
        print("Jumlah dan harga harus berupa angka.")
        return

    transaksi = Transaksi(tanggal, aset, jenis, jumlah, harga)
    file_baru = not os.path.exists(FILE_CSV) or os.path.getsize(FILE_CSV) == 0

    with open(FILE_CSV, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if file_baru:
            writer.writerow(HEADER)
        writer.writerow(transaksi.to_list())

    print("Transaksi berhasil disimpan. Tahun tercatat pada kolom Tanggal.")
    print("Tanggal transaksi:", tanggal)


def main():
    while True:
        print("\n=== MENU TRANSAKSI ===")
        print("1. Tambah transaksi")
        print("0. Kembali")
        pilihan = input("Pilih: ").strip()
        if pilihan == "1":
            simpan_transaksi()
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
