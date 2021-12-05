print("========= Latihan 1 - Dictionary =========")
print()
s={'Ari': '0895767999', 'Dina': '081288886'}
print("Daftar Kontak :\n", s)
print()

#Menampilkan kontak
print("Menampilkan kontak Ari :", s['Ari'])
print("=========================================================================================")

#Menambah Kontak Baru
print("Menambah Kontak Baru\n")
print("Daftar Kontak sebelum ditambah :\n", s)
s['Riko']='081354587';
print("Daftar Kontak setelah ditambah :\n", s)
print("=========================================================================================")

#Mengubah Kontak
print("Mengubah Kontak\n")
print("Daftar Kontak sebelum diubah :\n", s)
s['Dina']='088960779';
print("Daftar Kontak setelah diubah :\n", s)
print("=========================================================================================")

#Menampilkan Semua Nama Kontak
print("Menampilkan Semua Nama Kontak :\n")
print(s.keys())
print("=========================================================================================")

#Menampilkan Semua Nomor Kontak
print("Menampilkan Semua Nomor Kontak :\n")
print(s.values())
print("=========================================================================================")

#Menampilkan Seluruh Daftar Kontak Beserta Nomor Telp
print("Daftar Kontak :\n")
print(s.items())
print("=========================================================================================")

#Menghapus Kontak Dina
print("Menghapus salah satu kontak\n")
print("Daftar Kontak sebelum dihapus :\n", s)
del s['Dina'];
print("Daftar Kontak setelah dihapus :\n", s)