import requests,os,random,string,time
from bs4 import BeautifulSoup
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich.table import box 
from rich.align import Align 

### GLOBAL VARIABLE
menu_options = {
   1: 'Random user & password',
   2: 'Random user & password with gmail domain',
   3: 'Random user & password with random domain',
   4: 'Exit',
}

headers = requests.utils.default_headers()
headers.update({
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
})
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
### END GLOBAL VARIABLE

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

#get HTML content
def get_html_content(url):
	
	resp = requests.get(url,headers=headers)
	return BeautifulSoup(resp.content,'html.parser')

#find Input with type from HTML content
def find_input_type(url,type):
	return get_html_content(url).find('input',{'type':type})

def fill_submit_form(url,mail_format):

	try:
		#COUNTING LOOP
		s = 1
		while True:
			try:
				# Find Type from input
				findTypeText = find_input_type(url,'text')
				findTypePass = find_input_type(url,'password')
				# get The Value
				getValText = findTypeText.get('name')
				getValPass = findTypePass.get('name')

				if findTypeText is None or findTypePass is None:
					console.print("Tidak ada form input type text atau password | Atau web sudah down silahkan check website | Atau kesalahan input,periksa inputanmu",style="red1")
					console.print("Sedang menghubungkan lagi...",style="spring_green1")
					time.sleep(5)
					continue

				if mail_format is None: username = get_random_username()
				elif mail_format == 'gmail': username = get_random_username()+"@gmail.com"
				else: username = get_random_username()+'@'+random.choice(random_domain)
					
				random_string = generate_random_string(8)
				rm_random_pass_spaces = get_random_pass().replace(" ","") #remove spaces
				join_pass =  ''.join([rm_random_pass_spaces,random_string])

				min = 9 # atur panjang minimal password
				max = 13 # atur panjang maximal password

				# Adding a random string if it meets the criteria.
				if len(rm_random_pass_spaces) == min: password = rm_random_pass_spaces
				elif len(rm_random_pass_spaces) < min:
					selisih = len(join_pass)-min
					password = join_pass[: - selisih] 
				elif len(rm_random_pass_spaces) > min:
					selisih = len(join_pass)-max
					password = join_pass[: - selisih]
				
				data = {
					getValText : username,
					getValPass : password
				}
				push_data = requests.post(url, data=data,headers=headers)

				if push_data.status_code == 200:
					console.log(f"Spam ke {s} dengan username: {username} dan password: {password}",style="bright_green")
				else:
					console.print("Koneksi Timeout, mencoba lagi dalam beberapa detik...",style="bright_cyan")
					time.sleep(3) 
				s += 1

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
