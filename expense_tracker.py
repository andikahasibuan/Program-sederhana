transaksi = []

def tambah_transaksi(transaksi):
	print("Contoh YY-MM--DD")
	tanggal = input("Masukkan tanggal:")
	jumlah = int(input("Masukkan jumlah: "))
	keterangan = input("Masukkan keterangan: ")
	transaksi.append(f"({tanggal}) Rp{jumlah} keterangan: {keterangan}")
	print("Transaksi anda berhasil ditambahkan!")
		

def lihat_transaksi(transaksi):
	print("==Riwayat transaksi anda==")
	for index, i in enumerate(transaksi):
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