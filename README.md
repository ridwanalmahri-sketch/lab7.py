Deskripsi Program
Program ini adalah implementasi sederhana dari sistem manajemen data mahasiswa menggunakan Pemrograman Berorientasi Objek (OOP) dalam Python. Program ini mendemonstrasikan penggunaan class dan method untuk menyimpan serta menampilkan informasi mahasiswa.

Langkah-Langkah Pembuatan Program
1. Membuat Class Mahasiswa
```
python
def __init__(self, nim, nama):
...
```
Class Mahasiswa adalah blueprint untuk membuat objek mahasiswa.
Method __init__ adalah constructor yang dipanggil saat objek dibuat.
Parameter nim dan nama wajib diisi saat membuat objek.
Atribut umur dan alamat diinisialisasi dengan nilai default.
2. Membuat Method cetak_nama()
python
2 lines
Copy code
Download code
Click to expand
def cetak_nama(self):
print(f"Nama Mahasiswa: {self.nama}")
Method ini mencetak nama mahasiswa.
Menggunakan self untuk mengakses atribut nama dari objek.
3. Membuat Method cetak_data()
python
5 lines
Copy code
Download code
Click to expand
def cetak_data(self):
print(f"NIM: {self.nim}")
...
Method ini mencetak semua data mahasiswa secara lengkap.
Menampilkan NIM, Nama, Alamat, dan Umur.
4. Membuat Instance/Object dalam Function demo()
python
5 lines
Copy code
Download code
Click to expand
def demo():
# membuat instance Mahasiswa sesuai contoh slide
...
Membuat objek mhs1 dari class Mahasiswa.
Mengisi NIM dan nama saat pembuatan objek.
Mengubah nilai atribut umur dan alamat setelah objek dibuat.
5. Memanggil Method dari Object
python
5 lines
Copy code
Download code
Click to expand
# memanggil method cetak_nama (sesuai slide)
mhs1.cetak_nama()
...
Memanggil method cetak_nama() untuk mencetak nama mahasiswa.
Memanggil method cetak_data() untuk mencetak semua informasi.
6. Menjalankan Program
python
2 lines
Copy code
Download code
Click to expand
if __name__ == '__main__':
demo()
Memastikan function demo() hanya dijalankan jika file ini dieksekusi langsung.
Tidak akan dijalankan jika file diimport sebagai modul.
Output Program

Copy code
Nama Mahasiswa: M.Ridwan Almahri
NIM: 312510157
Nama: M.Ridwan Almahri
Alamat: Bekasi
Umur: 19
Konsep OOP yang Digunakan
Encapsulation: Data dan method digabungkan dalam satu class.
Class: Template untuk membuat objek (Mahasiswa).
Object: Instance dari class (mhs1).
Attributes: Properti objek (nim, nama, umur, alamat).
Methods: Fungsi yang dimiliki objek (cetak_nama, cetak_data).
Cara Menjalankan Program
Pastikan Python sudah terinstall (Python 3.x).
Buka terminal/command prompt.
Navigate ke folder yang berisi file praktikum7.py.
Jalankan perintah:

 
python praktikum7.py
Pengembangan Lebih Lanjut
Program ini dapat dikembangkan dengan menambahkan:

Method untuk mengubah data mahasiswa.
Validasi input NIM dan nama.
Menyimpan data ke file atau database.
Menambah atribut lain seperti jurusan, IPK, dll.
Membuat list untuk menyimpan banyak mahasiswa.
Method untuk mencari mahasiswa berdasarkan NIM.
Flowchart
```
START
  |
  |---> [Define Class Mahasiswa]
  |           - attributes: nim, nama, umur, alamat
  ```
methods: init, cetak_nama, cetak_data
```
---> if name == 'main'


        +---> CALL demo()
                  |
                  +---> mhs1 = Mahasiswa('312510157', 'M.Ridwan Almahri')
                  |
                  +---> mhs1.umur = 19
                  |
                  +---> mhs1.alamat = "Bekasi"
                  |
                  +---> CALL mhs1.cetak_nama()
                  
```

                  +---> CALL mhs1.cetak_data()
                            -> prints NIM, Nama, Alamat, Umur
                  |
                  `---> RETURN from demo()
        |
`---> END


**Penjelasan singkat:**
- Blok "Define Class" hanya mendefinisikan struktur kelas (tidak dieksekusi sebagai aksi runtime sampai dipakai).
- Kondisi `if __name__ == '__main__'` menjalankan fungsi `demo()` saat file dijalankan langsung.
- `demo()` membuat instance Mahasiswa, menetapkan atribut, lalu memanggil method untuk menampilkan data.

