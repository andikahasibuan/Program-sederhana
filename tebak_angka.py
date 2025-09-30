import random

def tebak_angka():
	angka_random = random.randint(1, 5)
	pilihan = int(input("Silahkan tebak, angka berapa yang akan muncul dari 1-5:"))
	if pilihan > 10:
		print("Angka yang anda masukkan tidak valid!")
	elif pilihan == angka_random:
		print("Selamat anda berhasil menebak dengan benar!")
	elif pilihan != angka_random:
		print("Anda salah menebak angka!")

def keluar():
	print("Terimah kasih sudah bermain")


def main():
	print("Selamat datang di game tebak angka!")
	print("1. Mulai")
	print("2. Keluar")

while True:
	main()
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