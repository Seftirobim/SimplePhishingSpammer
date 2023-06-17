import requests
import os
import random
import string
from rich.console import Console



#FUNCTIONS
console = Console(log_path=False)
def drawLine(symbol):
    rows, columns = os.get_terminal_size()
    i = symbol
    for x in range(2, rows):
        i += symbol
    return i

def allign_center(text):
    rows, columns = os.get_terminal_size()
    devided = rows - 1
    return devided

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))


def fill_submit_form(url):

	
	#COUNTING LOOP
	s = 1	
	try:
		while True:
			username = generate_random_string(10) # ubah panjang username sesuai kemauan
			password = generate_random_string(12) # ubah panjang username sesuai kemauan

			data = {
				input_username : username,
				input_password : password
			}
			response = requests.post(url, data=data)

			if response.status_code == 200:
				console.log(f"Spam ke {s} dengan username: {username} dan password: {password}")
				#print(f"Sukses ke {s} dengan username: {username} dan password: {password}")
			else:
				print("Failed")
			s += 1
			#time.sleep(0.2)		
	except requests.exceptions.ConnectionError as e:
		print ("Koneksi Timeout, Silahkan jalankan lagi")
		 
	except KeyboardInterrupt:
	    #Shows the total number of spammed login attempts
	    print(drawLine('='))
	    print('Berhasil di spam {} kali ke {} !'.format(s-1, Targeturl))
	


#Terminal header
title = 'Simple Phising Spammer '
print(drawLine('+'))
print(str.center(title, allign_center(title)))
print(str.center('github.com/v3lip/PhishingSpammer', allign_center('github.com/v3lip/PhishingSpammer')))
print(drawLine('+'))

#INPUT
input_username = "email"
input_password = "pass"
Targeturl = "https://gsi.mypict1.com/"

#RUN PROGRAM
fill_submit_form(Targeturl)	



   
