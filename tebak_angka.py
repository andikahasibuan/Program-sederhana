import random

def tebak_angka():
	while True:
		angka_random = random.randint(1, 5)
		pilihan = int(input("Silahkan tebak, angka berapa yang akan muncul dari 1-5:"))
		if pilihan > 5:
			print("Angka yang anda masukkan tidak valid!")
		elif pilihan != angka_random:
			print("Anda salah menebak angka!")
		else:
			print("Selamat anda berhasil menebak dengan benar!")
		pilihan1 = input("ingin lanjut [y/n]?: ")
		if pilihan1 == "y":
			return tebak_angka()
		elif pilihan1 == "n":
			print("Anda kembali ke menu utama")
			break			

def keluar():
	print("Terimah kasih sudah bermain")


def main():
	print("Selamat datang di game tebak angka!")
	print("1. Mulai")
	print("2. Keluar")

while True:
	main()
	try:
		pilihan = int(input("Silahkan pilih: "))
		if pilihan > 2:
			print("Angka yang anda masukkan tidak valid!")
		elif pilihan == 1:
			tebak_angka()
		elif pilihan == 2:
			keluar()
			break
		else:
			print("Pilihan anda tidak valid!")
	except ValueError:
		print("Input yang anda masukkan tidak valid!")