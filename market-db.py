def ekleme():    
    global urun
    global ID
    ID=int(input("Ürün ID giriniz: "))
    AD=str(input("Ürünün adını giriniz: "))
    FIYAT=int(input("Ürün fiyatı giriniz: "))
    urun={ID:{"ad":AD,"fiyat":FIYAT },}
def okuma():
    ara=int(input("Hangi ID aransın: "))
    dsyoku=open("db.txt","r")
    kont=dsyoku.readlines()
    # for i in kont:
    #     if i.startswith(str(ara)):
    #         print(i)
    
    print(lambda x:x in kont if (x.startswith(str(ara))))
def yazma():
    while True:
        try:
            dsy=open("db.txt","a")
        except:
            dsy=open("db.txt","w")
        else:
            break
    dsy.write(str(ID).ljust(10)+" "+str(urun[ID]["ad"]).center(10)+" "+str(urun[ID]["fiyat"]).rjust(10)+"\n")
secim=0
while(secim!=3):
    secim =int(input("Yapmak istediğiniz eylemi seçiniz: \n1) Ürün ekleme \n2)Ürün listeleme \n3)Çıkış\n"))
    if secim==1:
        ekleme()
        yazma()
        secim=0
    elif secim==2:
        okuma()
        secim=0