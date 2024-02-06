from IPython.display import display, Math
import matplotlib.pyplot as plt
import os

os.system('clear')


"""
MENULIS FOORMULA MATEMMATIS PADA PYTHON 
"""

x = 5
y = 10
z = 2


# MENGGUNAKAN FORMAT VERSI LAMA 
# 1. %s UNTUK STRING
# 2. %d UNTUK DIGIT ATAU BIALNGAN BULAT
# 3. %f UNTUK BILANGAN FLOAT
# 4. #g UNTUK BILANGAN FLOAT YANG MEMILIKI BANYAK ANGKA DIBELAKANG KOMA


# STUDI KASUS :
operasi1 = 5 * x * ( 5 + y )
display(Math(f"5x(5+y) = %d" %operasi1))

operasi2 = -y - ((x-2)/z)
display(Math(f"-y - \\frac {x-2}{z} = %g" %operasi2)) # \\frac BENTUK FORMAT PEMBAGIAN 

# PEMANGKATAN :
# CONTOH 1 :
display(Math(f"3^3 = {3**2}")) # (^) MERUPAKAN SIBOL PANGKAT PADA FUNGSI MATH BUKAN XORS 

# CONTOH 2 :
display(Math(f"3^2 \\times 3^3 = 3^5")) # \\times BENTUK SIMBOL PERKALIAN (X)


# STUDI KASUS :
a = 5
b = 5.1

soal1 = a**(3/4) * 4**b
display(Math(f"x^{3/4} \\times 4^b = %g" %soal1))

soal2 = 3**3 / a**b
display(Math(f"\\frac {3^3}{a^b} = %g" %soal2))

soal3 = 10**(a-4)
display(Math(f"10^{a-4} = %g" %soal3))