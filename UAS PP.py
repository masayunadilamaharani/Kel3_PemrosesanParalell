array = ['192.168.42.17', '192.168.42.249', '192.168.42.110', '192.168.42.227']
nama_pengguna ='root'
katasandi = 'extreme5end911'
def pc_bayu():
    import paramiko
    import time
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=array[0],username=nama_pengguna ,password=katasandi)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    print("connected")
    print("_____________________________")
    print("------PROGRAM MENGHITUNG------")
    print(  "1.keliling segitiga dan luas \n"
                "2.keliling lingkaran dan luas \n"
                "3.keliling persegi dan luas \n ")
    x=input("pilih--:")
    if x=='1':
        s=str(input("masukkan nilai alas :"))
        s2=str(input("masukkan nilai tinggi :"))
        s3=str(input("masukkan nilai sisi :"))
        conn.send("python3 segitigak.py \n")
        conn.send(s+"\n")
        conn.send(s2+"\n")
        conn.send(s3+"\n")
        time.sleep(1)
        output =conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
            
    elif x=='2':
        j = float(input("masukkan jari :"))
        conn.send("python3 lingkar.py \n")
        conn.send(str(j)+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    elif x=='3' :
        x = str(input("masukan sisi :"))
        conn.send("python3 persegi.py \n")
        conn.send(x+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    else :
        print (" tidak ada dalam pilihan")
def pc_masayu():
    import paramiko
    import time
    print("connecting")
    print("_____________________________")
    print("------PROGRAM MENGHITUNG------")
    print(  "1.keliling segitiga dan luas \n"
                "2.keliling lingkaran dan luas \n"
                "3.keliling persegi dan luas \n ")
    x=input("pilih--:")
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=array[1],username=nama_pengguna ,password=katasandi)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    if x=='1':
        s=str(input("masukkan nilai alas :"))
        s2=str(input("masukkan nilai tinggi :"))
        s3=str(input("masukkan nilai sisi :"))
        conn.send("python3 segitigak.py \n")
        conn.send(s+"\n")
        conn.send(s2+"\n")
        conn.send(s3+"\n")
        time.sleep(1)
        output =conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
            
    elif x=='2':
        j = float(input("masukkan jari :"))
        conn.send("python3 lingkar.py \n")
        conn.send(str(j)+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    elif x=='3' :
        x = str(input("masukan sisi :"))
        conn.send("python3 persegi.py \n")
        conn.send(x+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    else :
        print (" tidak ada dalam pilihan")
def pc_alfiah():
    import paramiko
    import time
    print("connecting")
    print("_____________________________")
    print("------PROGRAM MENGHITUNG------")
    print(  "1.keliling segitiga dan luas \n"
                "2.keliling lingkaran dan luas \n"
                "3.keliling persegi dan luas \n ")
    x=input("pilih--:")
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=array[2],username=nama_pengguna ,password=katasandi)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    if x=='1':
        s=str(input("masukkan nilai alas :"))
        s2=str(input("masukkan nilai tinggi :"))
        s3=str(input("masukkan nilai sisi :"))
        conn.send("python3 segitigak.py \n")
        conn.send(s+"\n")
        conn.send(s2+"\n")
        conn.send(s3+"\n")
        time.sleep(1)
        output =conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
            
    elif x=='2':
        j = float(input("masukkan jari :"))
        conn.send("python3 lingkar.py \n")
        conn.send(str(j)+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    elif x=='3' :
        x = str(input("masukan sisi :"))
        conn.send("python3 persegi.py \n")
        conn.send(x+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    else :
        print (" tidak ada dalam pilihan")
def pc_saad():
    import paramiko
    import time
    ssh_client=paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=array[3],username=nama_pengguna ,password=katasandi)
    conn=ssh_client.get_transport().open_session()
    conn.invoke_shell()
    print("connected")
    print("_____________________________")
    print("------PROGRAM MENGHITUNG------")
    print(  "1.keliling segitiga dan luas \n"
                "2.keliling lingkaran dan luas \n"
                "3.keliling persegi dan luas \n ")
    x=input("pilih--:")
    if x=='1':
        s=str(input("masukkan nilai alas :"))
        s2=str(input("masukkan nilai tinggi :"))
        s3=str(input("masukkan nilai sisi :"))
        conn.send("python3 segitigak.py \n")
        conn.send(s+"\n")
        conn.send(s2+"\n")
        conn.send(s3+"\n")
        time.sleep(1)
        output =conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
            
    elif x=='2':
        j = float(input("masukkan jari :"))
        conn.send("python3 lingkar.py \n")
        conn.send(str(j)+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    elif x=='3' :
        x = str(input("masukan sisi :"))
        conn.send("python3 persegi.py \n")
        conn.send(x+"\n")
        time.sleep(1)
        output = conn.recv(65535)
        print(output.decode())
        print("Apa mau lanjut?")
        z=input("y/n :")
        if z=='y':
            menu()
        else:
            print()
    else :
        print (" tidak ada dalam pilihan")
        menu()
    
    


def menu():
    print("------------SELAMAT DATANG DI MASTERNODE-----------")
    print('\n')
    print("Node Yang Tersedia")
    print("-----------------------")
    print("1. pc_bayu")
    print("2. pc_masayu")
    print("3. pc_alfiah")
    print("4. pc_saad")
    print("-----------------------")
    x = input("Masukan Pilihan anda :").split(",")

    for pilih in x:
        if pilih =='1':
            pc_bayu()
        elif pilih=='2':
            pc_masayu()
        elif pilih=='3':
            pc_alfiah()
        elif pilih=='4':
            pc_saad()
        else :
            print ("\n")
            print ("Not Found ! periksa lagi pilihan anda..!")
            print ("________________________________________")
            print("Refresh ?")
            print("ya")
            print("no")
            choose =input('>>> : ')
            if choose=='ya':
                menu()
            else :
                print("Shutdown Program")
                print("Terima-Kasih")

            
menu()
