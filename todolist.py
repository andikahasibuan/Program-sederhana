import time
tugas = []
def tambah_tugas(tugas1):
	tugas2 = input("Tulis tugas yang ingin ditambahkan: ").capitalize()
	tugas1.append(tugas2)
	print("Tugas anda berhasil ditambahkan!")
	time.sleep(1)

def hapus_tugas(tugas1):
	if tugas1 == []:
		print("==Daftar tugas anda==")
		print("Anda tidak memiliki tugas yang bisa di hapus untuk saat ini.")
	else:
		print("==Daftar tugas anda==")
		for nomor, daftar in enumerate(tugas1):
			print(f"{nomor + 1}. {daftar}")
		data = int(input("Silahkan pilih tugas yang ingin dihapus: ")) -1
		if data > nomor:
			print("Nomor yang anda masukkan tidak valid!")
		else :
			tugas1.pop(data)
			print(f"Tugas nomor {data + 1} berhasil dihapus!")
	while True:
		pilihan = input("Ketik q untuk kembali: ")
		if pilihan != "q":
			print("Anda tidak mengetik q!")
			time.sleep(1)
		else:
			print("Anda kembali ke menu utama!")
			time.sleep(1)
			break
		

def lihat_tugas(tugas1):
	print("==Daftar tugas anda==")
	for nomor, daftar in enumerate(tugas1):
		print(f"{nomor + 1}. {daftar}")
	if tugas1 == []:
		print("Anda belum memiliki tugas untuk saat ini.")
	while True:
		pilihan = input("Ketik q untuk kembali: ")
		if pilihan != "q":
			print("Anda tidak mengetik q!")
			time.sleep(1)
		else:
			print("Anda kembali ke menu utama!")
			time.sleep(1)
			break

def keluar():
	print("Program akan dihentikan dalam..")
	time.sleep(1)
	print("3..")
	time.sleep(1)
	print("2..")
	time.sleep(1)
	print("1..")
	time.sleep(1)
	print("Program dihentikan")



def main():
	print("===to-do list===")
	print("1. Tambah tugas")
	print("2. Lihat semua tugas")
	print("3. Hapus tugas")
	print("4. Keluar")


while True:
	main()
	try:
		pilihan = int(input("Silahkan pilih nommor yang ada dimenu: "))
		if pilihan > 4:
			print("Nomor tidak valid")
		elif pilihan == 1:
			tambah_tugas(tugas)
		elif pilihan == 2:
			lihat_tugas(tugas)
		elif pilihan == 3:
			hapus_tugas(tugas)
		elif pilihan ==4:
			keluar()
			break
	except ValueError:
		print("Harus memasukkan nomor!")

