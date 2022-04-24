from colorama import Fore,Style
import smtplib
import time
import os
import getpass
import sys

class bcolors:
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'


def bomb():
	os.system('clear')
	print (f'''


█▀▀ █▀▄▀█ ▄▀█ █ █░░   █ █▄░█ █░█ ▄▀█ █▀▄ █▀▀ █▀█
██▄ █░▀░█ █▀█ █ █▄▄   █ █░▀█ ▀▄▀ █▀█ █▄▀ ██▄ █▀▄

''' )


os.system('clear')


#Input
print( f'''{Fore.CYAN}

░░░░░░▄▄▄▄▀▀▀▀▀▀▀▀▄▄▄▄▄▄▄
░░░░░█░░░░░░░░░░░░░░░░░░▀▀▄
░░░░█░░░░░░░░░░░░░░░░░░░░░░█
░░░█░░░░░░▄██▀▄▄░░░░░▄▄▄░░░░█
░▄▀░▄▄▄░░█▀▀▀▀▄▄█░░░██▄▄█░░░░█
█░░█░▄░▀▄▄▄▀░░░░░░░░█░░░░░░░░░█     
█░░█░█▀▄▄░░░░░█▀░░░░▀▄░░▄▀▀▀▄░█
░█░▀▄░█▄░█▀▄▄░▀░▀▀░▄▄▀░░░░█░░█
░░█░░░▀▄▀█▄▄░█▀▀▀▄▄▄▄▀▀█▀██░█
░░░█░░░░██░░▀█▄▄▄█▄▄█▄▄██▄░░█
░░░░█░░░░▀▀▄░█░░░█░█▀█▀█▀██░█
░░░░░▀▄░░░░░▀▀▄▄▄█▄█▄█▄█▄▀░░█
░░░░░░░▀▄▄░░░░░░░░░░░░░░░░░░░█
░░▐▌░█░░░░▀▀▄▄░░░░░░░░░░░░░░░█
░░░█▐▌░░░░░░█░▀▄▄▄▄▄░░░░░░░░█
░░███░░░░░▄▄█░▄▄░██▄▄▄▄▄▄▄▄▀
░▐████░░▄▀█▀█▄▄▄▄▄█▀▄▀▄
░░█░░▌░█░░░▀▄░█▀█░▄▀░░░█
░░█░░▌░█░░█░░█░░░█░░█░░█
░░█░░▀▀░░██░░█░░░█░░█░░█
░░░▀▀▄▄▀▀░█░░░▀▄▀▀▀▀█░░█
░░░░░░░░░░█░░░░▄░░▄██▄▄▀     {Fore.WHITE}  █▀▀ █▀▄▀█ ▄▀█ █ █░░   █ █▄░█ █░█ ▄▀█ █▀▄ █▀▀ █▀█{Fore.CYAN}
░░░░░░░░░░█░░░░▄░░████       {Fore.WHITE}  ██▄ █░▀░█ █▀█ █ █▄▄   █ █░▀█ ▀▄▀ █▀█ █▄▀ ██▄ █▀▄{Fore.CYAN}    
░░░░░░░░░░█▄░░▄▄▄░░▄█                     
░░░░░░░░░░░█▀▀░▄░▀▀█        {Fore.GREEN} Yahoo: {Fore.CYAN}https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps{Fore.CYAN}
░░░░░░░░░░░█░░░█░░░█        {Fore.GREEN} Gmail: {Fore.CYAN}https://myaccount.google.com/lesssecureapps {Fore.CYAN} 
░░░░░░░░░░░█░░░▐░░░█ 
░░░░░░░░░░░█░░░▐░░░█        {Fore.RED} If Your {Fore.BLUE}Username {Fore.RED}or {Fore.BLUE}Password {Fore.RED}is incorrect{Fore.CYAN} 
░░░░░░░░░░░█░░░▐░░░█        {Fore.RED} you need to enable {Fore.YELLOW}[Less Secure Apps]{Fore.CYAN}
░░░░░░░░░░░█░░░▐░░░█
░░░░░░░░░░░█░░░▐░░░█         {Fore.CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
░░░░░░░░░░░█▄▄▄▐▄▄▄█         {Fore.CYAN}| {Fore.WHITE} Coded By: RetroPackets                    {Fore.CYAN}|
░░░░░░░▄▄▄▄▀▄▄▀█▀▄▄▀▄▄▄▄     {Fore.CYAN}|{Fore.WHITE} Instagram: @retropacketz                   {Fore.CYAN}|
░░░░░▄▀▄░▄░▄░░░█░░░▄░▄░▄▀▄   {Fore.CYAN}|   {Fore.WHITE} Github: https://github.com/RetroPackets {Fore.CYAN}|
░░░░░█▄▄▄▄▄▄▄▄▄▀▄▄▄▄▄▄▄▄▄█   {Fore.CYAN}~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
{Fore.CYAN}--------------------------
{Fore.WHITE}[1] {Fore.GREEN}Gmail
{Fore.WHITE}[2] {Fore.GREEN}Yahoo
{Fore.WHITE}[3] {Fore.GREEN}Hotmail/Outlook
''')
try:
	server = input(f'{Fore.WHITE}Choose An Option{Fore.YELLOW}:{Fore.GREEN} ')
	user = input(f'{Fore.BLUE}Your Email{Fore.YELLOW}: ')
	pwd = getpass.getpass(f'{Fore.BLUE}Password{Fore.YELLOW}: ')
	to = input(f'{Fore.BLUE}To{Fore.YELLOW}: ')
	subject = input(f'{Fore.BLUE}Subject (Optional){Fore.YELLOW}: ')
	body = input(f'{Fore.BLUE}Message{Fore.YELLOW}: ')
	nomes = input(f'{Fore.BLUE}Number of Emails to send{Fore.YELLOW}: ')
	no = 0
	message = 'From: ' + user + '\nSubject: ' + subject + '\n' + body
