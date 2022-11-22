listsayuran = [
    {
        'kode': 1,
        'nama': 'Bayam',
        'stock': 15,
        'harga': 5000,
        'expired': '01-12-22'
    },
    {
        'kode': 2,
        'nama': 'Daun Pepaya',
        'stock': 20,
        'harga': 6000,
        'expired': '28-11-22'
    },
    {
        'kode': 3,
        'nama': 'Brokoli',
        'stock': 30,
        'harga': 10000,
        'expired': '30-11-22'
    }
]

def semuaproduk(): #function ini berfungsi untuk menampilkan semua produk yang sudah tersimpan dalam program.
    print('Kode\t| Nama  \t| Stock\t| Harga\t| Expired')
    for i in range(len(listsayuran)) :
        print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listsayuran[i]['kode'],listsayuran[i]['nama'],listsayuran[i]['stock'],listsayuran[i]['harga'],listsayuran[i]['expired']))

def menampilkanmenuproduk() : #function untuk menu READ DATA
    inputmenu1=input('''
MENU DAFTAR PRODUK
1. LIHAT SEMUA DAFTAR PRODUK SAYURAN
2. LIHAT SALAH SATU PRODUK SAYURAN
3. EXIT MENU 

Masukkan angka menu yang Anda inginkan: ''')

    if(inputmenu1=='1'):
        if(len(listsayuran)!=0): #conditional statement untuk menilai apakah terdapat data sayuran yang sudah tersimpan dalam program.
            semuaproduk()
            menampilkanmenuproduk()
        else:
            print("\nTidak ada data")
            menampilkanmenuproduk()

    elif(inputmenu1=='2'):
        if(len(listsayuran)!=0):
            semuaproduk()
            inputprimarykey=int(input('\nDari seluruh produk di atas, masukkan salah satu kode produk yang ingin anda tampilkan: '))
            daftarkodesayuran=[] #list daftarkodesayuran ini dibuat untuk menampung value dari key kode sayuran saja, sehingga bisa dimanfaatkan untuk mencari keberadaan data berdasarkan kodenya.
            for x in range(len(listsayuran)):
                getkode=[listsayuran[x].get('kode')]
                daftarkodesayuran.extend(getkode)
            if(inputprimarykey in daftarkodesayuran): #conditional statement untuk menilai apakah user input yang dicari ada dalam data yang sudah tersimpan dalam program.
                y=daftarkodesayuran.index(inputprimarykey)  #variabel ini diperlukan untuk mencari tahu indeks dari input yang dimasukkan user. 
                print('\n{}\t| {}  \t| {}\t| {}\t| {}'.format(listsayuran[y]['kode'],listsayuran[y]['nama'],listsayuran[y]['stock'],listsayuran[y]['harga'],listsayuran[y]['expired']))
                menampilkanmenuproduk()
            else:
                print("\nTidak ada data")
                menampilkanmenuproduk()        
        else:
            print("\nTidak ada data")
            menampilkanmenuproduk()
   
    elif(inputmenu1=='3'):
        pass
   
    else:
        print("\nMohon masukkan input dengan angka antara 1-3 saja.") 
        menampilkanmenuproduk()

