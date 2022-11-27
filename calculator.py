def Choice(number1,number2):
    print '''__ISLEM MENUSU__
1.Toplama Islemi
2.Cikarma Islemi
3.Carpma Islemi
4.Bolme Islemi'''
    vote=raw_input("Lütfen Bir Secim Yapiniz: ")
    if(vote=="1"):print "Toplama Islemi Sonucu: ",number1+number2
    if(vote=="2"):print "Cikarma Islemi Sonucu: ",number1-number2
    if(vote=="3"):print "Carpma Islemi Sonucu: ",number1*number2
    if(vote=="4"):print "Bolme Islemi Sonucu: ",number1/number2

number1=input("Birinci Sayiyi Giriniz: ")
number2=input("Ikinci Sayiyi Giriniz: ")
Choice(number1,number2)

