Algoritma Struktur Data
Kelompok 9

#Anggota:
1.	Dinnuhoni Trahutomo		      (2209116006)
2.	Imelda Putri 			          (2209116016)
3.	Najwa Caesa Putri R. S. P.	(2209116048)

#Deskripsi Program:
Program “Toko Laundry” ini dibuat dengan tujuan untuk memudahkan pemilik toko dalam mengelola bisnis. selain itu juga memudahkan karyawan/admin dalam melakukan pendataan barang-barang laundry pelanggan.

#Library:
1.	from os import system yaitu modul yang menyediakan cara portable untuk menggunakan fungsionalitas yang bergantung pada system operasi.
2.	from prettytable import PrettyTable yaitu library dalam Python yang berguna dalam membuat data dalam bentuk table agar tampilan lebih rapi.
3.	import mysql.connector modul ini untuk berkomunikasi dengan database MySQL.
4.	from loginn import * digunakan agar saat menginput sandi, tampilan sandi berbentuk (*****).

#Linked list:
1.	class Node
2.	class linkedlist

a.	Fungsi dalam linkedlist
-	Aktifasidb
-	Add
-	Remove_task
-	Update
-	Sort_tasks
-	Jump_search
-	Showll
-	Mergesort
-	SortLaun
-	Sort
-	Bayar
-	Menupembeli
-	Home
-	Laundry

#Fitur:
1.	Pembeli:
-	Aktifkan database 
-	Tampil Data Laundry 
-	Search Data Laundry
-	Pembayaran
-	Kembali
-	Quit

2.	Admin:
-	Aktifkan database
-	Masukkan Data Laundry
-	Tampil Data Laundry
-	Edit Data Laundry
-	Delete Data Laundry
-	Sorting Data Laundry
-	Search Data Laundry
-	Menu Sebelumnya
-	Keluar

#Fungsionalitas:
1.	Pembeli dapat melakukan registrasi agar memiliki akun untuk dapat mengakses program.
2.	Pembeli mengakses program menggunakan akun yang telah dibuat pada saat login program.
3.	Pembeli dapat mengktifkan database untuk menampilkan data laundry, search data laundry, dan melakukan pembayaran.
4.	Akun admin dibuat untuk dipakai bersama sesama admin dapat digunakan untuk mengakses program pada bagian admin.
5.	Admin dapat mengaktifkan database, memasukkan data laundry, menampilkan data laundry, mengedit data laundry, delete data laundry, sorting data laundry, search data laundry.

