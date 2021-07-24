print("""
#########   ########     #      #   ########     ############                     
#       #   #            #    #     #      #     #          #
#       #   #            #  #       #      #     #          #
#########   ########     # #        ########     ############
#       #   #            #  #       #  #         #          #
#       #   #            #    #     #    #       #          #
#########   ########     #      #   #      #     #          #
\n Made by @EBSSecurty
""")
print("www.ebubekirbastama.com"+"\n")
import subprocess

komutumprocess = 'adb.exe shell ps'
komutumls = 'adb.exe shell ls -all'
komutumnetstat = 'adb.exe shell netstat'
devicessinfoversion = 'adb.exe shell getprop'
log = 'adb.exe logcat -d > telefonlogları.txt'
bugreport='adb.exe bugreport > telefonBuglogları.txt'
sysdump='adb.exe shell dumpsys > telefonBütün_Bilgileri.txt'
packetdump='adb.exe shell dumpsys activity > Paketisimleri.txt'
memdump='adb.exe  shell dumpsys meminfo > meminfo.txt'
memdumpdetayli='adb.exe  shell dumpsys meminfo'
komutpegasus='adb.exe  shell ls -all /sdcard/  > SdcardListe.txt'

print("1-) Process Listeleme"+"\n"+"2-) Klasör ve Ayrıntıları Listeleme"+"\n"+"3-) Netstat Çalıştırma"+"\n"+"4-) Telefon Detaylı Versiyon Bilgileri"+"\n"+"5-) Telefon Logları Çıktı Al"
      +"\n"+"6-) Telefon Bug Report Çıktı Al"+"\n"+"7-) Bütün Telefon Sistem Bilgileri(Wifi,batarya vb.)"+"\n"+"8-) Telefondaki Bütün Apk Paket İsimleri."
      +"\n"+"9-) Telefon Memori Packet Bilgileri"+"\n"+"10-) Packet İsmine Göre Memoriden Bilgi Getir."+"\n"+"11-) Pegasus Casus Yazılım Sdcard Liste alma"
      )

numara=input("Neyapmak İstersin..."+"?\n")

if numara == "1":
    piey = subprocess.Popen(komutumprocess, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print(gelenveri)
elif numara == "2":
    piey = subprocess.Popen(komutumls, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print(gelenveri)
elif numara == "3":
    piey = subprocess.Popen(komutumnetstat, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print(gelenveri)
elif numara == "4":
    piey = subprocess.Popen(devicessinfoversion, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print(gelenveri)
elif numara == "5":
    piey = subprocess.Popen(log, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Loglar Başarılı Bir Şekilde Aktarıldı.")
elif numara == "6":
    print("Aktarım Uzun Sürecektir Lütfen Bekleyiniz...")
    piey = subprocess.Popen(bugreport, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Loglar Başarılı Bir Şekilde Aktarıldı.")
elif numara == "7":
    print("Aktarım Uzun Sürecektir Lütfen Bekleyiniz...")
    piey = subprocess.Popen(sysdump, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Sistem Bilgileri Başarılı Bir Şekilde Aktarıldı.")
elif numara == "8":
    print("Aktarım Uzun Sürecektir Lütfen Bekleyiniz...")
    piey = subprocess.Popen(packetdump, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Packed Bilgileri Başarılı Bir Şekilde Aktarıldı.")
elif numara == "9":
    print("Aktarım Uzun Sürecektir Lütfen Bekleyiniz...")
    piey = subprocess.Popen(memdump, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Memori Bilgileri Başarılı Bir Şekilde Aktarıldı.")
elif numara == "10":
    packet_ismi = input("Lütfen Packet İsmini Yazınız Örnk(com.whatsapp)" + "?\n")
    dtyy=memdumpdetayli+" "+packet_ismi+" > memdetayliinfo.txt"
    piey = subprocess.Popen(dtyy, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Memori Bilgileri Başarılı Bir Şekilde Aktarıldı.")
elif numara == "11":
    print("Sdcard Dosyalar Listeleniyor...")
    piey = subprocess.Popen(memdump, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = piey.communicate()
    gelenveri = piey.communicate()
    print("Sdcard Dosyalar Başarılı Bir Şekilde Aktarıldı.")
