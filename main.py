id_kumulatif = 1

data_user = [
    {
        "id": 0,
        "username": "1",
        "password": "1",
        "buku": []
    },
    {
        "id": 1,
        "username": "2",
        "password": "2",
        "buku": []
    }
]

data_buku = [
    {
        "id": 0,
        "judul": "Malin Kundang",
        "tersedia": True
    },
    {
        "id": 1,
        "judul": "Sangkuriang",
        "tersedia": True
    },
    {
        "id": 2,
        "judul": "Timun Mas",
        "tersedia": True
    },
    {
        "id": 3,
        "judul": "Roro Jonggrang",
        "tersedia": True
    },
    {
        "id": 4,
        "judul": "Dilan",
        "tersedia": True
    },
    {
        "id": 5,
        "judul": "Laskar Pelangi",
        "tersedia": True
    },
    {
        "id": 6,
        "judul": "Harry Potter",
        "tersedia": True
    },
    {
        "id": 7,
        "judul": "Bumi Manusia",
        "tersedia": True
    },
    {
        "id": 8,
        "judul": "Python Dasar",
        "tersedia": True
    },
    {
        "id": 9,
        "judul": "Matematika",
        "tersedia": True
    }
]

def main_menu():
    print("\n=-=-=-=-=-= SELAMAT DATANG DI PERPUSTAKAAN =-=-=-=-=-=")
    print("1. Register")
    print("2. Login")
    print("3. Keluar Dari Program")

def register():
    print("\n=-=-=-=-=-= REGISTRASI AKUN =-=-=-=-=-=")
    
    while True:
        sudah_dipakai = False
        username = input("Masukkan Username: ")
        
        for user in data_user:
            if username == user["username"]:
                sudah_dipakai = True
            
        if sudah_dipakai == True:
            print("Username sudah terdaftar, silahkan masukkan username lain\n")
        elif username == '':
            print("Username tidak boleh kosong\n")
        elif " " in username:
            print("Username tidak boleh mengandung spasi\n")
        else:
            break
    
    while True:
        password = input("Masukkan Password (minimal 8 karakter): ")
        
        if len(password) < 8:
            print("Password tidak boleh kurang dari 8 karakter\n")
        elif " " in password:
            print("Password tidak boleh mengandung spasi\n")
        else: 
            break
    
    global id_kumulatif
    id_kumulatif += 1
    data_user.append(
        {
            "id": id_kumulatif,
            "username": username,
            "password": password,
            "buku": []   
        }
    )
    
def login():
    print("\n=-=-=-=-=-= LOGIN KE SISTEM =-=-=-=-=-=")
    
    id_login = None
    percobaan_login = 3
    akses = False
    login_berhasil = False
    while True: 
        if percobaan_login == 0:
            break
        
        username = input("Masukkan Username: ")
        password = input("Masukkan Password: ")
        
        for user in data_user:
            if username == user["username"] and password == user["password"]:
                print("Login berhasil")
                id_login = user["id"]
                login_berhasil = True
                break
                
        if login_berhasil == True:
            akses = True
            break
        else:
            print("Username dan Password salah, silahkan coba lagi")
            percobaan_login -= 1
        
    return akses, id_login
        
def home_menu(username):
    print(f"\n=-=-=-=-=-= SELAMAT DATANG {username.upper()} =-=-=-=-=-=")
    print("1. Lihat Katalog Buku")
    print("2. Pinjam Buku")
    print("3. Lihat Buku Yang Dipinjam")
    print("4. Kembalikan Buku")
    print("5. Logout")
    print("6. Keluar Dari Program")
    
def book_menu():
    print("\n=-=-=-=-=-= KATALOG BUKU =-=-=-=-=-=")
    
    for buku in data_buku:
        print(f"{(str(buku["id"] + 1) + ".").ljust(3)} {buku["judul"].ljust(28)} [{"T" if buku['tersedia'] else "X"}]")

    print("\nKeterangan")
    print("T = Tersedia")
    print("X = Dipinjam")
    
def borrow_book(user_id, param_buku):
    book_menu()
    selesai = False
    while not selesai:
        valid = False
        pilihan = input("\nMasukkan ID buku yang ingin dipinjam: ")
        for buku in data_buku:
            if pilihan == f"{buku["id"] + 1}":
                if buku["tersedia"]:
                    print("Buku berhasil dipinjam")
                    buku["tersedia"], selesai = False, True
                    param_buku.append(buku["id"])
                    valid = True
                    break
                else:
                    print("Buku tidak tersedia, pilih buku lainnya")
                    valid = True
        if not selesai and not valid:
            print("Buku tidak valid, silahkan coba lagi")
                
    data_user[user_id]["buku"] = param_buku
    
def book_owned(param_buku):
    print("\n=-=-=-=-=-= DAFTAR BUKU YANG DIPINJAM =-=-=-=-=-=")

    if (len(param_buku) > 0):
        i = 1
        for buku in data_buku:
            for list_buku in param_buku:
                if list_buku == buku["id"]:
                    judul_buku = buku["judul"]
                    print(f"{i}. {judul_buku}")
                    i += 1
    else:
        print("Tidak ada buku yang dipinjam")
        
def return_book(user_id, param_buku):
    book_owned(param_buku)
    if len(param_buku) > 0:
        selesai = False
        while not selesai:
            pilihan = int(input("\nMasukkan ID buku yang ingin dikembalikan: ")) - 1
            if 0 <= pilihan < len(param_buku):
                print("Buku berhasil dikembalikan")
                buku_kembali = param_buku[pilihan]
                selesai = True
                break
            else:
                print("Index tidak valid")
                
        for buku in data_buku:
            if buku["id"] == buku_kembali:
                buku["tersedia"] = True
                
        param_buku.pop(pilihan)        
        data_user[user_id]["buku"] = param_buku
            
def main():
    sudah_login = False
    id_login = None
    while True: 
        if sudah_login == False: # kalau user belum login
            main_menu()
            pilihan = input("Pilih menu (1-3): ")
            
            if pilihan == '1':
                register()
            elif pilihan == '2':
                akses, id_login = login()
                if akses == True:
                    sudah_login = True
                else:
                    print("Terlalu banyak percobaan gagal, coba lagi nanti")
                    break
            elif pilihan == '3':
                print("Sampai jumpa lagi")
                break
            else:
                print("Pilihan tidak valid silahkan ulangi")
                
        else: # kalau user udah login
            for user in data_user:
                if id_login == user["id"]:
                    user_id = user["id"]
                    username_login = user["username"]
                    buku = user["buku"]
                    
            home_menu(username_login)
            pilihan = input("Pilih menu (1-6): ")
            
            if pilihan == '1':
                book_menu()
            elif pilihan == '2':
                borrow_book(user_id, buku)
            elif pilihan == '3':
                book_owned(buku)
            elif pilihan == '4':
                return_book(user_id, buku)
            elif pilihan == '5':
                sudah_login = False
            elif pilihan == '6':
                print("Sampai jumpa lagi")
                break
            else:
                print("Pilihan tidak valid silahkan ulangi")
            
main()