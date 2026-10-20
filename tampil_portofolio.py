import csv
import os
from collections import defaultdict

FILE_CSV = "transaksi.csv"
LEBAR = [12, 12, 8, 13, 17, 17]
HEADER = ["Tanggal", "Aset", "Jenis", "Jumlah", "Harga/Unit", "Nilai Total"]


def potong(teks, lebar):
    teks = str(teks)
    if len(teks) > lebar:
        return teks[:lebar - 3] + "..."
    return teks


def cetak_baris(data):
    print(" | ".join(potong(data[i], LEBAR[i]).ljust(LEBAR[i]) for i in range(len(LEBAR))))


def muat_transaksi():
    if not os.path.exists(FILE_CSV) or os.path.getsize(FILE_CSV) == 0:
        return []
    hasil = []
    with open(FILE_CSV, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                tanggal = row["Tanggal"]
                # Pastikan tanggal valid dan tahun tersimpan dengan format empat digit.
                from datetime import datetime
                tanggal = datetime.strptime(tanggal, "%Y-%m-%d").date().isoformat()
                aset = row["Aset"].upper()
                jenis = row["Jenis"].lower()
                jumlah = float(row["Jumlah"])
                harga = float(row["Harga per Unit"])
                nilai = float(row["Nilai Total"])
                if jenis not in ("beli", "jual"):
                    continue
                hasil.append({
                    "Tanggal": tanggal, "Aset": aset, "Jenis": jenis,
                    "Jumlah": jumlah, "Harga/Unit": harga, "Nilai Total": nilai
                })
            except (KeyError, ValueError, TypeError):
                continue
    return hasil


def angka(nilai, desimal=2):
    return f"{nilai:,.{desimal}f}"


def tampilkan_riwayat(transaksi):
    if not transaksi:
        print("Belum ada transaksi yang bisa ditampilkan.")
        return
    print("\n=== RIWAYAT TRANSAKSI ===")
    cetak_baris(HEADER)
    print("-" * (sum(LEBAR) + 3 * (len(LEBAR) - 1)))
    for t in transaksi:
        cetak_baris([
            t["Tanggal"], t["Aset"], t["Jenis"],
            angka(t["Jumlah"], 8).rstrip("0").rstrip("."),
            angka(t["Harga/Unit"]), angka(t["Nilai Total"])
        ])
    print("-" * (sum(LEBAR) + 3 * (len(LEBAR) - 1)))
    print("Total transaksi:", len(transaksi))
    print("Catatan: tanggal memakai format YYYY-MM-DD, jadi tahun ikut ditampilkan.")


def tampilkan_portofolio(transaksi):
    if not transaksi:
        print("Belum ada transaksi. Tambahkan transaksi terlebih dahulu.")
        return
    saldo = defaultdict(float)
    total_beli = defaultdict(float)
    total_jual = defaultdict(float)
    for t in transaksi:
        aset = t["Aset"]
        if t["Jenis"] == "beli":
            saldo[aset] += t["Jumlah"]
            total_beli[aset] += t["Nilai Total"]
        else:
            saldo[aset] -= t["Jumlah"]
            total_jual[aset] += t["Nilai Total"]

    widths = [12, 16, 16, 16]
    headings = ["Aset", "Saldo Unit", "Total Beli", "Total Jual"]
    print("\n=== RINGKASAN PORTOFOLIO ===")
    print(" | ".join(headings[i].ljust(widths[i]) for i in range(4)))
    print("-" * (sum(widths) + 3 * 3))
    for aset in sorted(saldo):
        values = [
            potong(aset, widths[0]),
            angka(saldo[aset], 8).rstrip("0").rstrip("."),
            angka(total_beli[aset]), angka(total_jual[aset])
        ]
        row = []
        for i, value in enumerate(values):
            value = potong(value, widths[i])
            row.append(value.ljust(widths[i]) if i == 0 else value.rjust(widths[i]))
        print(" | ".join(row))
    print("-" * (sum(widths) + 3 * 3))
    print("Catatan: aplikasi ini tidak menggunakan harga pasar real-time.")
    print("Saldo negatif berarti penjualan melebihi pembelian yang tercatat.")


def main():
    while True:
        transaksi = muat_transaksi()
        print("\n=== MENU PORTOFOLIO ===")
        print("1. Tampilkan ringkasan portofolio")
        print("2. Tampilkan riwayat transaksi (tanggal dan tahun)")
        print("3. Muat ulang data")
        print("0. Kembali")
        pilihan = input("Pilih: ").strip()
        if pilihan == "1":
            tampilkan_portofolio(transaksi)
        elif pilihan == "2":
            tampilkan_riwayat(transaksi)
        elif pilihan == "3":
            print("Data dimuat ulang.")
        elif pilihan == "0":
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
