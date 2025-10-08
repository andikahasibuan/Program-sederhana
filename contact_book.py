import json
import os

if os.path.exists:
	try:
		with open("contact.json", "r") as file:
			kontak = json.load(file)
	except json.JSONDecodeError:
		kontak = []

def tambah_kontak(kontak):
	nama = input("Masukkan nama:").capitalize()
	telepon = int(input("No hp: "))
	email = input("Email: ")
	kontak.append({"Nama": nama, "Telepon": telepon, "Email": email})
	print("Kontak berhasil ditambahkan!")
	with open ("contact.json", "w") as file:
		kontak = json.dump(kontak, file, indent= 4)

def lihat_kontak(kontak):
	if not kontak:
		print("Anda belum memiliki kontak tersimpan!")
		return
	print("==Daftar kontak anda==")
	for index, daftar in enumerate(kontak):
		print(f"{index + 1}. Nama: {daftar["Nama"]}, Telepon: {daftar["Telepon"]}, Email: {daftar["Email"]}")

def cari_kontak(kontak):
	if not kontak:
		print("Anda belum memiliki kontak tersimpan!")
		return
	pilihan = input("Cari  berdasarkan nama: ").capitalize()
	ditemukan = False
	for daftar in kontak:
		if pilihan in daftar ["Nama"]:
			print(f"{pilihan} Ada dalam daftar kontak anda!")
			print(f"Nama: {daftar["Nama"]}, Telepon: {daftar["Telepon"]}, Email: {daftar["Email"]}")
			ditemukan = True
	if not ditemukan:
		print(f"{pilihan} tidak ada dalam daftar kontak anda!")

def hapus_kontak(kontak):
	if not kontak:
		print("Anda tidak memiliki kontak yang bisa dihapus!")
		return
	print("==daftar kontak anda==")
	for index, i in enumerate(kontak):
		print(f"{index + 1}. Nama: {i["Nama"]}, Telepon: {i["Telepon"]}, Email: {i["Email"]}")
	try:
		pilihan = int(input("Pilih kontak yang ingin dihapus: ")) -1
		match pilihan:
			case _ if pilihan > index:
				print("Pilihan tidak valid!")
			case _:
				kontak_hapus = kontak.pop(pilihan)
				print(f"{kontak_hapus["Nama"]} berhasil dihapus dari daftar kontak anda!")
	except ValueError:
		print("Pilihan anda tidak valid!")
	with open("contact.json", "w") as file:
		kontak = json.dump(kontak, file, indent= 4)

def update_kontak(kontak):
	if not kontak:
		print("Anda belum memiliki kontak tersimpan!")
		return
	for index, i in enumerate(kontak):
		print(f"{index + 1}. Nama: {i["Nama"]}, Telepon: {i["Telepon"]}, Email: {i["Email"]}")
	update = int(input("Pilih kontak yang ingin diupdate: ")) -1
	if update > index:
		print("Angka yang anda masukkan tidak valid!")
	else:
		print("1. Nama")
		print("2. Telepon")
		print("3. Email")
		pilihan = int(input("Pilih bagian mana yang ingin diupdate: "))
		match pilihan:
			case 1:
				nama_baru = input("Masukkan nama baru: ").capitalize()
				kontak[update]["Nama"] = nama_baru
			case 2:
				no_hp = int(input("Masukkan no telepon baru: "))
				kontak[update]["Telepon"]= no_hp
			case 3:
				email_baru = input("Masukkan email baru: ")
				kontak[update]["Email"] = email_baru
			case _:
				print("Tidak valid!")
	print("Kontak berhasil diupdate!")
	with open("contact.json", "w") as file:
		kontak =  json.dump(kontak, file, indent= 4)

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
	try:
		pilihan = int(input("Silahkan pilih:"))
		match pilihan:
			case _ if pilihan > 6:
				print("Angka yang anda masukkan tidak valid!")
			case 1:
				tambah_kontak(kontak)
			case 2:
				lihat_kontak(kontak)
			case 3:
				cari_kontak(kontak)
			case 4:
				hapus_kontak(kontak)
			case 5:
				update_kontak(kontak)
			case 6:
				print("Anda keluar dari Contact book!")
				break
			case _:
				print("Tidak valid!")
	except ValueError:
		print("Data yang anda masukkan tidak valid!")

			

	