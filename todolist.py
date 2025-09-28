import time
tugas = []
def tambah_tugas(tugas1):
	tugas2 = input("Tulis tugas yang ingin di tambahkan: ")
	tugas1.append(tugas2)
	print("Tugas anda berhasil di tambahkan!")
	time.sleep(1)

def hapus_tugas(tugas1):
	print("==Daftar tugas anda==")
	for nomor, daftar in enumerate(tugas1):
		print(f"{nomor + 1}. {daftar}")
	data = int(input("Silahkan pilih tugas yang ingin di hapus: ")) - 1
	tugas1.pop(data)
	print(f"Tugas nomor {data + 1} berhasil di hapus!")
	time.sleep(1)
		

def lihat_tugas(tugas1):
	print("==Daftar tugas anda==")
	for nomor, daftar in enumerate(tugas1):
		print(f"{nomor + 1}. {daftar}")

def keluar():
	print("Program akan di hentikan dalam..")
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
		pilihan = int(input("Silahkan pilih nommor yang ada di menu: "))
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

