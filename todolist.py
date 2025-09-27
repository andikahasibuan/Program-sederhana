tugas = []
def tambah_tugas(tugas1):
	tugas2 = input("tambahkan tugas: ")
	tugas1.append(tugas2)
	lanjut = input("tekan enter untuk lanjut")
	print("tugas berhasil di tambahkan!")

def hapus_tugas(tugas1):
	for daftar in tugas1:
		print(daftar)
		data = input("pilih nomor yang ingin dihapus: ")
		print("tugas berhasil di hapus!")
		

def lihat_tugas(tugas1):
	for nomor, daftar in enumerate(tugas1):
		print(f"{nomor + 1}. {daftar}")
	lanjut = input("tekan enter untuk kembali")


def main():
	print("===to-do list===")
	print("1. tambah tugas")
	print("2. hapus tugas")
	print("3. lihat semua tugas")
	print("4 keluar")


while True:
	main()
	pilihan = int(input("silahkan pilih nommor yang ada di menu: "))
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


