from models.buku import Buku, BukuDigital
from models.anggota import Anggota
from models.perpustakaan import Perpustakaan

def menu():
    perpustakaan = Perpustakaan()

    while True:
        print("\n=== Menu Perpustakaan ===")
        print("1. Tambah Buku")
        print("2. Tambah Anggota")
        print("3. Pinjam Buku")
        print("4. Kembalikan Buku")
        print("5. Daftar Buku Tersedia")
        print("6. Tampilkan Info Anggota")
        print("7. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            judul = input("Judul: ")
            pengarang = input("Pengarang: ")
            tahun = input("Tahun Terbit: ")
            isbn = input("ISBN: ")
            buku = Buku(judul, pengarang, tahun, isbn)
            perpustakaan.tambah_buku(buku)

        elif pilihan == "2":
            nama = input("Nama: ")
            nomor = input("Nomor Anggota: ")
            alamat = input("Alamat: ")
            anggota = Anggota(nama, nomor, alamat)
            perpustakaan.tambah_anggota(anggota)

        elif pilihan == "3":
            nama = input("Nama Anggota: ")
            judul = input("Judul Buku: ")
            perpustakaan.pinjam_buku(nama, judul)

        elif pilihan == "4":
            nama = input("Nama Anggota: ")
            judul = input("Judul Buku: ")
            perpustakaan.kembalikan_buku(nama, judul)

        elif pilihan == "5":
            perpustakaan.daftar_buku_tersedia()

        elif pilihan == "6":
            nama = input("Nama Anggota: ")
            anggota = next((a for a in perpustakaan._Perpustakaan__daftar_anggota if a._Anggota__nama == nama), None)
            if anggota:
                anggota.tampilkan_info_anggota()
            else:
                print("Anggota tidak ditemukan.")

        elif pilihan == "7":
            print("Terima kasih telah menggunakan aplikasi perpustakaan!")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
