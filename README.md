Dokumentasi Program Mahasiswa - praktikum7.py
Deskripsi Program
Program ini adalah implementasi sederhana dari sistem manajemen data mahasiswa menggunakan Pemrograman Berorientasi Objek (OOP) dalam Python. Program ini mendemonstrasikan penggunaan class dan method untuk menyimpan serta menampilkan informasi mahasiswa.
Langkah-Langkah Pembuatan Program
1. Membuat Class Mahasiswa
pythonclass Mahasiswa:
```
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
        self.umur = 0
        self.alamat = ""
```
Class Mahasiswa adalah blueprint untuk membuat objek mahasiswa
Method __init__ adalah constructor yang dipanggil saat objek dibuat
Parameter nim dan nama wajib diisi saat membuat objek
Atribut umur dan alamat diinisialisasi dengan nilai default

2. Membuat Method cetak_nama()
pythondef cetak_nama(self):
    print(f"Nama Mahasiswa: {self.nama}")

Method ini mencetak nama mahasiswa
Menggunakan self untuk mengakses atribut nama dari objek

3. Membuat Method cetak_data()
```
pythondef cetak_data(self):
    print(f"NIM: {self.nim}")
    print(f"Nama: {self.nama}")
    print(f"Alamat: {self.alamat}")
    print(f"Umur: {self.umur}")
```
Method ini mencetak semua data mahasiswa secara lengkap
Menampilkan NIM, Nama, Alamat, dan Umur

4. Membuat Instance/Object dalam Function demo()
pythondef demo():
    # membuat instance Mahasiswa sesuai contoh slide
```
    mhs1 = Mahasiswa('31251@157', 'M.Ridwan Almahri')
    mhs1.umur = 19
    mhs1.alamat = "Bekasi"
```
Membuat objek mhs1 dari class Mahasiswa
Mengisi NIM dan nama saat pembuatan objek
Mengubah nilai atribut umur dan alamat setelah objek dibuat

5. Memanggil Method dari Object
python    # memanggil method cetak_nama (sesuai slide)
    mhs1.cetak_nama()
    
    # cetak data lengkap
    mhs1.cetak_data()

Memanggil method cetak_nama() untuk mencetak nama mahasiswa
Memanggil method cetak_data() untuk mencetak semua informasi

6. Menjalankan Program
pythonif __name__ == '__main__':
    demo()
```
- Memastikan function `demo()` hanya dijalankan jika file ini dieksekusi langsung
- Tidak akan dijalankan jika file diimport sebagai modul

## Output Program
```
```
Nama Mahasiswa: M.Ridwan Almahri
NIM: 31251@157
Nama: M.Ridwan Almahri
Alamat: Bekasi
Umur: 19
```
Konsep OOP yang Digunakan

Encapsulation: Data dan method digabungkan dalam satu class
Class: Template untuk membuat objek (Mahasiswa)
Object: Instance dari class (mhs1)
Attributes: Properti objek (nim, nama, umur, alamat)
Methods: Fungsi yang dimiliki objek (cetak_nama, cetak_data)

Cara Menjalankan Program

Pastikan Python sudah terinstall (Python 3.x)
Buka terminal/command prompt
Navigate ke folder yang berisi file praktikum7.py
Jalankan perintah:

bash   python praktikum7.py
Pengembangan Lebih Lanjut
Program ini dapat dikembangkan dengan menambahkan:

Method untuk mengubah data mahasiswa
Validasi input NIM dan nama
Menyimpan data ke file atau database
Menambah atribut lain seperti jurusan, IPK, dll
Membuat list untuk menyimpan banyak mahasiswa
Method untuk mencari mahasiswa berdasarkan NIM

FLOWCHART 
```
START
  |
  |---> [Define Class Person]
  |           - attributes: nama, alamat, __umur (private)
  |           - methods: cetak(), __cek_umur(), property umur (getter/setter)
  |
  |---> [Define Class Mahasiswa (inherits Person)]
  |           - attributes: nim
  |           - methods: cetak_nama(), cetak_data() (overriding)
  |
  |---> if __name__ == '__main__'
            |
            +---> CALL demo()
                      |
                      +---> mhs1 = Mahasiswa('312510157', 'M.Ridwan Almahri')
                      |         (calls Person.__init__ via super())
                      |
                      +---> mhs1.umur = 19
                      |         (setter memvalidasi umur >= 0)
                      |
                      +---> mhs1.alamat = "Bekasi"
                      |
                      +---> CALL mhs1.cetak_nama()
                      |         -> prints "Nama Mahasiswa: M.Ridwan Almahri"
                      |
                      +---> CALL mhs1.cetak_data()
                                -> prints NIM, Nama, Alamat, Umur
                      |
                      `---> RETURN from demo()
            |
  `---> END
  ```
Penjelasan singkat:

Blok "Define Class" hanya mendefinisikan struktur kelas (tidak dieksekusi sebagai aksi runtime sampai dipakai).
Kondisi if __name__ == '__main__' menjalankan fungsi demo() saat file dijalankan langsung.
demo() membuat instance Mahasiswa, menetapkan atribut, lalu memanggil method untuk menampilkan data.
