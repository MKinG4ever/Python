from random import random as rnd
from time import sleep as dly
from os import system as cmd


# keep Network Lookup a live
# this script is write only for linux
# and it's open source
# Enjoy


_ip = input('Enter ip Address: ')  # x.x.x.x
_ips = '.'.join(_ip.split('.')[:-1])  # x.x.x[.x] -> x.x.x


# The linux commands that used: nmap, arp, clear
def auto(no):
	for n in range(1,no+1):
		# - Presentation Part
		cmd('clear')  # os.system() -> cmd()
		print(f'-> {_ip} \t [ROUND:{n}]')
		print('\nInitiation...\n')
		dly(1)  # time.sleep() -> dly()
		
		# - Command Part
		# cmd(f'ping -c 10 {ip}')
		# cmd(f'fping {ip}')
		cmd(f'nmap {_ip}/24 ')
		print('\n- NMAP Done!\n')
		cmd(f'echo; nmap {_ip}/24 >> bak.txt')
		
		# - Command Part 2
		cmd(f'arp')
		cmd(f'echo; arp >> bak.txt')
		print('\n- ARP Done!\n')
		dly(1)
		
		# - Interruptind Part (delay/sleep/standby)
		for i in range(60):
			print(f'\r{str(i).zfill(3)}/{i/6*10:.1f}-100%',end='')
			dly(1)
			
		# - Restart Part
    cmd(f'echo; echo {n} >> bak.txt')
		print('\nroot@root:~$ sudo re-start',end='')
		dly(1)
		chs=''
		for ch in 're-starting all the process ..... ':
			chs+=ch
			print(f'\r{chs}',end='')
			dly(rnd())
	
	print('\nDone!')  # end of script

rand = int(input('Round time: '))
auto(rand)
