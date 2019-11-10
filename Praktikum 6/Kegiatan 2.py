##Program Akun
##Dibuat oleh Daffa Zufar L200190188
import random
Angka = random.randint(0,1000)

Nama = 'Daffa Zufar Fakhriansyah'
TanggalLahir = '26 Juni 2001'
NamaSingkat = Nama[0:4] + '. ' + Nama[6] + '. ' + Nama[12:23]
Username = Nama[0] + TanggalLahir[0] + TanggalLahir[8:12]
Password = Nama[0:4] + str(Angka)
print(Username)
print(Password)
