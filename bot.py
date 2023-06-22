import requests
import os
import random
import string
import time
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown



#FUNCTIONS
title_markdown = """
# Simple Phishing Spammer |  Ctrl + C for interupt
"""
md = Markdown(title_markdown)

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
    return ''.join(random.choice(letters) for _ in range(length))

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

	
console = Console(log_path=False)
def fill_submit_form(url):

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
				#Dapetin valuenya
				get_username_value = findInputText.get('name')
				get_pass_value = findInputPass.get('name')

				username = get_random_username()
				random_string = generate_random_string(8)
				join_pass =  get_random_pass()+random_string

				length = 12 # atur maksimal panjang password
				if len(join_pass) <= length:
					password = join_pass
				else:
					selisih = len(join_pass)-length
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
		if (s == 0):
			console.print("Gagal di spam!",style="red1")
		else:
			console.print('Berhasil di spam {} kali ke {} ! <- Keyboard Interupt'.format(s-1, Targeturl),style="bold spring_green1")
	


#Terminal header
print_title()

#INPUT
# input_username = input ("attribute name value for (username) ? : ") 
# input_password = input ("attribute name value for (password) ? : ")
Targeturl = input ("Enter Target Url : ")

#RUN PROGRAM
fill_submit_form(Targeturl)
