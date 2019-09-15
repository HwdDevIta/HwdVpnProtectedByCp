import os
import sys
import time
import signal
import random
import platform
class colors:
    OKGREEN = '\033[92m'
    END = '\n'
    OKRED = '\033[31m'
    OKYELLOW = '\033[33m'
    OKBLUE = '\033[34m'
    OKMANGENTA = '\033[35m'
    OKACQUA = '\033[36m'
d1 = 1,2,3,4,5,6,7,8,9
d2 = 10,11,12,13,14,15,16,17,17,19,20
d3 = 21,22,23,24,25,26,27,28,29,30
d4 = 31,32,33,34,35,36,37,38,39,40
dint = 100,200,300,400,500
dint3 = 110,120,130,140,150,160,170,180,190
dint4 = 342,455,243,454,845,927,234,645,233,445,454,232,123,454,653,653
dint2 = 600,700,800,900
os.system('clear')
print(colors.OKGREEN + "[STARTING]" + colors.END)
time.sleep(1)
deck = list(range(100, 120))

dstr = random.sample(deck, k=1)[0]

deck2 = list(range(100, 135))
dstr2 = random.sample(deck2, k=1)[0]

deck3 = list(range(10, 90))
dstr3 = random.sample(deck3, k=1)[0]

deck4 = list(range(1, 9))



dstr4 = random.sample(deck4, k=1)[0]

ip = str(dstr) + '.' + str(dstr2) + '.' + str(dstr3) + '.' + str(dstr4)
netmsk = str(dstr) + '.' + str(dstr2) + '.' + str(dstr4)

Permission = input(colors.END + colors.OKGREEN + "[PRESS ONE BUTTON TO CHANGE IP/Ctrl + C to Stop]" + colors.END)
if(Permission == ""):
   print(ip)
   myCmd = f'sudo ifconfig wlan0 {ip} netmask {netmsk}'
   os.system(myCmd)
   myCmd = f'sudo route add default gw {ip} wlan0'
   os.system(myCmd)
   myCmd = f'route -n'
   os.system(myCmd)
   myCmd = f'servce network-manager restart'
   os.system(myCmd)
   print(colors.OKGREEN + "[IP-CHANGED]" + colors.END)
   myCmd = 'HwdUltraVpnStatic.py'
   os.system(myCmd)