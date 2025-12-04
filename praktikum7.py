""
class Person:
	def __init__(self, nama: str):
		self.nama = nama
		self.alamat = ""
		self.__umur = 0  # atribut private

	def cetak(self) -> None:
		print(f"\nNama: {self.nama}\nAlamat: {self.alamat}")

	def __cek_umur(self) -> str:
		return "sudah dewasa" if self.__umur > 17 else "belum dewasa"

	@property
	def umur(self) -> int:
		return self.__umur

	@umur.setter
	def umur(self, value: int) -> None:
		if not isinstance(value, int) or value < 0:
			raise ValueError("Umur harus berupa bilangan bulat >= 0")
		self.__umur = value


class Mahasiswa(Person):
	def __init__(self, nim: str, nama: str):
		# memanggil konstruktor parent untuk inisialisasi nama, alamat, umur
		super().__init__(nama)
		self.nim = nim

	def cetak_nama(self) -> None:
		# contoh method khusus Mahasiswa
		print(f"Nama Mahasiswa: {self.nama}")

	# overriding contoh: cetak data lengkap (menggunakan property umur)
	def cetak_data(self) -> None:
		print(
			f"\nNIM: {self.nim}\nNama: {self.nama}\nAlamat: {self.alamat}\nUmur: {self.umur}"
		)


def demo():
	# membuat instance Mahasiswa sesuai contoh slide
	mhs1 = Mahasiswa('312510157', 'M.Ridwan Almahri')
	mhs1.umur = 19
	mhs1.alamat = "Bekasi"
	# memanggil method cetak_nama (sesuai slide)
	mhs1.cetak_nama()
	# cetak data lengkap
	mhs1.cetak_data()


if __name__ == '__main__':
	demo()