except KeyboardInterrupt:
	print (bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
	sys.exit()

#Gmail

if server == '1' or server == 'gmail' or server == 'Gmail':
	bomb()
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print (f'''{Fore.RED}Your {Fore.BLUE}Username {Fore.RED}or {Fore.BLUE}Password {Fore.RED}is incorrect, please try again using the correct credentials
		Or you need to enable {Fore.YELLOW}[Less Secure Apps]{Fore.RED}
		On Gmail: {Fore.CYAN}https://myaccount.google.com/lesssecureapps ''')
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print (f'{Fore.WHITE}[Email Invader]{Fore.GREEN} SENT:{Fore.YELLOW} ' + str(no+1) + f' {Fore.CYAN}EMAILS')
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print (bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print (f"{Fore.CYAN}[Email Invader] {Fore.RED}FAILED TO SEND ")
	server.close()
	
#Yahoo
elif server == '2' or server == 'Yahoo' or server == 'yahoo':
	server = smtplib.SMTP("smtp.mail.yahoo.com", 587)
	bomb()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print (f'''{Fore.RED}Your {Fore.BLUE}Username {Fore.RED}or {Fore.BLUE}Password {Fore.RED}is incorrect, please try again using the correct credentials
		Or you need to enable {Fore.YELLOW}[Less Secure Apps]
		On Yahoo: {Fore.CYAN}https://login.yahoo.com/account/security?.scrumb=Tiby8TXUvJt#less-secure-apps
		''')
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print (f'{Fore.WHITE}[Email Invader]{Fore.GREEN} SENT:{Fore.YELLOW} ' + str(no + 1) + ' {Fore.CYAN}EMAILS')
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print (bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except:
			print (f"{Fore.CYAN}[Email Invader] {Fore.RED}FAILED TO SEND ")
	server.close()
	
#Hotmail/Outlook
elif server == '3' or server == 'outlook' or server == 'Outlook' or server == 'Hotmail' or server == 'hotmail':
	server = smtplib.SMTP("smtp-mail.outlook.com", 587)
	bomb()
	server.ehlo()
	server.starttls()
	try:
		server.login(user, pwd)
	except smtplib.SMTPAuthenticationError:
		print (f'{Fore.RED}Your {Fore.BLUE}Username {Fore.RED}or {Fore.BLUE}Password {Fore.RED}is incorrect, please try again using the correct credentials')
		sys.exit()
	while no != nomes:
		try:
			server.sendmail(user, to, message)
			print (f'{Fore.WHITE}[Email Invader]{Fore.GREEN} SENT: {Fore.YELLOW}' + str(no + 1) + ' {Fore.CYAN}EMAILS' + bcolors.ENDC)
			no += 1
			time.sleep(.8)
		except KeyboardInterrupt:
			print (bcolors.FAIL + '\nCanceled' + bcolors.ENDC)
			sys.exit()
		except smtplib.SMTPAuthenticationError:
			print (f'\n{Fore.RED}The {Fore.BLUE}Username {Fore.RED}or {Fore.BLUE}Password {Fore.RED}you entered is incorrect.')
			sys.exit()
		except:
			print (f"{Fore.CYAN}[Email Invader] {Fore.RED}FAILED TO SEND ")
	server.close()
	
else:
	print (f'{Fore.YELLOW}Works only with {Fore.BLUE}Gmail{Fore.YELLOW}, Yahoo{Fore.YELLOW}, Outlook {Fore.YELLOW}and {Fore.BLUE}Hotmail{Fore.YELLOW}.')
	sys.exit()
