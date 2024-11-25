class Perpustakaan:
    def __init__(self):
        self.__daftar_buku = []
        self.__daftar_anggota = []

    def tambah_buku(self, buku):
        self.__daftar_buku.append(buku)
        print(f"Buku '{buku.get_judul()}' berhasil ditambahkan.")

    def daftar_buku_tersedia(self):
        print("Daftar Buku Tersedia:")
        for buku in self.__daftar_buku:
            if buku.get_status() == "Tersedia":
                buku.tampilkan_info_buku()

    def tambah_anggota(self, anggota):
        self.__daftar_anggota.append(anggota)
        print(f"Anggota '{anggota._Anggota__nama}' berhasil didaftarkan.")

    def pinjam_buku(self, nama_anggota, judul_buku):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nama == nama_anggota), None)
        buku = next((b for b in self.__daftar_buku if b.get_judul() == judul_buku), None)
        if anggota and buku:
            anggota.pinjam_buku(buku)
        else:
            print("Anggota atau Buku tidak ditemukan.")

    def kembalikan_buku(self, nama_anggota, judul_buku):
        anggota = next((a for a in self.__daftar_anggota if a._Anggota__nama == nama_anggota), None)
        buku = next((b for b in self.__daftar_buku if b.get_judul() == judul_buku), None)
        if anggota and buku:
            anggota.kembalikan_buku(buku)
        else:
            print("Anggota atau Buku tidak ditemukan.")
