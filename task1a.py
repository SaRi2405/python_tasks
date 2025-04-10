# 1) 123 rəqəmini string/character ə çevirin və tipini yoxlayın.
num = 123
str_num = str(num)
print(str_num, type(str_num))  # '123' <class 'str'>

# 2) 19.99 dəyərini tam ədədə çevirin və nəticəni çap edin.
flt = 19.99
int_flt = int(flt)
print(int_flt)  # 19

# 3) "500" dəyərini numericə çevirin və 2-yə bölüb nəticəni çap edin.
text_num = "500"
num_val = int(text_num)
print(num_val / 2)  # 250.0

# 4) a = 8 və b = 12 yaradın. a < b və a == b şərtlərini yoxlayın, nəticələri çap edin.
a = 8
b = 12
print(a < b)   # True
print(a == b)  # False

# 5) x = 5, y = 10, z = 15 yaradın. (x < y) and (y < z) şərtini yoxlayın və nəticəni çap edin.
x = 5
y = 10
z = 15
print((x < y) and (y < z))  # True

# 6) 25-i 4-ə bölün. Tam bölmə, qalıq və adi bölmə nəticələrini çap edin.
tam = 25 // 4
qaliq = 25 % 4
bolme = 25 / 4
print("Tam bölmə:", tam)       # 6
print("Qalıq:", qaliq)         # 1
print("Adi bölmə:", bolme)    # 6.25

# 7) 3-ü 4-cü dərəcəyə qaldırın və nəticəni çap edin.
quvvet = 3 ** 4
print(quvvet)  # 81

# 8) qiymet = 75.5 yaradın. Onu tam ədədə çevirin və tipini yoxlayın.
qiymet = 75.5
qiymet_int = int(qiymet)
print(qiymet_int, type(qiymet_int))  # 75 <class 'int'>

# 9) n = 20 yaradın. (n > 10) or (n < 5) və (n > 15) and (n < 25) şərtlərini yoxlayın, nəticələri çap edin.
n = 20
print((n > 10) or (n < 5))         # True
print((n > 15) and (n < 25))       # True

# 10) "42.8" dəyərini əvvəl float-a, sonra tam ədədə çevirin və hər addımda tipi yoxlayın.
val = "42.8"
val_float = float(val)
print(val_float, type(val_float))  # 42.8 <class 'float'>
val_int = int(val_float)
print(val_int, type(val_int))      # 42 <class 'int'>
