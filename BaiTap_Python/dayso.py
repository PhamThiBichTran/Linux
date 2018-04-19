#!/usr/bin/python
n= input('nhap so nguyen n= ')
for i in range (1, n+1):
       print'%d  '%(i)
s=0
for i in range (1, n+1):
      if(i%2==0):
           s=s+i	
print'tong cac so chan s=%d' %(s)
