# 1.) code / decode / latin1

b = b'r\xc3\xa9sum\xc3\xa9'
s = b.decode('utf-8') # преобразование в строку
a = b.decode('utf-8').encode('latin1') # преобразование 
                                       #в байтовый вид latin1 
c = a.decode('latin1') # декодировал обратно в строку



print(s)
print(a)
print(c)

#§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§§

