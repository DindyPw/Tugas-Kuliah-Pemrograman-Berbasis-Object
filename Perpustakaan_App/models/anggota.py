class Anggota:
    def __init__(self, nama, nomor_anggota, alamat):
        self.__nama = nama
        self.__nomor_anggota = nomor_anggota
        self.__alamat = alamat
        self.__daftar_pinjaman = []

    def tampilkan_info_anggota(self):
        print(f"Nama: {self.__nama}, Nomor Anggota: {self.__nomor_anggota}, Alamat: {self.__alamat}")
        print("Buku yang dipinjam:")
        if self.__daftar_pinjaman:
            for buku in self.__daftar_pinjaman:
                print(f"- {buku.get_judul()}")
        else:
            print("Tidak ada buku yang dipinjam.")

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.__daftar_pinjaman.append(buku)
            print(f"{buku.get_judul()} berhasil dipinjam.")
        else:
            print(f"{buku.get_judul()} sedang tidak tersedia.")

    def kembalikan_buku(self, buku):
        if buku in self.__daftar_pinjaman:
            buku.kembalikan()
            self.__daftar_pinjaman.remove(buku)
            print(f"{buku.get_judul()} berhasil dikembalikan.")
        else:
            print(f"{buku.get_judul()} tidak ada dalam daftar pinjaman.")
