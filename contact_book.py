kontak = []


def tambah_kontak(kontak):
	pilihan = input("Masukkan nama:")
	telepon = int(input("No hp: "))
	email = input("Email: ")
	data = {
		"Nama" : pilihan,
		"Telepon" : telepon,
		"Email" : email
	}
	kontak.append(data)
	print("Kontak berhasil ditambahkan!")

def lihat_kontak():
	print("==Daftar kontak anda==")
	for index, daftar in enumerate(kontak):
		print(f"{index + 1}. {kontak}")

def cari_kontak():
	pass

def hapus_kontak(kontak):
	print("==daftar kontak anda==")
	for index, i in enumerate(kontak):
		print(f"{index + 1}. {i}")
	pilihan = int(input("Pilih kontak yang ingin dihapus: ")) -1
	match pilihan:
		case _ if pilihan > index:
			print("Pilihan tidak valid!")
		case _:
			kontak.pop(pilihan)
			print("Kontak berhasil dihapus!")


def update_kontak():
	pass

def main():
	print("==Contact Book==")
	print("1. Tambah Kontak")
	print("2. Lihat Kontak")
	print("3. Cari Kontak")
	print("4. Hapus Kontak")
	print("5. Update Kontak")
	print("6. Keluar")

while True:
	main()
	pilihan = int(input(":"))
	match pilihan:
		case _ if pilihan > 6:
			print("Angka yang anda masukkan tidak valid!")
		case 1:
			tambah_kontak(kontak)
		case 2:
			lihat_kontak()
		case 3:
			cari_kontak()
		case 4:
			hapus_kontak(kontak)
		case 5:
			update_kontak()
		case 6:
			print("Anda keluar dari Contact book")
			break
		case _:
			print("Tidak valid!")

			

	