from os import system
from prettytable import PrettyTable
import mysql.connector
from loginn import *

global cursor
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "datalaundry")
cursor = mydb.cursor()

# Linked List
class Node:
    def __init__(self,kode,id,nama,berat,harga):
        self.kode = kode
        self.id = id
        self.nama = nama
        self.berat = berat
        self.harga = harga
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.aktif = False
    
    def aktifasidb(self):
        cursor.execute("SELECT * FROM datapemesanan")
        for i in cursor:
            temp = Node(i[0],i[1],i[2],i[3],i[4])
            if self.head is None:
                self.head = temp
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = temp
        self.aktif = True
    
    def add(self):
        if self.aktif == False:
            print("harap aktifkan database terlebih dahulu")
        elif self.aktif == True:
            print("="*50) 
            kodee = input("Masukkan Kode                            : ")
            id = input("Masukkan Jenis Laundry                   : ")
            nama = input("Masukkan Nama Pelanggan                  : ")
            berat = int(input("Masukkan Laundry/Kg Pelanggan Yang Baru  : "))
            harga_per_kg = {
                "One Day Service": 8000,
                "Dry Cleaning": 7000,
                "Layanan Antar Jemput": 10000
                }

            if id in harga_per_kg:
                total_harga = harga_per_kg[id] * berat
            else:
                print("Jenis pakaian tidak tersedia.")
                total_harga = 0
            
            print("Total harga: Rp", total_harga)
            print("="*50)   
            harga = int(input("Masukkan Harga yang tertera             : "))
            sql = "INSERT INTO datapemesanan (kode, id, nama, berat, harga) VALUES (%s , %s, %s, %s, %s)"
            val = (kodee, id, nama, berat,harga)
            cursor.execute(sql, (val))
            mydb.commit()
            temp = Node(kodee,id,nama,berat,harga)
            if self.head is None:
                self.head = temp
            else:
                current = self.head
                while current.next is not None:
                    current = current.next
                current.next = temp
        
    def remove_task(self):
        if self.aktif == False:
            print("harap aktifkan database terlebih dahulu")
        elif self.aktif == True:
            sqlhps = "DELETE FROM datapemesanan WHERE kode = %s "
            kd = input("Input Kode Pelanggan Ingin Dihapus : ")
            hps = (kd,) 
            temp = self.head
            previous = None
            while temp is not None:
                if temp.kode == kd:
                    if previous is None:
                        self.head = temp.next
                    else:
                        previous.next = temp.next
                    cursor.execute(sqlhps, hps)
                    mydb.commit()
                    return True
                previous = temp
                temp = temp.next
            return True
    
    def update(self):
        if not self.aktif:
            print("harap aktifkan database terlebih dahulu")
        else:
            print("="*50)
            kode = input("Masukkan Kode Yang Ingin Diubah Datanya : ")
            sqlupt = "UPDATE datapemesanan SET id = %s, berat = %s, harga = %s WHERE kode = %s"
            if self.head is not None:
                temp = self.head
                idbaru = input("Masukkan Jenis Laundry baru              : ")
                namabaru = input("Masukkan Nama Pelanggan baru             : ")
                beratbaru = int(input("Masukkan Laundry/Kg Pelanggan Yang Baru  : "))
                harga_per_kg = {
                "One Day Service": [8000],
                "Dry Cleaning": [7000],
                "Layanan Antar Jemput": [10000]
                }

                if idbaru in harga_per_kg:
                    a = harga_per_kg[idbaru][0] * beratbaru
                else:
                    print("Jenis pakaian tidak tersedia.")
                    a = 0
            
                print("Total harga: Rp" , a)
                print("="*50)
                hargabaru = int(input("Masukkan Harga yang tertera             : "))

                while temp is not None and temp.kode != kode:
                    temp = temp.next
                        
                if temp is not None:
                    temp.id, temp.nama, temp.berat, temp.harga = idbaru, namabaru, beratbaru, hargabaru
                    cursor.execute(sqlupt, (idbaru, beratbaru, hargabaru, kode))
                    mydb.commit()
                else:
                    system("cls")
                    print(f"Kode {kode} tidak ditemukan dalam data pemesanan")
            else:
                print("data masih kosong")

    def sort_tasks(self):
        kode = []
        temp = self.head
        while temp is not None:
            kode.append(temp)
            temp = temp.next
        kode.sort(key=lambda kode: kode.kode)
        return kode
    
    def jump_search(self):
        try:
            data = input("masukkan kode laundry yang ingin di cari : ")
            # Sorting tasks by description
            tasks = self.sort_tasks()
            
            # Applying jump search algorithm
            n = len(tasks)
            jump = int(n**0.5)
            left = 0
            right = jump
            
            while right < n and tasks[right].kode <= data:
                left = right
                right += jump
            
            for i in range(left, min(right,n)):
                if tasks[i].kode == data:
                    return tasks[i]
            return None
        except ValueError and KeyboardInterrupt:
            print("<<< harap input data yang benar >>>")

    def showll(self):
        if self.aktif == False:
            print("harap aktifkan database terlebih dahulu")
        else:
            temp = self.head
            tabel = PrettyTable(["kode","id","nama","berat","harga"])
            tabel.clear_rows()
            while temp is not None:
                tabel.add_row([temp.kode,temp.id,temp.nama,temp.berat,temp.harga])
                temp = temp.next
            print(tabel)

    # Merge Sorting
    def mergeSort(self,array):
        if len(array) > 1:
            center = round(len(array)/2)
            sublist_kiri = array[:center]
            sublist_kanan = array[center:]
            self.mergeSort(sublist_kiri)
            self.mergeSort(sublist_kanan)
            data_kiri = len(sublist_kiri);  
            data_kanan = len(sublist_kanan)
            i = j = k = 0
            while i < data_kiri and j < data_kanan:
                if sublist_kiri[i] < sublist_kanan[j]:
                    array[k] = sublist_kiri[i]
                    i = i + 1
                else:
                    array[k] = sublist_kanan[j]
                    j = j + 1
                k = k + 1
            while i < len(sublist_kiri):
                array[k] = sublist_kiri[i]
                i = i + 1
                k = k +  1
            while j < len(sublist_kanan):
                array[k] = sublist_kanan[j]
                j = j +  1
                k = k +  1
        return array

    def SortLaun(array):
        for i in range(len(array)):
            print(array[i], end=" ")

    def sort(self):
        ulang1 = "y"
        while(ulang1 == "y" or True):
            print("""
            +===================================+
            |       Sorting Data Laundry        |
            +===================================+
            | 1 | Sorting data ID pelanggan     |
            | 2 | Sorting data laundry          |
            | 3 | Sorting data berat laundry    |
            | 4 | Menu sebelumnya               |
            +===================================+
            """)
            while True:
                try:
                    pilih = int(input("\nPilihan => "))
                    break
                except:
                    print("Gunakan Angka Saat Menginput Pilihan\n")
                    system("cls")
                    continue

            if pilih == 1:
                system("cls") 
                cursor.execute("SELECT * FROM datapemesanan ")
                array = [int(i[0]) for i in cursor.fetchall()]
                terurut = self.mergeSort(array)
                print("Data ID Pelanggan Terurut : ")
                tabelurut = PrettyTable(["kode"])
                for i in terurut:
                    tabelurut.add_row([i])
                print(tabelurut)
                print("\n")
                continue

            elif pilih == 2:  
                system("cls") 
                cursor.execute("SELECT * FROM datapemesanan ")
                array = [str(i[2]) for i in cursor.fetchall()]
                terurut = self.mergeSort(array)
                print("Data Nama Pelanggan Terurut : ")
                tabelurut = PrettyTable(["kode"])
                for i in terurut:
                    tabelurut.add_row([i])
                print(tabelurut)
                print("\n")
                continue
        
            elif pilih == 3:
                system("cls") 
                cursor.execute("SELECT * FROM datapemesanan ")
                array = [int(i[3]) for i in cursor.fetchall()]
                terurut = self.mergeSort(array)
                print("Data ID Pelanggan Terurut : ")
                tabelurut = PrettyTable(["kode"])
                for i in terurut:
                    tabelurut.add_row([i])
                print(tabelurut)
                print("\n")
                continue

            elif pilih == 4:
                self.laundry()
            else:
                print("Pilihan Tidak Tersedia")
                ulang1 = input("Apakah Ingin Mengulang? (y/n) :")
                if ulang1 == "y":
                    self.sort()
                    continue
                else:
                    print("\nTerimakasih Sudah Menggunakan Program Layanan Dream Laundry")
                    quit()


