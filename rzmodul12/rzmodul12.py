import mysql.connector

cnx=mysql.connector.connect(host='localhost',
                            user='root',
                            database='keretaapi')

def selectPenumpang(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM penumpang'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Penumpang')

def selectKeretaApi(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM kereta_api'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Kereta Api')

def selectPembelian(cnx):
    cursor=cnx.cursor()

    sql='SELECT*FROM pembelian'

    cursor.execute(sql)

    results=cursor.fetchall()
    print(results)

    print('data Pembelian')

def tambahPenumpang(cnx):
    cursor=cnx.cursor()

    idPenumpang=input('Masukkan id Penumpang: ')
    namaPenumpang=input ('Masukkan Nama Penumpang: ')
    alamatPenumpang=input ('Masukkan alamat Penumpang: ')

    sql='INSERT INTO penumpang (idPenumpang, namaPenumpang, alamatPenumpang) VALUES (%s, %s, %s)'
    val=(idPenumpang, namaPenumpang, alamatPenumpang)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def tambahKeretaApi(cnx):
    cursor=cnx.cursor()

    idKeretaApi=input('Masukkan id Kereta: ')
    namaKeretaApi=input('Masukkan nama Kereta: ')
    kelasKeretaApi=input('Masukkan kelas Kereta: ')
    jadwalKeretaApi=input('Masukkan jadwal Kereta: ')

    sql='INSERT INTO kereta_api (idKeretaApi, namaKeretaApi, kelasKeretaApi, jadwalKeretaApi) VALUES (%s, %s, %s, %s)'
    val=(idKeretaApi, namaKeretaApi, kelasKeretaApi, jadwalKeretaApi)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def tambahPembelian(cnx):
    cursor=cnx.cursor()

    idPembelian=input('Masukkan id Pembelian: ')
    asalstasiun=input('Masukkan asal Stasiun: ')
    tujuanstasiun=input('Masukkan tujuan Stasiun: ')
    

    sql='INSERT INTO pembelian (idPembelian, asalstasiun, tujuanstasiun) VALUES (%s, %s, %s)'
    val=(idPembelian, asalstasiun, tujuanstasiun)

    cursor.execute(sql, val)
    cnx.commit()
    print('Berhasil ditambahkan')

def hapusPenumpang(cnx):
    cursor=cnx.cursor()

    idPenumpang=input('Masukkan id Penumpang: ')
    sql='DELETE FROM penumpang WHERE idPenumpang=%s'
    val=(idPenumpang, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def hapusKeretaApi(cnx):
    cursor=cnx.cursor()

    idKeretaApi=input('Masukkan id Kereta: ')
    sql='DELETE FROM kereta_api WHERE idKeretaApi=%s'
    val=(idKeretaApi, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def hapusPembelian(cnx):
    cursor=cnx.cursor()

    idPembelian=input('Masukkan id Pembelian: ')
    sql='DELETE FROM pembelian WHERE idPembelian=%s'
    val=(idPemebelian, )

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil dihapus')

def updatePenumpang(cnx):

    cursor=cnx.cursor()
    
    idPenumpang=input('Masukkan id Penumpang: ')
    namaPenumpang=input ('Masukkan Nama baru: ')
    alamatPenumpang=input ('Masukkan alamat baru: ')

    sql='UPDATE penumpang SET namaPenumpang=%s, alamatPenumpang=%s WHERE idPenumpang=%s'
    val=(namaPenumpang, alamatPenumpang, idPenumpang)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')

def updateKeretaApi(cnx):

    cursor=cnx.cursor()
    
    idKeretaApi=input('Masukkan id Kereta: ')
    namaKeretaApi=input('Masukkan nama baru: ')
    kelasKeretaApi=input('Masukkan kelas baru: ')
    jadwalKeretaApi= input('Masukkan jadwal baru: ')
    
    sql='UPDATE kereta_api SET namaKeretaApi=%s, kelasKeretaApi=%s, jadwalKeretaApi=%s WHERE idKeretaApi=%s'
    val=(namKeretaApi, kelasKeretaApi, jadwalKeretaApi, idKeretaApi)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')

def updatePembelian(cnx):

    cursor=cnx.cursor()
    
    idPembelian=input('Masukkan id Pembelian: ')
    asalstasiun=input('Masukkan asal Stasiun baru: ')
    tujuanstasiun=input('Masukkan tujuan Stasiun baru: ')

    sql='UPDATE pembelian SET asalstasiun=%s, tujuanstasiun=%s, WHERE idPembelian=%s'
    val=(asalstasiun, tujuanstasiun, idPembelian)

    cursor.execute(sql, val)
    cnx.commit()

    print('Berhasil update')


print("=====Aplikasi Database TIKET KERETA API=====")
print("1.Select")
print("2.Insert")
print("3.Delete")
print("4.Update")
print("0.Keluar")
menu=input("Pilih perintah : ")
print("===========================")
print("1.Penumpang")
print("2.Kereta Api")
print("3.Pembelian")
menu2=input("Pilih entitas : ")

if menu=="1":
    if menu2=="1":
        selectPenumpang(cnx)
    elif menu2=="2":
        selectKeretaApi(cnx)
    elif menu2=="3":
        selectPembelian(cnx)

elif menu=="2":
    if menu2=="1":
        tambahPenumpang(cnx)
    elif menu2=="2":
        tambahKeretaApi(cnx)
    elif menu2=="3":
        tambahPembelian(cnx)
        
elif menu=="3":
    if menu2=="1":
        hapusPenumpang(cnx)
    elif menu2=="2":
        hapusKeretaApi(cnx)
    elif menu2=="3":
        hapusPembelian(cnx)
        
elif menu=="4":
    if menu2=="1":
        updatePenumpang(cnx)
    elif menu2=="2":
        updateKeretaApi(cnx)
    elif menu2=="3":
        updatePembelian(cnx)
    
    
elif menu=="0":
    exit()
else:
    print("salah")
