def penjumlahan():
	a = int(input("masukkan angka:"))
	b = int(input("di tambah: "))
	hasil = a + b 
	print(f"hasil: {hasil}")

def pengurangan():
	a = int(input("masukkan angka: "))
	b = int(input("di kurang: "))
	hasil = a - b
	print(f"hasil: {hasil}")

def perkalian():
	a = int(input("masukkan angka: "))
	b = int(input("di kali: "))
	hasil = a * b
	print(f"hasil: {hasil} " )

def pembagian():
	a = int(input("masukkan angka: "))
	b = int(input("di bagi: "))
	hasil = a % b
	print(f"hasil: {hasil} ")


def main():
	print("===kalkulator===")
	print("1. penjumlahan")
	print("2. pengurangan")
	print("3. perkalian")
	print("4. pembagian")
	print("5. keluar")

while True:
	main()
	try:
		pilihan = int(input("silahkan pilih: "))
		if pilihan > 5:
			print("angka tidak valid")
			tanya = input("Enter untuk lanjut..")
		elif pilihan == 1:
			penjumlahan()
			tanya = input("Enter untuk lanjut..")
		elif pilihan == 2:
			pengurangan()
			tanya = input("Enter untuk lanjut..")
		elif pilihan == 3:
			perkalian()
			tanya = input("Enter untuk lanjut..")
		elif pilihan == 4:
			pembagian()
			tanya = input("Enter untuk lanjut..")
		elif pilihan == 5:
			print("program selesai")
			break
	except ValueError:
		print("tidak valid, harus memasukkan angka!")

