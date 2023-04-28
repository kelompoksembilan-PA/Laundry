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


    #PEMBAYARAN
    def bayar(self):
        try:
            sqll = "SELECT id,nama, harga FROM datapemesanan WHERE kode = %s "
            kode = input("masukan kode pesanan anda : ")
            cash = int(input("masukan jumlah uang anda  : "))
            val = (kode,)
            cursor.execute(sqll, val)
            dt = cursor.fetchall()
            if len(dt)>0:
                for i in dt:
                    harga = i[2]
                    if cash - harga >= 0:
                        kembali = cash - harga
                        with open("struk.txt","a") as f:
                            system('cls')
                            print("\n\n=================================================",file=f)
                            print("=============== S T R U K  B A Y A R ============",file=f)
                            print("================= DREAM LAUNDRY =================",file=f)
                            print("=================================================",file=f)
                            print("nama pembeli      : ",i[1],file=f)
                            print("metode pembayaran :  cash ",file=f)
                            print("pesanan           : ",i[0],file=f)
                            print("uang pembeli      : ",cash,file=f)
                            print("dibayar           : ",i[2],file=f)
                            print("kembalian         : ",kembali,file=f)
                            print("=================================================",file=f)
                            print("=================================================",file=f) 
                    else:
                        print("maaf uang anda kurang")
            else:
                print("kode invalid")  
        except ValueError:
            print("menu invalid")

    #Menu
    def menupembeli(self):
        system("cls")
        ulang = "ya"
        while(ulang == "ya"):
                print("\n")
                print("="*30)
                print("---     Rincian Laundry    ---")     
                print("="*30)
                print(" 0. aktifkan database ")
                print(" 1. Tampil Data Laundry ")
                print(" 2. Search Data Laundry")
                print(" 3. Pembayaran")
                print(" 4. Kembali")
                print(" 5. Quit")

                print("="*30)
                try:
                    pilih = int(input("Masukan Pilihan Anda : "))
                except:
                    print("Gunakan Angka Saat Menginputkan Pilihan\n")
                    continue
                if pilih == 0:
                    if mulai.aktif == False:
                        mulai.aktifasidb()
                        system("cls")
                        print("database telah aktif")
                    else:
                        print("database sudah aktif")
                elif pilih == 1:
                    system("cls")   
                    mulai.showll()
                    print("\n")
                elif pilih == 2:
                    system("cls")   
                    if mulai.aktif == False:
                        print("harap aktifkan database terlebih dahulu")
                    elif mulai.aktif == True:
                        kode = mulai.jump_search()
                        if kode is not None:
                            table = PrettyTable(['kode', 'id', 'nama','berat','harga'])
                            table.add_row([kode.kode, kode.id, kode.nama,kode.berat,kode.harga])
                            print(table)
                        else:
                            print("kode laundry tidak ditemukan.")
                    print("\n")
                elif pilih == 3:
                    if mulai.aktif == False:
                        system("cls")
                        print("harap aktifkan database terlebih dahulu")
                    else:
                        system("cls")
                        mulai.showll()
                        mulai.bayar()
                elif pilih == 4:
                    system("cls")
                    break
                elif pilih == 5:
                    print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                    quit()
                else:
                    print("Pilihan Tidak Tersedia")
                    ulang = input("Apakah Ingin Mengulang ? ya / tidak \n=>")
                    if ulang == "ya":
                        mulai.menupembeli()
                        continue
                    else:
                        print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                        quit()

    def home(self):
        while True:
            print("""
            +===================================================+
            |          Selamat Datang di Dream Laundry          |
            +===================================================+
            | 1 |                    Admin                      |
            | 2 |               Layanan Laundry                 |
            | 3 |                  Buat Akun                    |
            | 4 |                   Keluar                      |
            +===================================================+
            """)
            try:
                pilih = int(input("Masukan Pilihan Anda : "))
            except:
                print("Gunakan Angka Saat Menginputkan Pilihan\n")
                continue

            if pilih == 1:
                system('cls')
                login_admin()
                mulai.laundry()
                return True
            elif pilih == 2:
                system('cls')
                login_user()
                mulai.menupembeli()   
            elif pilih == 3:
                system('cls')
                tambah_user()
                mulai.home ()
                return True    
            elif pilih == 4:
                system('cls')
                print ("Terimakasih sudah menggunakan program ini")
                quit ()
            else:
                print("\nPilihan Tidak Tersedia")
                back = input("Apakah anda ingin kembali ? ya/tidak \n=>")
                if back == "ya":
                    mulai.home ()
                    continue
                else:
                    print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                    quit()

    def laundry(self):
        system("cls")
        ulang = "ya"
        while(ulang == "ya"):
                print("\n")
                print("="*30)
                print("---     Rincian Laundry    ---")     
                print("="*30)
                print(" 0. aktifkan database ")
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
                if pilih == 0:
                    if mulai.aktif == False:
                        mulai.aktifasidb()
                        system("cls")
                        print("database telah aktif")
                    else:
                        print("database sudah aktif")
                elif pilih == 1:
                    system("cls") 
                    mulai.add()
                elif pilih == 2:
                    system("cls")   
                    mulai.showll()
                elif pilih == 3:
                    system("cls") 
                    mulai.update()
                elif pilih == 4:
                    system("cls")
                    mulai.remove_task()
                elif pilih == 5:
                    system("cls")   
                    mulai.sort()
                    print("\n")
                elif pilih == 6:
                    system("cls")   
                    if mulai.aktif == False:
                        print("harap aktifkan database terlebih dahulu")
                    elif mulai.aktif == True:
                        kode = mulai.jump_search()
                        if kode is not None:
                            table = PrettyTable(['kode', 'id', 'nama','berat','harga'])
                            table.add_row([kode.kode, kode.id, kode.nama,kode.berat,kode.harga])
                            print(table)
                        else:
                            print("kode laundry tidak ditemukan.")
                elif pilih == 7:
                    mulai.home()
                elif pilih == 8:
                    print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                    quit()
                else:
                    system('cls')
                    print("Pilihan Tidak Tersedia")
                    ulang = input("Apakah Ingin Mengulang ? ya / tidak \n=> ")
                    if ulang == "ya":
                        system('cls')
                        continue
                    else:
                        print("\nTerimakasih Sudah Menggunakan Program Layanan Laundry DIC")
                        quit()
 
mulai = linkedlist()
mulai.home()