def gainAccess(Username=None, Password=None):
    Username = input("Masukkan Username anda: ")
    Password = input("Masukkan Password anda: ")
    
    if not len(Username or Password) < 1:
        if True:
            db = open("datalogin.txt", "r")
            d = []
            f = []
            for i in db:
                a,b = i.split(",")
                b = b.strip()
                c = a,b
                d.append(a)
                f.append(b)
                data = dict(zip(d, f))
            try:
                if Username in data:
                    hashed = data[Username].strip('b')
                    hashed = hashed.replace("'", "")
                    hashed = hashed.encode('utf-8')
                    
                    try:
                        if bcrypt.checkpw(Password.encode(), hashed):
                            system("cls")
                            print("\n""============ Selamat anda berhasil login ==============n")
                            print("                     Halo ", Username )
                        else:
                            print("Password yang anda masukkan salah")
                        
                    except:
                        print("password atau username anda salah")
                else:
                    print("User tidak ditemukan")
            except:
                print("Password atau username tidak")
        else:
            print("Kesalahan masuk ke sistem")
            
    else:
        print("Silahkan untuk login ulang")
        gainAccess()
        b = b.strip()

def register(Username=None, Password1=None, Password2=None):
    Username  = input("Tuliskan Username anda  : ")
    Password1 = input("Password                : ")
    Password2 = input("Konfirmasi Password     : ")
    db = open("datalogin.txt", "r")
    d = []
    for i in db:
        a,b = i.split(",")
        b = b.strip()
        c = a,b
        d.append(a)
    if not len(Password1)<=5:
        db = open("datalogin.txt", "r")
        if not Username ==None:
            if len(Username) <1:
                print("Username tidak boleh kurang dari 1 huruf")
                register()
            elif Username in d:
                print("Username ditemukan")
                register()		
            else:
                if Password1 == Password2:
                    Password1 = Password1.encode('utf-8')
                    Password2 = bcrypt.hashpw(Password1, bcrypt.gensalt())
                                       
                    db = open("datalogin.txt", "a")
                    db.write(Username+", "+str(Password1)+"\n")
                    print("User berhasil dibuat")
                else:
                    print("Password tidak sama")
                    register()
    else:
        print("Password tidak boleh kurang dari 5 elemen")



