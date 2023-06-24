import requests
import os
import random
import string
import time
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.table import box 
from rich.align import Align 

menu_options = {
   1: 'Random user & password',
   2: 'Random user & password with gmail domain',
   3: 'Random user & password with random domain',
   4: 'Exit',
}
random_domain = ['gmail.com','hotmail.com','outlook.com','live.com','email.com','yahoo.com','icloud.com','msn.com','edu.com','free.fr','web.de','mail.ru']
title_markdown = """
# Simple Phishing Spammer |  Ctrl + C for interupt Spamming
"""
md = Markdown(title_markdown)
console = Console(log_path=False)

SRM_logo = """
  █████████  ███████████   ██████   ██████
 ███░░░░░███░░███░░░░░███ ░░██████ ██████ 
░███    ░░░  ░███    ░███  ░███░█████░███ 
░░█████████  ░██████████   ░███░░███ ░███ 
 ░░░░░░░░███ ░███░░░░░███  ░███ ░░░  ░███ 
 ███    ░███ ░███    ░███  ░███      ░███ 
░░█████████  █████   █████ █████     █████
 ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░     ░░░░░                                                                                            
"""
#FUNCTIONS
def print_menu():

    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("No",justify="center",style='bold bright_yellow')
    table.add_column("Options",justify="center",style='gold1')

    for key in menu_options.keys():
        table.add_row('['+str(key)+']',Align(menu_options[key],'left'))
    console.print(table)
    
def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

def print_title():
    console.print(SRM_logo, justify="center",style="bright_cyan")
    console.print('https://github.com/Seftirobim/SimplePhishingSpammer', justify="center", style="bold grey100")
    console.print(md)

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choices(letters, k=length))

# get random username from file
def get_random_username():

	user_file = 'usernames.txt'
	with open(user_file,"r",encoding="utf8") as file:
		usernames = file.read().splitlines()
	return random.choice(usernames)

#get random password from file
def get_random_pass():

	pass_file= 'passwords.txt'
	with open(pass_file,"r",encoding="utf8") as file:
		passwords = file.read().splitlines()
	return random.choice(passwords)

	

def fill_submit_form(url,mail_format):

	try:
		#COUNTING LOOP
		s = 1
		while True:
			try:
				
				resp = requests.get(Targeturl)
				soup = BeautifulSoup(resp.content,'html.parser')
				# Cari input sesuai type
				findInputText = soup.find('input',{'type':'text'})
				findInputPass = soup.find('input',{'type':'password'})

				if findInputText is None or findInputPass is None:
					console.print("Tidak ada form input type text atau password | Atau web sudah down silahkan check website | Atau kesalahan input,periksa inputanmu",style="red1")
					console.print("Sedang menghubungkan lagi...",style="spring_green1")
					time.sleep(5)
					continue
				#Dapetin valuenya dari attribute name
				get_username_value = findInputText.get('name')
				get_pass_value = findInputPass.get('name')

				if mail_format is None: username = get_random_username()
				elif mail_format == 'gmail': username = get_random_username()+"@gmail.com"
				else: username = get_random_username()+'@'+random.choice(random_domain)
					
				random_string = generate_random_string(8)
				rm_random_pass_spaces = get_random_pass().replace(" ","") #remove spaces
				join_pass =  ''.join([rm_random_pass_spaces,random_string])

				min = 9 # atur panjang minimal password
				max = 13 # atur panjang maximal password
				if len(rm_random_pass_spaces) == min: password = rm_random_pass_spaces
				elif len(rm_random_pass_spaces) < min:
					selisih = len(join_pass)-min
					password = join_pass[: - selisih] 
				elif len(rm_random_pass_spaces) > min:
					selisih = len(join_pass)-max
					password = join_pass[: - selisih]
				
				data = {
					get_username_value : username,
					get_pass_value : password
				}
				push_data = requests.post(url, data=data)

				if push_data.status_code == 200:
					console.log(f"Spam ke {s} dengan username: {username} dan password: {password}",style="bright_green")
				else:
					console.print("Koneksi Timeout, mencoba lagi dalam beberapa detik...",style="bright_cyan")
					time.sleep(3) 
				s += 1
				#time.sleep(0.2)

			except (requests.exceptions.ConnectionError,requests.Timeout, requests.RequestException):
				console.print("Koneksi Timeout, mencoba lagi dalam beberapa detik...",style="bright_cyan")
				time.sleep(3) 
	except KeyboardInterrupt:
		#Shows the total number of spammed login attempts
		print(drawLine('='))
		if (s-1 == 0):
			console.print("Gagal di spam!",style="red1")
		else:
			console.print('Berhasil di spam {} kali ke {} ! <- Keyboard Interupt'.format(s-1, Targeturl),style="bold spring_green1")


# RUN PROGRAM
# Terminal header
print_title()
print_menu()
    

while True:
	option = ''
	try:
		option = int(input("Select an option between [1-4] : "))
	except:
		None
	if option == 1:
		Targeturl = input ("Enter Target Url : ")
		fill_submit_form(Targeturl,None)
		break
	elif option == 2:
		Targeturl = input ("Enter Target Url : ")
		fill_submit_form(Targeturl,'gmail')
		break
	elif option == 3:
		Targeturl = input ("Enter Target Url : ")
		fill_submit_form(Targeturl,"random")
		break
	elif option == 4:
		console.print("Exit!",style="bold red1")
		break
	else:
		console.print("Invalid input ! Choose an option beetween [1-4]",style="cyan")
