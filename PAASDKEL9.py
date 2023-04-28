import bcrypt
from os import system
from platform import system as getsys
import time
import collections
from datetime import datetime
from prettytable import PrettyTable
from bisect import bisect_left

def time():
    jam = datetime.now()
    waktu = int(jam.strftime("%H"))
    system("cls")
    print("="*52)
    print(jam.strftime("[ Tanggal = %d/%b/%Y]))      [ Waktu = %H:%M:%S ]"))
    print("="*52,"\n")

def cls():
    if getsys() == "WINDOWS": system("cls")
    else:
        system("clear")

# Database
id_laundry = [23,12,48]
nama_laundry = ["imel","dinnu",'cesa']
berat_laundry = [10,15,8]

# Linked List
class Node(object):
    def __init__(self,initvalue, next = None):
        self.value=initvalue
        self.next=None
        self.previous=None
    def getvalue(self):
        return self.value
    def getNext(self):
        return self.next
    def getPrevious(self):
        return self.previous
    def setvalue(self,newvalue):
        self.value=newvalue
    def setNext(self,newNext):
        self.next=newNext
    def setPrev(self,newPrevious):
        self.previous=newPrevious
    def r_next(self):
        return self.next

class linkedlist:
    def __init__(self, data,next = None):
        self.head = data
        self.next = next
    
    def sizeof (self,count=0):
        x = self.head
        while x:
            count += 1
            x = x.next
        return count
    
    def delete(self,data):
        temp = self.head
        if (temp is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return
            while (temp is not None):
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next
            if (temp == None):
                return 
            prev.next = temp.next
            temp = None
    
def make_list (elements):
    head = linkedlist(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = linkedlist(element)
    return head 

def print_list(head,head1,head2):
    ptr = head
    ptr1 = head1
    ptr2 = head2
    i=0
    table = PrettyTable(["No.","ID","Nama","Laundry/Kg"])
    while ptr:
        table.add_row([i+1,ptr.head,ptr1.head,ptr2.head])
        ptr = ptr.next
        ptr1 = ptr1.next
        ptr2 = ptr2.next
        i+=1
    print(table)

class Solution:
  def solve(self, node):
    values = []
    head = node
    while node:
        values.append(node.data)
        node = node.next
    mergeSort(values)
    values = collections.deque(values)
    node = head
    while node:
        node.val = values.popleft()
        node = node.next
    return head

#======Function======
def append():
    IDx = make_list(id_laundry)             
    Name = make_list(nama_laundry)
    Weight = make_list(berat_laundry)
    print_list(IDx,Name,Weight)
    print("="*40)
    print("---       Masukkan Data Laundry      ---")     
    print("="*40)
    ID = int(input("Masukkan ID Pelanggan         : "))
    id_laundry.append(ID)
    Nama = input("Masukkan Nama Pelanggan       : ")
    nama_laundry.append(Nama)
    Kg = int(input("Masukkan Laundry/Kg Pelanggan : "))
    berat_laundry.append(Kg)
    IDx = make_list(id_laundry)
    Name = make_list(nama_laundry)
    Weight = make_list(berat_laundry)
    print_list(IDx,Name,Weight)
    print("="*30)
    print ("Data Pelanggan Berhasil Dibuat ")
    print("="*30)
    return

def update():
    IDx = make_list(id_laundry)             
    Name = make_list(nama_laundry)
    Weight = make_list(berat_laundry)
    print_list(IDx,Name,Weight)
    while True:
        print("="*34)
        print("---      Edit Data Laundry     ---")     
        print("="*34)
        try:
            ID = int(input("Input Nomor Pelanggan Ingin Diubah : "))
        except:
            print("Gunakan Angka Saat Menginput Pilihan")
            continue
        if ID <= 0 :
            print("Pilihan Tidak Tersedia")
            continue
        idx = ID - 1
        if (idx > len(id_laundry) - 1):
            print ("No Tidak Tersedia")
            continue
        else:
            try:
                tambah = input("Masukkan Laundry/Kg Pelanggan Yang Baru :  ")
            except:
                print("Gunakan Angka Saat Menginput Pilihan")
                continue
            hasil = tambah 
            berat_laundry [idx] = hasil
            return

def delete():
    while True:
        print("="*34)
        print("---      Hapus Data Laundry    ---")     
        print("="*34)
        IDx = make_list(id_laundry)
        Name = make_list(nama_laundry)
        Weight = make_list(berat_laundry)
        print_list(IDx,Name,Weight)
        try:
            ID = int(input("Input Nomor Pelanggan Ingin Dihapus : ")) 
        except:
            print("Gunakan Angka Saat Menginput Pilihan")
            continue
        ID = ID - 1
        hapus = ID 
        if ID == (hapus):
            print("Anda Telah Menghapus ID",str(id_laundry.pop(ID)),"dari Data Laundry")
            IDx = make_list(id_laundry)
            Name = make_list(nama_laundry)
            Weight = make_list(berat_laundry)
            print_list(IDx,Name,Weight)
            return
        else:
            print("Pilihan Tidak Tersedia")

# Merge Sorting
def mergeSort(array):
    if len(array) > 1:
        center = round(len(array)/2)
        sublist_kiri = array[:center]
        sublist_kanan = array[center:]
        mergeSort(sublist_kiri)
        mergeSort(sublist_kanan)
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
    tampung = []
    table = PrettyTable()
    table.field_names =["pelanggan 1","pelanggan 2","pelanggan 3"]
    table.clear_rows()
    for i in range(len(array)):
        tampung.append(array[i])
    table.add_row(tampung)
    print(table)

def sort():
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
            array = id_laundry
            mergeSort(array)
            print("Data ID Pelanggan Terurut : ")
            SortLaun(array)
            print("\n")
            continue
        elif pilih == 2:  
            system("cls") 
            array = nama_laundry
            mergeSort(array)
            print("Data Nama Pelanggan Terurut : ")
            SortLaun(array)
            print("\n")
            continue
        elif pilih == 3:
            system("cls") 
            array = berat_laundry
            mergeSort(array)
            print("Data Laundry/Kg Pelanggan Terurut : ")
            SortLaun(array)
            print("\n")
            continue
        elif pilih == 4:
            laundry()
        else:
            print("Pilihan Tidak Tersedia")
            ulang1 = input("Apakah Ingin Mengulang? (y/n) :")
            if ulang1 == "y":
                continue
            else:
                print("\nTerimakasih Sudah Menggunakan Program Layanan Dream Laundry")
                quit()

# Search menggunakan Fibonnaci 
def f_search(arr, x, n):
    if x == arr[0]:
        return 0;
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
 
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
 
    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)
        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
 
    if(fibMMm1 and arr[n-1] == x):
        return n-1
        
    return -1

def search():
    n = len(id_laundry)
    x = int(input("Masukkan ID Laundry yang Ingin Dicari : "))
    ind = f_search(id_laundry, x, n)
    if ind >=0:
        print ("Ditemukan di Indeks Ke-", ind)
    else:
        print ("ID Laundry yang Anda Cari Tidak Ada")


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
