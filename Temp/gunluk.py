
print("""
   _____ _   _       _ _   _ _    
  / ____(_) (_)     | (_) (_) |   
 | |  __ _   _ _ __ | |_   _| | __
 | | |_ | | | | '_ \| | | | | |/ /
 | |__| | |_| | | | | | |_| |   < 
  \_____|\__,_|_| |_|_|\__,_|_|\_\ 

  Copyright © 2020 Tüm Hakları Saklıdır.
                                  
""")

secim = input("""
[1] Dosya oku
[2] Dosya yaz
: """)

a = input("Günlük Adı :")

if secim == "1":
    try:         
        gunlukoku=open("Desktop\Günlük\ "+a+".günlük", "r")
        print("Yazı : "+gunlukoku.read())
        gunlukoku.close()
    except FileNotFoundError:
        print("Günlük dosyası bulunamadı.")

if secim == "2":
    try:
        b=input("Dosya dizini : ")
        gunlukyaz=open("Desktop\Günlük\ "+a+".günlük", "w+")
        yaz = input("Yazılacak yazı : ")
        gunlukyaz.write(yaz)
        gunlukyaz.close()
        print("Dosya başarıyla yazıldı.")
    except FileNotFoundError:
        print("Dosya yazılırken bir hata oluştu.")