def home(option=None):
    while True:
        print("""
        +===================================================+
        |          Selamat Datang di Dream Laundry          |
        +===================================================+
        | 1 |               Layanan Laundry                 |
        | 2 |                 Buat akun                     |
        | 3 |                   Keluar                      |
        +===================================================+
        """)
        pilih = int(input("\nPilihan => "))
        if pilih == 1:
            system('cls')
            gainAccess()
            return True
        elif pilih == 2:
            system('cls')
            register()
            return True    
        elif pilih == 3:
            system('cls')
            print ("Terimakasih sudah menggunakan program ini")
            quit ()
        else:
            print("\nPilihan Tidak Tersedia")
            back = input("Apakah anda ingin kembali ? ya/tidak \n=>")
            if back == "ya":
                continue
            else:
                print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                quit()

def laundry():
    system("cls")
    if home():
        ulang = "ya"
        while(ulang == "ya"):
            print("\n")
            print("="*30)
            print("---     Rincian Laundry    ---")     
            print("="*30)
            print(" 1. Masukkan Data Laundry ")
            print(" 2. Tampil Data Laundry ")
            print(" 3. Edit Data Laundry ")
            print(" 4. Delete Data Laundry ")
            print(" 5. Sorting Data Laundry")
            print(" 6. Search Data Laundry")
            print(" 7. Menu Sebelumnya")
            print(" 8. Keluar")
            print("="*30)
            try:
                pilih = int(input("Masukan Pilihan Anda : "))
            except:
                print("Gunakan Angka Saat Menginputkan Pilihan\n")
                continue
            if pilih == 1:
                system("cls")   
                append()
                print("\n")
            elif pilih == 2:
                system("cls")   
                IDx = make_list(id_laundry)             
                Name = make_list(nama_laundry)
                Weight = make_list(berat_laundry)
                print_list(IDx,Name,Weight)
                print("\n")
            elif pilih == 3:
                system("cls")   
                update()
                print("\n")
            elif pilih == 4:
                system("cls")   
                delete()
                print("\n")
            elif pilih == 5:
                system("cls")   
                sort()
                print("\n")
            elif pilih == 6:
                system("cls")   
                search()
                print("\n")
            elif pilih == 7:
                home()
            elif pilih == 8:
                print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                quit()
            else:
                print("Pilihan Tidak Tersedia")
                ulang = input("Apakah Ingin Mengulang ? ya / tidak \n=>")
                if ulang == "ya":
                    continue
                else:
                    print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                    quit()

laundry()
