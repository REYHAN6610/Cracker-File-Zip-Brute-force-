#Script By Reyhan6610
#Jangan di salah gunakan ya coy, Emangnya ada ya yang menyalah gunakan🙄🤔
#Oke Kalau mau rekode silah kan
#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*#+#×#*


import pyzipper

def print_green(message):
    print(f"\033[92m{message}\033[0m")  

def print_red(message):
    print(f"\033[91m{message}\033[0m")

def brute_force_zip(zip_file):
    password_file = 'sampek_bawah😎👇.txt'  
    try:
        with pyzipper.AESZipFile(zip_file) as zf:
            with open(password_file, 'r') as pf:
                found = False
                for password in pf:
                    password = password.strip()  
                    print(f'Mencoba password: {password}')  
                    try:
                        zf.extractall(pwd=password.encode('utf-8'))
                        print_green(f'Password ditemukan: {password}')
                        found = True
                        break  
                    except RuntimeError:
                        print_red(f'Password salah: {password}')  
                if not found:
                    print_red('Password tidak ditemukan.')
    except FileNotFoundError:
        print("File ZIP tidak ditemukan.")

zip_file = input("Masukan Dimana File (.zip)=> ")

brute_force_zip(zip_file)