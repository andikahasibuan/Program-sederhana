kontak = []

def tambah_kontak(kontak):
	nama = input("Masukkan nama:")
	telepon = int(input("No hp: "))
	email = input("Email: ")
	kontak.append({"Nama": nama, "Telepon": telepon, "Email": email})
	print("Kontak berhasil ditambahkan!")

def lihat_kontak(kontak):
	print("==Daftar kontak anda==")
	for index, daftar in enumerate(kontak):
		print(f"{index + 1}. Nama: {daftar["Nama"]}, Telepon: {daftar["Telepon"]}, Email: {daftar["Email"]}")

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

def update_kontak(kontak):
	for index, i in enumerate(kontak):
		print(f"{index + 1}. Nama: {i["Nama"]}, Telepon: {i["Telepon"]}, Email: {i["Email"]}")
	update = int(input("Pilih kontak yang ingin diupdate: ")) -1
	if update > index:
		print("Angka yang anda masukkan tidak valid!")
	else:
		print("1. Nama")
		print("2. No hp")
		print("3. Email")
		pilihan = int(input("Pilih bagian mana yang ingin diupdate: "))
		match pilihan:
			case 1:
				nama_baru = input("Masukkan nama baru: ")
				kontak[update]["Nama"] = nama_baru
			case 2:
				no_hp = int(input("Masukkan no hp baru: "))
				kontak[update]["Telepon"]= no_hp
			case 3:
				email_baru = input("Masukkan email baru: ")
				kontak[update]["Email"] = email_baru
			case _:
				print("Tidak valid!")

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
			lihat_kontak(kontak)
		case 3:
			cari_kontak()
		case 4:
			hapus_kontak(kontak)
		case 5:
			update_kontak(kontak)
		case 6:
			print("Anda keluar dari Contact book")
			break
		case _:
			print("Tidak valid!")

			

	