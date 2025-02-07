#print("Hello")

#import time
#print(time.ctime())

#z = "Hello"
#y = 20
#c = 30,9
#f = ["Apple" , "berry"] #ini string, karenan ditandain dengan pake kurung siku sama tanda petik dua

#print(z,y,c,f) #kalau f[0] yang muncul cmn apple


#o = int(1) #buta ngubah tipe data ke integer
#y = int(2.8) # kalau ini awalnya kan float yak, dgn tambahin int, barti tipe data diubah ke integer
#z = int("3") # kalau ini dari string ke integer
#j = str(20) # kalau ini dari integer ke string

#print(o,y,z,j)


#a = "Hello"
#b = "World"
#c = a + b
#print(c)


#a = "Hello World"
#print(a[1]) # itu kan index 1, kok keluarnya e? kalau dikomputer huruf pertama atau kata pertama itu dibaca 0, jadi kalau 1, maka yang dibaca huruf ke-2
#print(len(a)) #buat print panjang isi dari variabel a atau string a


#b = "BINUS Univ"
#print(b[2:5]) #ini buat keluarin nilai di dalam index ke-2 smpe ke-5

#c = "BINUS Univ"
#print(c[:5]) # ini buat keluarin nilai di index 0 smpe ke-5

#d = "BINUS Univ"
#print(d[5:]) # ini buat keluarin nilai di index ke-5 smpe terakhir 


#a = "Hello"
#print(a.upper()) #buat ubah huruf kecil jadi besar

#b = "Hello"
#print(b.lower()) #buat ubah huruf besar jadi kecil

#c = "Hello"
#print(c.replace("H","J")) #buat ganti huruf H jadi J


#9
#nama = "Sam"
#x = 19
#string = "nama saya {} umur {}" #ini buat string format
#print(string.format(nama,x)) #ini buat format stringnya, jadi nanti misalkan nama diisni pertama gtu, kalau misalkan 'x' sama 'nama' dibalik hasil output bakal beda


#10 
#nama = "Sindy"
#for i in enumerate(nama): #ini buat bikin index dan isi stringnya , i itu index kek (int i di C), 
                          #trus kalau enumerate itu kek loop gtu, jadi baka ngulang sebanyak panjang kata

#    print(i) #ini buat print index dan isi stringnya ( atau valuenya atau nilainya )

#11
#def perbandingan(a,b): # a dgn b itu kek parameter kek nilai yang kita lempar gitu   
#    if a > b: 
#       print("a lebih besar dari b")
#    elif a < b: #elif itu kek else if
#        print("a lebih kecil dari b")
#    else: print("a sama dengan b")

#perbandingan(5,9) #ini buat contoh inputnya

    
#12
#i = 1
#while i < 6: #ini looping gtu
#    print(i)
#    i+=1


#13
#i = 1 # ini keknya ga ngaruh, soalnya bakal ketutupan dengan nilai 'i' dari loop
#for i in range(2,6): #ini looping gtu, range itu kek dari 0 sampai 5
#    print(i)


#14
#for i in range(2,40): # ini dalam rentang 2-40, cari nilai genap dengan ganjil, ini cuman dari 2-39 yang di cek, 40 nggak
#    if(i % 2 == 0): # ini buat ngecek apakah nilai i itu genap atau nggak
#        print(i ,  "Genap")
#    elif(i % 2 != 0): # kalai pake elif, harus ada statementnya
#    else : # ini kan pakai else
#        print(i , "Ganjil")


#15
#import numpy as np # manggil library numpy, trus np itu kek nama singkatnya dah
#x = np.array([[1, 2, 3] , [4, 5, 6]]) # ini buat array, array itu kek list tapi bisa diakses dengan index
#x