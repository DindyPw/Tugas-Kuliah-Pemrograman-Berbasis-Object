class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, isbn):
        self.__judul = judul
        self.__pengarang = pengarang
        self.__tahun_terbit = tahun_terbit
        self.__isbn = isbn
        self.__status = "Tersedia"

    def tampilkan_info_buku(self):
        print(f"Judul: {self.__judul}, Pengarang: {self.__pengarang}, "
              f"Tahun Terbit: {self.__tahun_terbit}, ISBN: {self.__isbn}, Status: {self.__status}")

    def pinjam(self):
        if self.__status == "Tersedia":
            self.__status = "Dipinjam"
            return True
        return False

    def kembalikan(self):
        self.__status = "Tersedia"

    def get_status(self):
        return self.__status

    def get_judul(self):
        return self.__judul


class BukuDigital(Buku):
    def __init__(self, judul, pengarang, tahun_terbit, isbn, format_file):
        super().__init__(judul, pengarang, tahun_terbit, isbn)
        self.__format_file = format_file

    def tampilkan_info_buku(self):
        super().tampilkan_info_buku()
        print(f"Format File: {self.__format_file}")
