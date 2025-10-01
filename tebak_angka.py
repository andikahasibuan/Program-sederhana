import random
import time

def tebak_angka():
	try:
		angka_random = random.randint(1, 5)
		pilihan = int(input("Silahkan tebak, angka berapa yang akan muncul dari 1-5:"))
		if pilihan > 5 or pilihan == 0:
			print("Anda hanya boleh menebak dari angka 1-5!")
		elif pilihan != angka_random:
			print("Anda salah menebak angka!, angka yang benar adalah: ", + angka_random)
		else:
			print("Selamat anda berhasil menebak dengan benar!")
	except:
		print("Anda hanya bisa memasukkan angka!")

def keluar():
	print("Anda akan keluar dalam")
	time.sleep(1)
	print("3")
	time.sleep(1)
	print("2")
	time.sleep(1)
	print("1")
	time.sleep(1)
	print("Anda keluar dari permainan.")
	time.sleep(1)
	print("Terima kasih sudah bermain!")


def main():
	print("Permain tebak angka")
	print("1. Mulai")
	print("2. Keluar")

while True:
	main()
	try:
		pilihan = int(input("Silahkan pilih: "))
		if pilihan > 2 or pilihan == 0:
			print("Angka yang anda masukkan tidak valid!")
		elif pilihan == 1:
			tebak_angka()
			while True:
				pilihan1 = input("Apakah anda ingin lanjut? [y/n]: ")
				if pilihan1 == "y":
					tebak_angka()
				elif pilihan1 == "n":
					print("Anda kembali ke menu utama!")
					time.sleep(1)
					break
				else:
					print("Anda hanya bisa menjawab y atau n!")
		elif pilihan == 2:
			keluar()
			break
	except ValueError:
		print("Anda harus memasukkan angka! ")