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
	jumlah = int(input("Masukkan jumlah: "))
	kategori = input("Masukkan kategori: ")
	catatan = input("Masukkan keterangan: ")
	print("Transaksi anda berhasil ditambahkan!")
	
	data = {
		"tanggal" : tanggal1,
		"jumlah" : jumlah,
		"kategori": kategori,
		"catatan": catatan,
		}
	transaksi.append(data)
	with open("data.json", "w") as file:
		json.dump(transaksi, file, indent = 4, default= str)

		

def lihat_transaksi(transaksi):
	print("==Riwayat transaksi anda==")
	with open("data.json", "r") as file:
		data = json.load(file)
	for index, i in enumerate(data):
		print(f"{index + 1}. {i}")
	

def keluar():
	print("Anda keluar dari Expense Tracker!")

def main():
	print("==Expense Tracker==")
	print("1. Tambah transaksi")
	print("2. Lihat transaksi")
	print("3. Keluar")


while True:
	main()
	pilihan = int(input("Silahkan pilih: "))
	if pilihan > 3:
		print("Nomor tidak valid")
	elif pilihan == 1:
		tambah_transaksi(transaksi)
	elif pilihan == 2:
		lihat_transaksi(transaksi)
	elif pilihan == 3:
		keluar()
		break