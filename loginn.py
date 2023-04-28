import pwinput
import json
admin = {"username": ["admin"],
        "password": ["admin",]}
file_json = open("user.json")
user = json.loads(file_json.read())

def setting_member():
    with open("user.json","w") as userbaru:
        json.dump(user,userbaru)
#LOGIN
def login_admin():
    while True:
        username = input("masukkan username : ")
        password = pwinput.pwinput("masukkan password : ")
        try:
            login = admin["username"].index(username)
            if username == admin["username"][login] and password == admin["password"][login]:
                
                break
            else:
                print("Invalid Password")
        except ValueError:
            print("Invalid Username")

def login_user():
    while True:
        try:
            username = input("username : ")
            password = pwinput.pwinput("password : ")
            login = user["username"].index(username)
            if username == user["username"][login] and password == user["password"][login]:
                break
            else:
                print("\npassword tidak terdaftar pada user, coba lagi\n")
        except ValueError:
            print("\nuser anda tidak terdaftar sebagai member, coba lagi\n") 

def tambah_user():
    while True:
        try:
            username = str(input("masukan username baru : ").replace("\t","").replace(" ",""))
            if username == "":
                print("=== data tidak boleh kosong ===")
                break
            elif username in user["username"]:
                print("username telah digunakan")
                break
            elif username not in user["username"]:

                password = str(pwinput.pwinput("masukan password anda : ").replace("\t","").replace(" ",""))
                if password == "":
                    print("=== data tidak boleh kosong ===")
                    break
                elif password in user["username"]:
                    print("password telah digunakan")
                    break

                else:
                    user["username"].append(username)
                    user["password"].append(password)
                    print("=== selamat datang",username," ===")
                    setting_member()
                    break
        except ValueError:
            print("\ninput data dengan benar\n")