def menambahkanproduk() : #function untuk menu CREATE DATA
    inputmenu2=input('''
MENAMBAHKAN PRODUK
1. MENAMBAHKAN JENIS SAYURAN
2. EXIT MENU 

Masukkan angka menu yang Anda inginkan:  ''')

    if(inputmenu2=='1'):
        inputprimarykey=input('\nMasukkan nama jenis sayuran yang ingin anda tambahkan: ')
        namasayuran=inputprimarykey.title() #ini diperlukan agar inputan berupa strings bisa disamakan dengan data yang sudah ada dalam program, yaitu dengan huruf kapital di depan. Selain itu untuk memudahkan juga dalam melakukan fungsi komparasi.
        daftarnamasayuran=[] #list daftarnamasayuran ini dibuat untuk menampung value dari key nama sayuran saja, sehingga bisa dimanfaatkan untuk mencari keberadaan data berdasarkan namanya.
        for x in range(len(listsayuran)):
            getnamasayuran=[listsayuran[x].get('nama')]
            daftarnamasayuran.extend(getnamasayuran)
        if(namasayuran in daftarnamasayuran):  #conditional statement untuk menilai apakah user input berupa nama sayuran sudah ada dalam program.
            print("\nMaaf, sayuran jenis {} sudah ada dalam daftar produk.".format(namasayuran))
            menambahkanproduk()
        else:
            print('\nNama Jenis Sayuran: {}'.format(namasayuran))
            while(True): #while loop ini digunakan utk memastikan bahwa kode sayuran yang diinput tidak duplikat dengan kode yang sudah ada dalam daftar.
                kodesayuran = int(input('Masukkan Kode Sayuran: '))
                daftarkodesayuran=[] 
                for x in range(len(listsayuran)):
                    getkode=[listsayuran[x].get('kode')]
                    daftarkodesayuran.extend(getkode)
                if(kodesayuran in daftarkodesayuran):
                    print('Kode tersebut sudah dipakai oleh produk lain, silakan masukkan nomor kode yang berbeda.')
                else:
                    break
            stocksayuran = int(input('Masukkan Stock Sayuran: '))
            hargasayuran = int(input('Masukkan Harga Sayuran: '))
            expiredsayuran = (input('Masukkan Tanggal Expired Sayuran (DD-MM-YY): '))  
            yakinsimpan=input("\nApakah Anda yakin ingin menambahkan data tersebut? Ketik 1 jika ingin dilanjutkan dan 0 jika ingin dibatalkan: ")
            if(yakinsimpan=='1'):
                listsayuran.append({
                    'kode': kodesayuran,
                    'nama': namasayuran,
                    'stock': stocksayuran,
                    'harga': hargasayuran,
                    'expired': expiredsayuran
                })
                print("\nSelamat, data di bawah ini sudah berhasil ditambahkan!\n")    
                print('Kode\t| Nama  \t| Stock\t| Harga\t| Expired')
                print('{}\t| {}  \t| {}\t| {}\t| {}'.format(kodesayuran,namasayuran,stocksayuran,hargasayuran,expiredsayuran))
                menambahkanproduk()
            elif(yakinsimpan=='0'):
                menambahkanproduk()  
            else:
                print("\nInput yang Anda masukkan tidak sesuai, silakan ulangi!")  
                menambahkanproduk()

    elif(inputmenu2=='2'):
        pass
    
    else:
        print("\nMohon masukkan input dengan angka antara 1-2 saja.")
        menambahkanproduk()

def mengubahproduk() : #function untuk menu UPDATE DATA
    inputmenu3=input('''
MENGUBAH PRODUK
1. MENGUBAH ISI DATA SAYURAN
2. EXIT MENU 

Masukkan angka menu yang Anda inginkan:  ''')

    if(inputmenu3=='1'):
        inputprimarykey=(input('\nMasukkan nama jenis sayuran yang ingin anda update: '))
        namasayuran=inputprimarykey.title()  #ini diperlukan agar inputan berupa strings bisa disamakan dengan data yang sudah ada dalam program, yaitu dengan huruf kapital di depan. Selain itu untuk memudahkan juga dalam melakukan fungsi komparasi.
        daftarnamasayuran=[] #list daftarnamasayuran ini dibuat untuk menampung value dari key nama sayuran saja, sehingga bisa dimanfaatkan untuk mencari keberadaan data berdasarkan namanya.
        for x in range(len(listsayuran)):
            getnamasayuran=[listsayuran[x].get('nama')]
            daftarnamasayuran.extend(getnamasayuran)
        if(namasayuran in daftarnamasayuran): 
            z=daftarnamasayuran.index(namasayuran) #variabel ini diperlukan untuk mencari tahu indeks dari input yang dimasukkan user.   
            print('\nKode\t| Nama  \t| Stock\t| Harga\t| Expired')
            print('{}\t| {}  \t| {}\t| {}\t| {}'.format(listsayuran[z]['kode'],listsayuran[z]['nama'],listsayuran[z]['stock'],listsayuran[z]['harga'],listsayuran[z]['expired']))
            mauupdate=input("\nApakah Anda ingin mengubah data di atas? Ketik 1 jika ingin dilanjutkan dan 0 jika ingin dibatalkan: ")
            if(mauupdate=='1'):
                print('\nSilakan masukkan data {} yang terbaru.\n'.format(namasayuran))
                namasayuran = input('Masukkan Nama Sayuran Terbaru: ')
                namasayuran = namasayuran.title()
                while(True): #while loop ini digunakan utk memastikan bahwa kode sayuran yang diinput tidak duplikat dengan kode yang sudah ada dalam daftar.
                    kodesayuran = int(input('Masukkan Kode Sayuran Terbaru: '))
                    daftarkodesayuran=[] 
                    for x in range(len(listsayuran)):
                        getkode=[listsayuran[x].get('kode')]
                        daftarkodesayuran.extend(getkode)
                    if(kodesayuran in daftarkodesayuran):
                        print('Kode tersebut sudah dipakai oleh produk lain, silakan masukkan nomor kode yang berbeda.')
                    else:
                        break
                stocksayuran = int(input('Masukkan Stock Sayuran Terbaru: '))
                hargasayuran = int(input('Masukkan Harga Sayuran Terbaru: ')) 
                expiredsayuran = input('Masukkan Tanggal Expired Sayuran (DD-MM-YY): ')
                yakinupdate=input("\nApakah Anda yakin ingin mengubah data tersebut? Ketik 1 jika ingin dilanjutkan dan 0 jika ingin dibatalkan: ")
                if(yakinupdate=='1'):
                    listsayuran[z]['kode']=kodesayuran
                    listsayuran[z]['nama']=namasayuran
                    listsayuran[z]['stock']=stocksayuran
                    listsayuran[z]['harga']=hargasayuran
                    listsayuran[z]['expired']=expiredsayuran
                    print("\nSelamat, data di bawah ini sudah berhasil diperbaharui!\n")    
                    print('Kode\t| Nama  \t| Stock\t| Harga\t| Expired')
                    print('{}\t| {}  \t| {}\t| {}\t| {}'.format(kodesayuran,namasayuran,stocksayuran,hargasayuran,expiredsayuran))
                    mengubahproduk()
                elif(yakinupdate=='0'):
                    mengubahproduk()
                else:
                    print("\nInput yang Anda masukkan tidak sesuai, silakan ulangi!")
                    mengubahproduk()
            elif(mauupdate=='0'):
                mengubahproduk()
            else:
                print("\nInput yang Anda masukkan tidak sesuai, silakan ulangi!")
                mengubahproduk()        
        else:      
            print("\nMaaf, data yang Anda cari tidak ada.")
            mengubahproduk() 

    elif(inputmenu3=='2'):
        pass
    
    else:
        print("\nMohon masukkan input dengan angka antara 1-2 saja.")
        mengubahproduk()

