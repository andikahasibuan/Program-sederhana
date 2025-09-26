tugas = []
def tambah_tugas(tugas1):
	tugas2 = input("tambahkan tugas: ")
	tugas1.append(tugas2)
	print("tugas berhasil di tambahkan")

def hapus_tugas(tugas1):
	for daftar in tugas1:
		print(daftar)
		data = input("pilih nomor yang ingin dihapus: ")
		print("tugas berhasil di hapus")
		

def lihat_tugas():
	tugas = []
	for i in tugas:
		print(i)


def main():
	print("===todo-list===")
	print("1. tambah tugas")
	print("2. hapus tugas")
	print("3. lihat tugas")
	print("4 keluar")


while True:
	main()
	pilihan = int(input("pilih no berapa: "))
	if pilihan > 4:
		print("nomor tidak valid")
	elif pilihan == 1:
		tambah_tugas(tugas)
	elif pilihan == 2:
		hapus_tugas(tugas)
	elif pilihan == 3:
		lihat_tugas(tugas)
	elif pilihan ==4:
		break
	else:
		print("kosong")