#Cara penggunaan:
1.	Menu awal
Pada menu awal, terdapat 4 pilihan yaitu Admin, Layanan Laundry, Buat Akun, Keluar.
![image](https://user-images.githubusercontent.com/122195566/235309828-71bf3965-6a08-4b32-baac-0b3fafe59c9e.png)

#1.	Admin
Pada menu awal, jika user admin memilih opsi pertama yaitu “Admin”, maka user akan diminta untuk langsung memasukkan username serta password dari admin pada bagian login admin.
![image](https://user-images.githubusercontent.com/122195566/235309834-fd92d441-5691-4076-8f60-10ee61542001.png)
 
Apabila user admin memasukkan username serta password yang benar maka, akan tampil opsi-opsi untuk admin
![image](https://user-images.githubusercontent.com/122195566/235309844-19ae135d-7fa4-467f-a917-ca55d5cd58a9.png)

Apabila user admin memasukkan username serta password yang salah maka, akan tampil “Invalid Password”, kemudian user admin akan diminta untuk memasukkan username serta password hingga benar.
![image](https://user-images.githubusercontent.com/122195566/235309867-330fed44-bd79-40e1-bf02-8bcc4e073d0f.png)
 
Jika user admin berhasil login, maka tampilan untuk admin sebagai berikut.
![image](https://user-images.githubusercontent.com/122195566/235309888-be5d3695-5a4e-493b-bf3c-2a4591256573.png)
 
Opsi-opsi pada admin:
0.	Aktifkan database:
Mengaktfikan database dengan cara mengetik 0 setiap kali ingin mengetik opsi-opsi yang lain.
![image](https://user-images.githubusercontent.com/122195566/235309896-23273dac-491b-49b9-b1d1-1f628af1c083.png)

1. Masukkan Data Laundry:
Memasukkan data laundry ada beberapa hal yang harus diisi oleh user admin diantaranya kode, jenis laundry (One Day Service/Dry Cleaning/Layanan Antar Jemput), nama pelanggan, berat laundry (Kg), serta menginput kembali total harga yang tertera seperti pada gambar.
![image](https://user-images.githubusercontent.com/122195566/235310688-95af4551-5ba8-49bf-a3d1-3cdd1c43a5cd.png)

2. Tampil Data Laundry:
Tampil data laundry akan menampilkann kode, id, nama, berat serta harga dari bagian admin.
![image](https://user-images.githubusercontent.com/122195566/235312528-9a64907a-7464-4913-b301-d58698493afd.png)

3. Edit Data Laundry:
Mengedit data laundry ada beberapa hal yang harus diisi oleh user admin diantaranya kode, jenis laundry (One Day Service/Dry Cleaning/Layanan Antar Jemput), nama pelanggan, berat laundry (Kg), serta menginput kembali total harga yang tertera seperti pada gambar.
![image](https://user-images.githubusercontent.com/122195566/235311183-00c95361-0755-484e-bb69-c859ed01e655.png)

4. Delete Data Laundry:
Apabila user admin ingin menghapus data laundry, maka user admin hanya mengetik kode pelanggan yang ingin dihapus seperti gambar.
![image](https://user-images.githubusercontent.com/122195566/235311304-73e3796a-f2f0-45f5-a823-07dadf22d8c6.png)
Jika kode yang ingin dihapus sesuai dengan data yang ada maka akan tampil sebagai berikut
![image](https://user-images.githubusercontent.com/122195566/235311466-be386ae0-3c36-4aa8-87b5-6ce0f1d5548f.png)

5. Sorting Data Laundry
Dalam sorting Data Laundry terdapat 4 pilihan
![image](https://user-images.githubusercontent.com/122195566/235311513-f3cd69fd-ba3b-491e-ac43-78be98f9a28e.png)

a. Sorting data ID pelanggan
![image](https://user-images.githubusercontent.com/122195566/235311543-223d59ab-1634-45ef-a51c-8b9d213af4f0.png)

b. Sorting data laundry
![image](https://user-images.githubusercontent.com/122195566/235311586-17725a96-c56d-409e-9561-114e9ac978d0.png)

c. Sorting data berat laundry
![image](https://user-images.githubusercontent.com/122195566/235311605-b87e38e6-16e9-4bfc-b700-70baf3c1c285.png)

d. Menu sebelumnya
![image](https://user-images.githubusercontent.com/122195566/235311618-f174f366-683f-4d45-9082-44897529cb43.png)

6. Search Data Laundry
Search data laundry dapat dilakukan dengan mengetik kode pelanggan yang ingin dicari
![image](https://user-images.githubusercontent.com/122195566/235311694-29a3b0da-47fe-4e82-ac56-fe6fd81544cf.png)

7. Menu Sebelumnya
![image](https://user-images.githubusercontent.com/122195566/235311618-f174f366-683f-4d45-9082-44897529cb43.png)

8. Keluar
Opsi "Keluar" akan mengeluarkan user admin dari program
![image](https://user-images.githubusercontent.com/122195566/235311756-1600282f-5850-41bb-b602-59f59d9d4d9b.png)

#2. Layanan Laundry
Layanan laundry adalah opsi untuk user pelanggan pada program laundry
![image](https://user-images.githubusercontent.com/122195566/235311811-c908474b-9e66-4530-98a3-01ded351401c.png)

Apabila user pelanggan mengetik angka 2, maka akan diarahkan pada login pelanggan. Pada login pelanggan, user pelanggan diminta untuk memasukkan username serta password yang telah didaftarkan dan tersedia di json tepatnya "user.json".
![image](https://user-images.githubusercontent.com/122195566/235312383-25577d97-447f-484f-a921-bd7f9bc5f68c.png)
Pada gambar, user pelanggan yang digunakan adalah "dinnu" dengan password "2323".
![image](https://user-images.githubusercontent.com/122195566/235312058-ed387baf-3b86-464f-9375-c7059f1ecd42.png)

0.	Aktifkan database:
Mengaktfikan database dengan cara mengetik 0 setiap kali ingin mengetik opsi-opsi yang lain.
![image](https://user-images.githubusercontent.com/122195566/235309896-23273dac-491b-49b9-b1d1-1f628af1c083.png)

1. Tampil Data Laundry:
Tampil data laundry akan menampilkann kode, id, nama, berat serta harga dari bagian pelanggan.
![image](https://user-images.githubusercontent.com/122195566/235312528-9a64907a-7464-4913-b301-d58698493afd.png)

2. Search data laundry:
Pelanggan dapat mencari data laundry sendiri yang berupa kode, id, nama, berat, serta harga dengan mengetik kode pelanggan, maka akan tampil sebagai berikut.
![image](https://user-images.githubusercontent.com/122195566/235312666-889568e3-856e-42b7-bd35-5961a914e789.png)

3. Pembayaran:
Pelanggan dapat membayar laundry mereka dengan memasukkan kode terlebih dahulu, kemudian akan tampil jumlah yang harus dibayar, lalu pelanggan membayar total laundry.
![image](https://user-images.githubusercontent.com/122195566/235312865-56698a1f-e62b-49ca-af6b-a2938a079935.png)
Apabila pembayaran telah dilakukan, maka akan tampil di txt tepatnya "struk.txt".
![image](https://user-images.githubusercontent.com/122195566/235312933-f72383df-634e-4562-943b-0783810909ce.png)

4. Kembali
![image](https://user-images.githubusercontent.com/122195566/235311618-f174f366-683f-4d45-9082-44897529cb43.png)

5. Keluar
Opsi "Keluar" akan mengeluarkan user pelanggan dari program
![image](https://user-images.githubusercontent.com/122195566/235311756-1600282f-5850-41bb-b602-59f59d9d4d9b.png)

#3. Buat Akun
Opsi "Buat Akun" adalah tahap dimana pelanggan ingin membuat akun agar dapat menggunakan program.
![image](https://user-images.githubusercontent.com/122195566/235313009-7961c666-6f49-48c0-925f-916d6455c5bb.png)

User akan diarahkan untuk mengetik username serta password untuk membuat akun. Pada hal ini username dibawah "tom" dengan password "3232".
![image](https://user-images.githubusercontent.com/122195566/235313212-0ca06567-e804-49cf-8e19-5a6396ecab2d.png)

Apabila berhasil maka akan tampil di json tepatnya "user.json". Berikut adalah gambar sebelum dan sesudah memasukkan user pelanggan baru.
![image](https://user-images.githubusercontent.com/122195566/235313285-3da77b1e-6b53-4199-8969-efbd70df18ab.png)
![image](https://user-images.githubusercontent.com/122195566/235313336-d65c8f21-0f05-4336-9dbb-874394d79958.png)

#4. Keluar
Opsi "Keluar" akan mengeluarkan user dari program.
![image](https://user-images.githubusercontent.com/122195566/235311756-1600282f-5850-41bb-b602-59f59d9d4d9b.png)












