#Kegiatan 1
get = open('L200190188', 'w')

nim = input('Masukkan NIM : ')
ttl = input('Masukkan Tanggal Lahir (DD-MM-YYYY) : ')
nama = input('Masukkan Nama Lengkap : ')
get.writelines('{}\n{}\n{}'.format(ttl,nim,nama))

get.close()

#Kegiatan 2
get = open('L200190188', 'a')
readln = open('L200190188', 'r')

kota = input('Masukkan Nama Kota Asal : ')

get.writelines('\n{}'.format(kota))

string = ' '

#convert
ttl = open('L200190188', "r").readlines()[0]
tanggal = ttl[3:5]+'/'+ttl[0:2]+'/'+ttl[6:10]

nama = open('L200190188', "r").readlines()[2]
nim = open('L200190188', "r").readlines()[1]

print('''
{}
{},{}
{}
'''.format(nama,kota,tanggal,nim))

get.close()

#Kegiatan 3-4
import shelve

F = shelve.open("L200190188.data")
F["nim"]  = ('L200190188')
F["ttl"]  = ('26-06-01')
F["nama"] = ('Daffa Zufar F')
F["kota"] = ('Solo')
F.close

F = shelve.open("L200190085.data")
print("NIM  : ", F["nim"])
print("TTL  : ", F["ttl"])
print("Nama : ", F["nama"])
print("Kota : ", F["kota"])
nim = F["nim"]
print(F["nama"])
F.close()
