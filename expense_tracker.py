from datetime import datetime
import json
import os

if os.path.exists:
	try:
		with open("data.json", 'r') as file:
			transaksi = json.load(file)
	except json.JSONDecodeError:
		transaksi = []
else:
	transaksi = []

def tambah_transaksi(transaksi):
	print("Contoh YY-MM--DD")
	tanggal =input("Masukkan tanggal:")
	tanggal1 = datetime.strptime(tanggal, "%Y-%m-%d").date()
	jumlah = int(input("Masukkan jumlah harga: "))
	kategori = input("Masukkan kategori: ")
	catatan = input("Tambahkan catatan: ")
	print("Transaksi anda berhasil ditambahkan!")
	data = f"({tanggal1}) Rp{jumlah} - {kategori}, {catatan}"
	transaksi.append(data)
	with open("data.json", "w") as file:
		json.dump(transaksi, file, indent = 4, default= str)

		

def lihat_transaksi():
	while True:
		print("==Riwayat transaksi anda==")
		with open("data.json", "r") as file:
			data = json.load(file)
		if not data:
			print("Anda belum memiliki riwayat transaksi!")
			return
		for index, i in enumerate(data):
			print(f"{index + 1}. {i}")
		pilihan = input("Ketik q untuk kembali: ")
		if pilihan != "q":
			print("Data tidak valid!")
		else:
			print("Anda kembali ke menu utama!")
			break

def hapus_transaksi():
	with open("data.json", "r") as file:
		data = json.load(file)
	if not data:
		print("Anda tidak memiliki data yang bisa di hapus!")
		return
	for nomor, i in enumerate(data):
		print(f"{nomor + 1}. {i}")
	pilihan = int(input("Silahkan pilih data transaksi mana yang ingin anda hapus:  ")) -1
	if pilihan > nomor :
		print("Data tidak valid!")
	else:
		data.pop(pilihan)
		print("Data transaksi berhasil di hapus!")
		with open ("data.json", "w") as file:
			json.dump(data, file)
			


def keluar():
	print("Anda keluar dari Expense Tracker!")

def main():
	print("==Expense Tracker==")
	print("1. Tambah transaksi")
	print("2. Lihat transaksi")
	print("3. Hapus transaksi")
	print("4. Keluar")


while True:
	main()
	try:
		pilihan = int(input("Silahkan pilih: "))
		if pilihan > 4 or pilihan == 0:
			print("Nomor tidak valid!")
		elif pilihan == 1:
			tambah_transaksi(transaksi)
		elif pilihan == 2:
			lihat_transaksi()
		elif pilihan == 3:
			hapus_transaksi()
		elif pilihan == 4:
			keluar()
			break
	except ValueError:
		print("Data yang anda masukkan tidak valid!")
