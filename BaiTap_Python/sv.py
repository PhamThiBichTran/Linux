#!/usr/bin/python
class sinhvien:
	def __init__(self,masv,hoten,makhoa):
        	self.masv = masv
        	self.hoten = hoten
        	self.makhoa = makhoa
	def printsv(self):
        	print self.masv, '\t', self.hoten, '\t', self.makhoa


class khoa:
	def __init__(self,makhoa,tenkhoa):
	     	self.makhoa = makhoa
		self.tenkhoa = tenkhoa
	def printkhoa(self):
		print self.makhoa, '\t', self.tenkhoa

sv1 = sinhvien("001","Mai A","01")
sv2 = sinhvien("002", "Tran B", "01")
sv3 = sinhvien("003", "Van C", "03")
sv4 = sinhvien("004","Thi K","001")

dssv=[]
dssv.append(sv1)
dssv.append(sv2)
dssv.append(sv3)
dssv.append(sv4)

k1 = khoa("01", "CNTT")
k2 = khoa("02", "KE TOAN")
k3 = khoa("03", "CO KHI")
k4 = khoa("04", "NUOI")

dskhoa=[]
dskhoa.append(k1)
dskhoa.append(k2)
dskhoa.append(k3)
dskhoa.append(k4)

for i in dssv:
	i.printsv()
print "\n"
for i in dskhoa:
	i.printkhoa()
print "\n"
for i in dskhoa:
	if(i.tenkhoa=="CNTT"):
		s = i.makhoa
print "\n"
for i in dssv:
	if(i.makhoa == s):
		i.printsv()
