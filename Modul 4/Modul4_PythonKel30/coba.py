
    # ==========================================
# 1. FUNCTION (Fungsi Standar)
# ==========================================

# Function non-return type tanpa parameter
def tampilkan_header():
    print("=======================================================")
    print("      SISTEM MANAJEMEN INVENTARIS TOKO ELEKTRONIK      ")
    print("=======================================================")


# Function return type dengan parameter (Menggunakan PENGKONDISIAN & PERULANGAN)
def hitung_total_setelah_kategori(daftar_produk, kategori_target):
    total_nilai = 0
    # PERULANGAN 1: Loop 'for' untuk menghitung total barang
    for p in daftar_produk:
        # PENGKONDISIAN 1: Memeriksa kode/kategori barang
        if p.kategori.upper() == kategori_target.upper():
            total_nilai += p.harga * p.stok
    return total_nilai


# ==========================================
# 2. CLASS & METHOD (Pemrograman Berbasis Objek)
# ==========================================

class Produk:
    def __init__(self, kode, nama, kategori, harga, stok):
        self.kode = kode          # Variabel Pengkodean (e.g., LAP-001)
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    # Method non-return type tanpa parameter (Menggunakan PENGKONDISIAN)
    def tampilkan_detail_status(self):
        # PENGKONDISIAN 2: Penentuan status ketersediaan stok
        if self.stok == 0:
            status = "STOK HABIS"
        elif self.stok < 5:
            status = "STOK KRITIS"
        else:
            status = "TERSEDIA"

        print(f"[{self.kode}] {self.nama:<18} | Rp {self.harga:>10,}/unit | Stok: {self.stok:>2} | Status: {status}")

    # Method return type dengan parameter (Menggunakan PENGKONDISIAN)
    def proses_pembelian(self, jumlah_beli):
        # PENGKONDISIAN 3: Validasi kecukupan stok saat transaksi
        if jumlah_beli <= 0:
            print(f"[ERROR] Pembelian {self.nama} gagal! Jumlah harus lebih dari 0.")
            return 0
        elif jumlah_beli > self.stok:
            print(f"[GAGAL] Stok {self.nama} tidak cukup! (Sisa stok: {self.stok})")
            return 0
        else:
            self.stok -= jumlah_beli
            total_harga = self.harga * jumlah_beli
            return total_harga


# ==========================================
# 3. PROGRAM UTAMA (Main Program)
# ==========================================
if __name__ == "__main__":
    # Memanggil Function non-return type tanpa parameter
    tampilkan_header()

    # Data produk dengan sistem Pengkodean
    daftar_produk = [
        Produk("LAP-001", "Laptop Gaming", "Komputer", 12000000, 3),
        Produk("MOU-002", "Mouse Wireless", "Aksesori", 150000, 15),
        Produk("KEY-003", "Keyboard RGB", "Aksesori", 450000, 0),
        Produk("MON-004", "Monitor 24 Inch", "Komputer", 2100000, 8),
    ]

    print("\n--- Status Inventaris Awal ---")
    # PERULANGAN 2: Loop 'for' untuk menampilkan status setiap produk
    for item in daftar_produk:
        # Memanggil Method non-return type tanpa parameter
        item.tampilkan_detail_status()

    print("\n--- Simulasi Pemrosesan Transaksi (Loop While) ---")
    # Antrean pengkodean transaksi pembelian: (kode_produk, jumlah_beli)
    transaksi = [
        ("KEY-003", 2),  # Pembelian barang stok habis
        ("LAP-001", 2),  # Pembelian berhasil (stok kritis berkurang)
        ("MOU-002", 5)   # Pembelian berhasil
    ]

    index = 0
    total_pendapatan = 0

    # PERULANGAN 3: Loop 'while' untuk memproses antrean transaksi
    while index < len(transaksi):
        kode_target, qty = transaksi[index]

        # Mencari produk yang sesuai dengan kode
        for p in daftar_produk:
            if p.kode == kode_target:
                # Memanggil Method return type dengan parameter
                biaya = p.proses_pembelian(qty)
                total_pendapatan += biaya
                break

        index += 1

    print("\n--- Status Inventaris Setelah Transaksi ---")
    for item in daftar_produk:
        item.tampilkan_detail_status()

    # Memanggil Function return type dengan parameter
    total_nilai_komputer = hitung_total_setelah_kategori(daftar_produk, "Komputer")

    print("\n--- Ringkasan Laporan ---")
    print(f"Total Pendapatan Transaksi : Rp {total_pendapatan:,}")
    print(f"Sisa Total Asset (Komputer): Rp {total_nilai_komputer:,}")
    print("=======================================================")
