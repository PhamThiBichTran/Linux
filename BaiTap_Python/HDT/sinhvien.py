class SinhVien:
	def __init__(self,ten,namsinh,khoa):
		self.ten = ten
		self.namsinh = namsinh
		self.khoa = khoa
	def set_ten(self, sTen):
		self.ten = sTen
	def get_ten(self):
		return self.ten
	def set_namsinh(self,sNamSinh):
		self.namsinh = sNamSinh
	def get_namsinh(self):
		return self.namsinh
	def set_khoa(self,sKhoa):
		self.khoa = sKhoa
	def get_khoa(self):
		return self.khoa
	def tostring(self):
		print"%s - %6s - %6s" %(self.ten,self.namsinh,self.khoa)
		return 0


