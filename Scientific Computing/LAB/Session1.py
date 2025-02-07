def calculate(uas, uts, asg): #Function buat hitung nilai, kenapa ada (uas, uts, asg) itu buat nampung variabel dri main di bwah
     return uas * 0.5 + uts * 0.3 + asg * 0.2


def grading(total): #Fungsi grading atau liat nilai
    if 90 <= total <= 100:
        return "A"
    elif 85 <= total < 90: # inget ya elif itu perlu condition
        return "A-"
    elif 80 <= total < 85:
        return "B+"
    elif 75 <= total < 80:
        return "B"
    elif 70 <= total < 75:
        return "C+"
    elif 60 <= total < 70:
        return "C"
    else: # else g perlu condition
        return "F"


Username = input("Masukkan username anda : ") # input ini gunanya buat nerima input user
Password = input("Masukkan passwrod anda : ")

if  Password == "Admin123":
    
    print(f"\nLogin Berhasil, Selamat datang {Username}" ) # nah ini knp ada 'f' itu buat ksih tau programbuat ambil data di variabel dalam {}
else :
    print("\nInvalid Password. Please Re-enter your Password! ")
    Username = input("Username : ")
    Password = input("Passwrod : ")


student_name = input("Masukkan nama siswa : ")
uas = float(input("Masukkan nilai UAS : ")) # ada float buat nandain kalau itu tipe data float, tpi masuknya disitu buat seperti C
uts = float(input("Masukkan nilai UTS : "))
asg = float(input("Masukkan nilai Assignment :"))

total = calculate(uas, uts, asg) # nah ini, yang ku bilang lempar variabel dari main, ini dia lembar data yag ada dalam variabel yang ditulis dalam tanda kurung
grade = grading(total)

print(f"\nHasil perolehan nilai {student_name}")
print(f"Final Score: {total}")
print(f"Grade {grade}")








