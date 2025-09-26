def tambah_tugas(tugas):
	tugas1 = input("tambahkan tugas: ")
	tugas.append(tugas1)

def hapus_tugas(tugas):
	hapus = input("pilih tugas: ")
	tugas.pop(hapus)

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
	tugas = []
	main()
	pilihan = int(input("pilih no berapa: "))
	if pilihan > 4:
		print("nomor tidak valid")
	elif pilihan == 1:
		tambah_tugas(tugas)
	elif pilihan == 2:
		hapus_tugas()
	elif pilihan == 3:
		lihat_tugas()
	elif pilihan ==4:
		break
	else:
		print("kosong")