def menghapusproduk(): #function untuk menu DELETE DATA
    inputmenu4=input('''
MENGHAPUS PRODUK
1. MENGHAPUS DATA SAYURAN
2. EXIT MENU 

Masukkan angka menu yang Anda inginkan: ''')    

    if(inputmenu4=='1'):
        semuaproduk() 
        indexhapus= int(input('\nMasukkan kode sayuran yang ingin dihapus: '))
        daftarkodesayuran=[] #list daftarkodesayuran ini dibuat untuk menampung value dari key kode sayuran saja, sehingga bisa dimanfaatkan untuk mencari keberadaan data berdasarkan kodenya.
        for x in range(len(listsayuran)):
            getkode=[listsayuran[x].get('kode')]
            daftarkodesayuran.extend(getkode)
        if(indexhapus in daftarkodesayuran): 
            k=daftarkodesayuran.index(indexhapus) #variabel ini diperlukan untuk mencari tahu indeks dari input yang dimasukkan user.   
            yakinhapus=input("\nAnda yakin ingin menghapus produk dengan kode {}?. Ketik 1 jika ingin dilanjutkan dan 0 jika ingin dibatalkan: ".format(indexhapus))   
            if(yakinhapus=="1"):            
                del listsayuran[k]
                print("\nData dengan kode {} sudah terhapus!".format(indexhapus))
                menghapusproduk()
            elif(yakinhapus=="0"):
                menghapusproduk()  
            else:
                print("\nInput yang Anda masukkan tidak sesuai, silakan ulangi!")
                menghapusproduk()     
        else:
                print("\nData yang anda cari tidak ada.")
                menghapusproduk()
    
    elif(inputmenu4=='2'):
        pass
    
    else:
        print("\nMohon masukkan input dengan angka antara 1-2 saja.")
        menghapusproduk()

while(True): #blok while statement ini berfungsi untuk menampilkan menu utama program.
    menuutama = input('''
Selamat Datang di Tukang Sayur

DAFTAR MENU :
1. MENAMPILKAN DAFTAR PRODUK
2. MENAMBAHKAN PRODUK
3. MENGUBAH PRODUK
4. MENGHAPUS PRODUK
5. STOP PROGRAM

Masukkan angka menu yang Anda inginkan: ''')

    if(menuutama == '1') :
        menampilkanmenuproduk()
    elif(menuutama == '2') :
        menambahkanproduk()
    elif(menuutama == '3') :
        mengubahproduk()
    elif(menuutama == '4') :
        menghapusproduk()
    elif(menuutama == '5') :
        break #menghentikan program utama
    else:
        print("\nPilihan menu yang anda masukkan salah, silakan input angka 1-5 saja!") 