def Menu():
    print''' ___CRUD ISLEMLERI___
1. Veri Tabanina Veri Ekleme
2. Veri Tabanindaki Verileri Okuma
3. Veri Tabanindaki Veriyi Guncelleme
4. Veri Tabanındaki Veriyi Silme '''
    vote=raw_input("Lutfen Yapacaginiz Islemi Seciniz: ")
    if(vote=="1"):Create()
    if(vote=="2"):List()
    if(vote=="3"):Update()
    if(vote=="4"):Delete()

def Create():
    print "Ekleme Fonksiyonu Calisti."
    
def List():
    print "Listeleme Fonksiyonu Calisti."

def Update():
    print "Guncelleme Fonksiyonu Calisti."

def Delete():
    print "Silme Fonksiyonu Calisti."

Menu()



