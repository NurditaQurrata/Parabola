print("====================FUNGSI PARABOLA====================")
import math
a=int(input("Masukkan nilai a: "))
b=int(input("Masukkan nilai b: "))
c=int(input("Masukkan nilai c: "))
print("y = ax^2 + bx + c")
print("y =",a,"x^2 +",b,"x +",c)
D = b**2 - 4*a*c
if D > 0 and a > 0:
    x1=(-b * +(math.sqrt (D))) / 2*a
    x2=(-b * -(math.sqrt (D))) / 2*a
    print("parabola terbuka ke atas , dan memiliki 2 titik potong dengan sumbu x yaitu (%1.2f" %x1,",0)", "dan (%1.2f" %x2,",0)")
elif D == 0 and a > 0:
    x=-b/2*a
    print("parabola terbuka ke atas , dan menyinggung sumbu x pada (%1.2f" %x,",0)")
elif D < 0 and a > 0:
    print("parabola terbuka ke atas , dan tidak memiliki titik potong dengan sumbu x")
elif D > 0 and a < 0:
    x1=(-b* +(math.sqrt (D))) / 2*a
    x2=(-b* -(math.sqrt (D))) / 2*a
    print("parabola terbuka ke bawah , dan memilik 2 titik potong dengan sumbu x yaitu (%1.2f" %x1,",0)", "dan (%1.2f" %x2,",0)")
elif D == 0 and a < 0:
    x=-b/2*a
    print("parabola terbuka ke bawah , dan menyinggung sumbu x pada (%1.2f" %x,",0)")
elif D < 0 and a < 0:
    print("parabola terbuka ke bawah , dan tidak memiliki titik potong dengan sumbu x")
else:
    print("Tidak memenuhi syarat/kriteria dari grafik parabola Bentuk y = ax^2 + bx + c")
